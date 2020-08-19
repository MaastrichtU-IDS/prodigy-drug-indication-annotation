This pipeline annoates for drug-disease relations. The task is to define the relation between a drug and a disease, if you cannot identify a drug and disease in a text, you may skip the text or reject.
Whenever possible, the Prodigy will tag disease and phrases that are helpful to identify relationship in the text for you.

**unzip diseases model**
```
unzip ../disease_ner/diseases-model.zip
```


**run relation annotation pipeline**
```
python3 -m prodigy rel.manual relation_data ../disease_ner/diseases-model ./dailymed_disease3.jsonl --label DISEASE_MODIFYING,SYMPTOMATIC_RELEIF --span-label DISEASE --d ./disable_patterns.jsonl --add-ents  --wrap
```

![alt text](https://github.com/MaastrichtU-IDS/prodigy-drug-indication-annotation/blob/master/relation/Screenshot%202020-08-19%20at%2010.04.37.png?raw=true)
