FROM python:3.8-alpine

WORKDIR /code

COPY . /code

# RUN pip install --upgrade pip
RUN apk update && \
    apk add --virtual build-deps gcc musl-dev

RUN pip3 install -r requirements.txt


# ENV STORAGE_PORT_EXT=4567
# ENV SCYLLA_NODES="scylla-node1,scylla-node2,scylla-node3"
# ENV SCYLLA_DEFAULT_KEYSPACE=""
# ENV ELASTICSEARCH_CLUSTER_NAME=elasticsearch-cluster
# ENV ELASTICSEARCH_CLUSTER_HOSTS=elasticsearch-node1,elasticsearch-node2
# ENV ELASTICSEARCH_HOST=elasticsearch
# ENV ELASTICSEARCH_PORT=9200
# ENV ELASTICSEARCH_SCHEME=http



CMD ["python3", "/code/server.py"]