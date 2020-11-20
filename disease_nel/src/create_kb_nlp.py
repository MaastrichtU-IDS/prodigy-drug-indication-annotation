import spacy
import os
import csv
from pathlib import Path
from spacy.kb import KnowledgeBase

from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import json

## Candidate generation 
## return candiatates and their probabilities for given label
def cand_gen(label, entities, ent2id, thres=70):
    cands = process.extract(label, entities,scorer=fuzz.token_sort_ratio, limit=5)
    total =0
    for c,s in cands:
        if s == 100: return [[ent2id[c]],[1.0]]
        if s>thres:
            total+=s
            #print (c,s)
    cands= [ (c,s/total) for c,s in cands if s>thres]
    qids = [ ent2id[c] for c,s in cands ]
    probs = [ s for c,s in cands ]
    return qids, probs

# parse jsonl file, return annotated text and labels
def parse_annots(annot_file_name):
    text_annots = {}
    ann_arr =[]
    with open(annot_file_name) as f:
        for l in f:
            res = json.loads(l)
            text = res['text']
            text_annots[text] = res
    return text_annots

nlp = spacy.load("../diseases-model")

def load_entities():
    entities_loc =   Path.cwd() / "../disease_entities.tsv"  # distributed alongside this notebook

    names = dict()
    descriptions = dict()
    with entities_loc.open("r", encoding="utf8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter="\t")
        #next(csvreader)
        for row in csvreader:
            qid = row[0]
            name = row[1]
            desc = row[2]
            names[qid] = name
            descriptions[qid] = desc
    return names, descriptions

name_dict, desc_dict = load_entities()

kb = KnowledgeBase(vocab=nlp.vocab, entity_vector_length=96)



# for each enitity, decsription vectors were added 
# if you didn't download correct the tokens vector, you need to change vector length
# if you download (python -m spacy download en_core_web_lg), the length should be 300
for qid, desc in desc_dict.items():
    desc_doc = nlp(desc)
    desc_enc = desc_doc.vector
    kb.add_entity(entity=qid, entity_vector=desc_enc, freq=342)   # 342 is an arbitrary value here

print (len(desc_enc))

#Now we want to specify aliases or synonyms. We first add the full names. Here, we are 100% certain that they resolve to their corresponding QID, as there is no ambiguity.
for qid, name in name_dict.items():
    kb.add_alias(alias=name, entities=[qid], probabilities=[1])   # 100% prior probability P(entity|alias)
    


aliases = {}
words = []
with open('disease_alieases.tsv', 'r') as fr:
    for row in fr:
        row = row.strip().split('\t')
        qid = row[0]
        name =row[1]
        #print (row)
        if kb.contains_entity(qid):
            aliases[name] = qid
            kb.add_alias(alias=name, entities=[qid], probabilities=[1])   # 100% prior probability P(entity|alias)


print ("Checking KB ...")
print (kb.contains_entity('MONDO:0000001'))

annots = parse_annots('dailymed_disease3_L.jsonl')


entity_labels = []
for text, res in annots.items():
    t=  res['text']
    for span in res['spans']:
        s = span['start']
        e = span['end']
        entity_labels.append(t[s:e])
        print (t[s:e])

entity_labels = list(set(entity_labels))

entities = name_dict.values()
ent2id= {v:k for k, v in name_dict.items()}

print ("Testing candidate generation")
print (entity_labels[0], cand_gen(entity_labels[0], entities, ent2id))

## adding (fuzzy matching) candidates into KB 
aliases = {}
words = []
for flabel in entity_labels:
    name = flabel
    qids, probs = cand_gen(flabel, entities, ent2id)
    if len(probs) ==1 and probs[0] ==1.0: continue
    kb.add_alias(alias=flabel, entities=qids, probabilities=probs)  # sum([probs]) should be <= 1 !

print(f"Candidates for 'hyperlipidemia': {[c.entity_ for c in kb.get_candidates('hyperlipidemia')]}")

# change the directory and file names to whatever you like
output_dir = Path.cwd() / "output"
if not os.path.exists(output_dir):
    os.mkdir(output_dir)
kb.dump(output_dir / "my_kb")

nlp.to_disk(output_dir / "my_nlp")
