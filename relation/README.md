This is a pipeline for drug-disease annoation. The task is to define relattion between drug and disease, if you can identify a drug and disease in a text, you can skip the text.
Whenever possible, the Prodigy will tag disease and phrases that are helpful to identify relationship for you.

**run relation annotation pipeline**
```
python3 -m prodigy rel.manual relation_data ../disease_ner/diseases-model ./dailymed_disease3.jsonl --label DISEASE_MODIFYING,SYMPTOMATIC_RELEIF --span-label DISEASE --d ./disable_patterns.jsonl --add-ents  --wrap
```
