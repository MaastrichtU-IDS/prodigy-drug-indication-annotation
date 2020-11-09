FROM python:3.7
# FROM jupyter/minimal-notebook


# ARG ANNOTATION_FILE=sample-annotations-md
# ARG DATASET_NAME=sample
# ARG LABELS_FILE=labels.txt
# ARG SAMPLE_SENTENCES_FILE=sample-sentences.txt
# ARG WHEEL_FILE=prodigy-1.10.0-cp36.cp37.cp38-cp36m.cp37m.cp38-linux_x86_64.whl


WORKDIR /root

# Add the licensed prodigy.whl file in the same directory as the Dockerfile
ADD . .

# ADD prodigy-1.10.0-cp36.cp37.cp38-cp36m.cp37m.cp38-linux_x86_64.whl ./prodigy-1.10.0-cp36.cp37.cp38-cp36m.cp37m.cp38-linux_x86_64.whl

# RUN rm -rf .cache

# Rename prodigy wheel file (from something like prodigy-1.10.0-cp36.cp37.cp38-cp36m.cp37m.cp38-linux_x86_64.whl)
# RUN mv prodigy*.whl prodigy.whl
# RUN mv prodigy-1.10.0-cp36.cp37.cp38-cp36m.cp37m.cp38-linux_x86_64.whl prodigy.whl

# RUN chmod +x prodigy-1.10.0-cp36.cp37.cp38-cp36m.cp37m.cp38-linux_x86_64.whl

RUN python -m pip install --upgrade pip

# RUN pip install ./${WHEEL_FILE}

RUN pwd
RUN ls -alh


## Pip is not able to simply install a wheel file.
# RUN pip install *.whl
# RUN pip install -e /root/prodigy-1.10.0-cp36.cp37.cp38-cp36m.cp37m.cp38-linux_x86_64.whl
# RUN pip install /root/*.whl
RUN python -m pip install *.whl

# RUN jupyter labextension install jupyterlab-prodigy

EXPOSE 8080

# VOLUME [ "/data" ]

# ENTRYPOINT [ "prodigy" "ner.manual" "reviews_ner" "en_core_web_sm" "./${ANNOTATION_FILE}" "--label" "${ANNOTATION_LABELS}" ]

ENTRYPOINT [ "python" "-m" "prodigy" "ner.manual" "${DATASET_NAME}" "blank:en" "./${SAMPLE_SENTENCES_FILE}" "-l" "./${LABELS_FILE}" ]
