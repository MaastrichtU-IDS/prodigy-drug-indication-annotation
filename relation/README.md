This pipeline annoates drug-disease relations. The task for annotators is to define the relation between a drug and a disease, if you cannot identify a drug and disease in a text, you may skip the text or reject.
Whenever possible, the Prodigy will tag disease and phrases that are helpful to identify relationship in the text for you.

<<<<<<< HEAD

**unzip diseases model
unzip ../disease_ner/diseases-model.zip

**run the relation annotation

=======
**unzip diseases model**
```
unzip ../disease_ner/diseases-model.zip
```


**run relation annotation pipeline**
>>>>>>> 3da3ec0af21935913000c7f389d06612ba14cf86
```
python3 -m prodigy rel.manual drugdisease_rel ../disease_ner/diseases-model ./dailymed_disease3.jsonl --label DISEASE_MODIFYING,SYMPTOMATIC_RELEIF --span-label DISEASE,DRUG,RELATION_PHRASE --patterns ./disable_patterns.jsonl --add-ents  --wrap
```

![alt text](https://github.com/MaastrichtU-IDS/prodigy-drug-indication-annotation/blob/master/relation/Screenshot%202020-08-19%20at%2010.04.37.png?raw=true)
