FROM amd64/python:3.8

ARG ANNOTATION_FILE=sample-annotations-md
ARG DATASET_NAME=sample
ARG LABELS_FILE=labels.txt
ARG SAMPLE_SENTENCES_FILE=sample-sentences.txt
ARG WHEEL_FILE=prodigy-1.10.0-cp36.cp37.cp38-cp36m.cp37m.cp38-linux_x86_64.whl

ENV ANNOTATION_FILE=${ANNOTATION_FILE}
ENV DATASET_NAME=${DATASET_NAME}
ENV LABELS_FILE=${LABELS_FILE}
ENV SAMPLE_SENTENCES_FILE=${SAMPLE_SENTENCES_FILE}
ENV WHEEL_FILE=${WHEEL_FILE}

# Add the licensed prodigy.whl file in the same directory as the Dockerfile
ADD . .

RUN pip install *.whl

EXPOSE 8080
VOLUME [ "/data" ]

ENTRYPOINT python -m prodigy ner.manual $DATASET_NAME blank:en $SAMPLE_SENTENCES_FILE -l $LABELS_FILE