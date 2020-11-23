# Drug Indication annotation using Prodi.gy

A project that uses [Prodigy](http://prodi.gy) to train a classifier to perform drug indication annotation with their medical context

**Requirement** 

```
python3 -m spacy download en_core_web_sm
pip3 install prodigy-....whl
```


**manual annoations for disease names using patterns**

```
python3 -m  prodigy ner.manual disease_ner_gold en_core_web_sm ../drugcentral-dailymed-labels.txt --label DISEASE -pt ./disease_patterns_doid.jsonl
```

**import the dataset**
```
python3 -m prodigy db-in disease_ner dailymed-annotations2-disease.jsonl
```

**train entity recoginition model**
```
python -m prodigy ner.batch-train [dataset] en_core_web_sm --output [model-name] --label [label] --eval-split [evaluation split ratio] --n-iter [number-of-iteration] --batch-szie [batch-size-for-NN]
python3 -m prodigy ner.batch-train disease_ner en_core_web_sm --output diseases-model  --label DISEASE --eval-split 0.2 --n-iter 20 --batch-size 8
```


**export the dataset**
```
python3 -m prodigy db-out dailymed --dry > dailymed-annotations.jsonl
```


