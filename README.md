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

**manually annotate the DailyMed drug labels and export the annotations**
```
python3 -m prodigy ner.manual dailymed blank:en ./drugcentral-dailymed-labels.txt -l ./indications_types.txt
python3 -m prodigy db-out dailymed --dry > dailymed-annotations.jsonl
```

## Run using Docker

1. Clone the repository

```bash
git clone https://github.com/MaastrichtU-IDS/prodigy-drug-indication-annotation
cd prodigy-drug-indication-annotation
```

2. Add the `prodigy.whl` file in the root directory, alongside the `Dockerfile`
3. Build with Docker:

```bash
docker build -t prodigy .
```

Unfortunately Prodigy is not build properly, and its installation fails when installed in docker (same file work on the local Ubuntu):

```Step 7/9 : RUN python -m pip install *.whl
Step 7/9 : RUN python -m pip install *.whl 
 ---> Running in 3c9e94427ab0
Processing ./prodigy-1.10.0-cp36.cp37.cp38-cp36m.cp37m.cp38-linux_x86_64.whl
ERROR: Exception:
Traceback (most recent call last):
  File "/usr/local/lib/python3.7/site-packages/pip/_internal/cli/base_command.py", line 228, in _main
    status = self.run(options, args)
  File "/usr/local/lib/python3.7/site-packages/pip/_internal/cli/req_command.py", line 182, in wrapper
    return func(self, options, args)
  File "/usr/local/lib/python3.7/site-packages/pip/_internal/commands/install.py", line 324, in run
    reqs, check_supported_wheels=not options.target_dir
  File "/usr/local/lib/python3.7/site-packages/pip/_internal/resolution/legacy/resolver.py", line 183, in resolve
    discovered_reqs.extend(self._resolve_one(requirement_set, req))
  File "/usr/local/lib/python3.7/site-packages/pip/_internal/resolution/legacy/resolver.py", line 391, in _resolve_one
    dist = abstract_dist.get_pkg_resources_distribution()
  File "/usr/local/lib/python3.7/site-packages/pip/_internal/distributions/wheel.py", line 29, in get_pkg_resources_distribution
    with ZipFile(self.req.local_file_path, allowZip64=True) as z:
  File "/usr/local/lib/python3.7/zipfile.py", line 1258, in __init__
    self._RealGetContents()
  File "/usr/local/lib/python3.7/zipfile.py", line 1325, in _RealGetContents
    raise BadZipFile("File is not a zip file")
zipfile.BadZipFile: File is not a zip file
The command '/bin/sh -c python -m pip install *.whl' returned a non-zero code: 2
```

4. Run with Docker on http://localhost:8080

```bash
docker run -it --name prodigy prodigy
```

You can also use a different annotation file and labels:

```bash
docker run -it --name prodigy -e DATASET_NAME=sample -e SAMPLE_SENTENCES_FILE=sample-sentences.txt -e LABELS_FILE=labels.txt prodigy
```

> Checkout the prodigy-recipes repository for more ways to use prodigy: https://github.com/explosion/prodigy-recipes

