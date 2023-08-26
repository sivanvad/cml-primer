# CML Asset for Professional Services

## Introduction

Cloudera Machine Learning (CML) makes it easy to bring Data Scientists to the data platform and makes it easier to overcome the challenges they face on a day to day basis. Since industry standards are still evolving, there are new solutions required to fit new use cases. This repository is an effort to document solutions to common problems faced during implementation and utilisation of CML. By doing so, anyone with access to this repository can find solutions faster than they would do otherwise.

<div class="alert alert-block alert-info">
<b>Note:</b> This is not an exhaustive document. There can be scenarios that may not be covered here. In such cases, reach out the ML SME group. Please refer to Cloudera documentation on product related information.
</div>

## ML Lifecycle

ML lifecycle, in high level, provides a basis of any ML project. Stages in ML Lifecycle can be categorised into 4 stages in general:
* Data Engineering
* Data Science
* Machine Learning Operations (MLOps)
* Consumption (Business Users)

<img src="docs/ml_lifecycle_vanilla.png" width="1250" height="625">

Each stage involve different sets of users. In Phase 1, Data Science stage is focused as it forms the core of ML lifecycle.

## CML Projects

Before we begin with the ML lifecycle, you start by creating a CML project.

As per Cloudera documentation, `"Projects form the heart of Cloudera Machine Learning. They hold all the code, configuration, and libraries needed to reproducibly run analyses. Each project is independent, ensuring users can work freely without interfering with one another or breaking existing workloads."`

Users can create a blank project, use existing templates or source from git repository.

### Create CML Project from git source

1. Setup SSH for remote Github by following the steps from [here](https://docs.cloudera.com/machine-learning/cloud/security/topics/ml-adding-ssh-key-to-github.html).
2. Create a CML project. Follow steps from [documentation](https://docs.cloudera.com/machine-learning/cloud/projects/topics/ml-creating-a-project-with-runtimes-c.html).

<div class="alert alert-block alert-info">
<b>Optional:</b> You can also create a blank project and pull data from existing git repository.
</div>

1. After creating blank project, start a session and navigate to 'Terminal Access'<br>
2. Initialise git<br>
`git init`<br>
3. Add remote origin to your git repo<br>
`git remote add origin <REPO_URL>`<br>
4. Pull git repo from remote<br>
`git pull`<br>
5. Switch to existing branch<br>
`git switch <BRANCH_NAME>`<br>
6. \[Optional\] Create new branch<br>
`git checkout -b <BRANCH_NAME>`<br>

## Data Science stage

Data exploration, Feature Engineering, Baseline model, Model Training & Model evaluation form the key phases of Data Science stage. Data Scientists often spend time defining the problem and analysing the data before starting model building.

Follow the below documents to go through each phase:

[0. Setup](notebooks/Data_Science_Starter.ipynb)<br>
[1. Baseline Model](notebooks/Baseline_Model.ipynb)
