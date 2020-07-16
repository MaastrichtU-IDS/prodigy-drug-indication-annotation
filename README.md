# Drug Indication annotation using Prodi.gy

A project that uses [Prodigy](http://prodi.gy) to train a classifier to perform drug indication annotation with their medical context

We define the following labels:

* DRUG: This refers to the official drug name or the active ingredient
* ROUTE: The route of administration (e.g. oral, intravenous, topical)
* FORMULATION: The formulation of the drug (e.g. solution, tablet)
* ACTION: The action between the drug and the condition (e.g. treatment of, management of)
* CONDITION: The condition that is indicated for the drug (e.g. tremors, pain)
* BASECONDITION: The base condition is the underlying pathophysiological state in which the indicated condition is a symptom of (e.g. parkinson's, cancer)
* ADJUNCT_TO: Where the drug acts as an adjunctive therapy, use this label to identify what it is combined with.
* AGE: The age of the patients for which the drug is indicated for.
* SYMPTOM: Symptoms that are mentioned that are part of the medical context of treatment.
* SIDEEFFECT: Side effects that appear in the statement.
* SEVERITY: The severity of the indicated condition.
* MEDICALCTX: Any sentences that discuss the medical context of the indication (notwithstanding age)
* OUTCOME: The primary anticipated outcome of the treatment.
* EFFECT: Any beneficial effects identified in the text as a result of the treatment.
* CONTRAINDICATION: Where the drug should not be used.
* INEFFECTIVE: Where the drug is ineffective.

**manually create new dataset**
   
```
python -m prodigy ner.manual [dataset-name] blank:en [sentence-file-path] -l [labels-file-path]
python -m prodigy ner.manual sample blank:en ./sample-sentences.txt -l ./labels.txt
```
the server will then start up and you can start annotating


**export annotations**
```
python -m prodigy db-out [dataset] --dry > [dataset.jsonl]
python -m prodigy db-out sample --dry > sample-annotations.jsonl

```

**review a dataset**
```
python -m prodigy review [reviewed-dataset-name] [dataset] -l [labels-file-path]
python -m prodigy review sample-review sample -l ./labels.txt

```

**export the patterns**
```
python -m prodigy terms.to-patterns [dataset] ./[dataset-patterns.jsonl] -l [labels-file-path] -m blank:en
python -m prodigy terms.to-patterns sample ./sample-patterns.jsonl -l ./labels.txt -m blank:en

```

**train the classifier**
```
python -m prodigy ner.teach [dataset] en_core_web_sm [corpus-filepath] -l [label-filepath] -pt [patterns-filepath]
python -m prodigy ner.teach sample en_core_web_sm ./[dpl-indications.csv] -l [./labels.txt] -pt ./sample-patterns.jsonl
```

**manually annotate the DailyMed drug labels and export the annotations

python3 -m prodigy ner.manual dailymed blank:en ./drugcentral-dailymed-labels.txt -l ./indications_types.txt
python3 -m prodigy db-out dailymed --dry > dailymed-annotations.jsonl
