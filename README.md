
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

The software component is responsible for managing document storage lifecycle and personnel.

### Folder hierarchy

        ├── core
        |  # base component for the server
        ├── features
        |  # each set of features is implemented in a folder
        └── storage
            ├── storage_service
            | # an abstraction for storage engines
            └── wrappers
            | # the implementation to handle 3rd party storage.

### Deploying

#### Docker

You can use docker-compose to build and deploy the containers:

    sudo docker-compose up -d

#### Native installation

Just try to convince your employer to switch to cloud services, if they would not, well.. good luck or find another job.


#### Development



### Progress
    
- Serving feature. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/75)
  - Documents.
  - Personnel.
  - Domains.
  - Origins.
  - Organisations.
- [x] 3rd Party storage solutions. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/70)
  - [x] SQL based storage.
    - [x] Insertion.
    - [x] Retrieval.
    - [ ] Search.
  - [ ] Elasticsearch.
    - [ ] Insertion.
    - [ ] Retrieval.
  - [ ] ~~ScyllaDB~~. (Aborted)

- [ ] Containerisation. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/85)
  - [x] Automation of deployment. (docker-compose)
  - [x] Smaller footprint.



<!-- >## NOTES: -->
>  
> 