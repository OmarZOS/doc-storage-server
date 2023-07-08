
## Document storage server
## Table of Contents

- Table of Contents
  - Description
  - Folder hierarchy
  - Deploying
    - Docker
    - Native installation
    - Development
  - Progress




### Description

This component is responsible of document storage
### Folder hierarchy

        ├── core
        |  # base component for the server
        ├── features
        |  # each feature is implemented in a file
        └── storage
            ├── storage_service
            | # an abstraction for storage engines
            └── wrappers
            | # the implementations for each 3rd party stores.

### Deploying

#### Docker

Use this command to build and deploy the containers:

    sudo docker-compose up -d

#### Native installation

Just try to convince your employer to switch to cloud services, if they would not, well.. good luck or find another employer.


#### Development



### Progress
    
- Serving feature. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/70)

- [x] 3rd Party storage solutions. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/60)
  - [ ] Elasticsearch.
    - [ ] Insertion.
    - [ ] Retrieval.
  - [x] SQL. (We're using sqlAlchemy)
    - [x] Insertion.
    - [x] Retrieval.
  - [ ] ~~ScyllaDB~~. (Review decision)

- [ ] Containerisation. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/85)
  - [x] Automation of deployment. (docker-compose)
  - [x] Smaller footprint.



>## NOTES:
> The software component is 
> 