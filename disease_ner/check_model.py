import spacy

nlp=spacy.load('diseases-model')



with open('../drugcentral-dailymed-labels.txt') as f:
    for l in f:
       doc =nlp(l)
       nents= [(ent.text, ent.label_) for ent in doc.ents]
       print (l)
       print (nents)
       input("next")
