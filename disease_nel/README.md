
**Manually link disease entities to a given set of options**

```
Generate NLP/KB  model (in 'output folder') using src/create_kb_nlp.py 
python src/create_kb_nlp.py

OR

Unzip "output.zip" to the main folder
unzip output.zip

```


```
python3 -m prodigy entity_linker.manual disease_nel dailymed_indsec_disease.txt output/my_nlp/ output/my_kb disease_entities.tsv -F el_recipe.py
```
