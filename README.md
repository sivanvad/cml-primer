# CML Demo for Professional Services

## Introduction

Cloudera Machine Learning (CML) makes it easy to bring Data Scientists to the data platform and makes it easier to overcome the challenges they face on a day to day basis. To understand more about CML, please view this [tour](https://www.cloudera.com/users/cdp-tour-cml-intro.html).

### About this demo

In a typical working day of a data scientist or a machine learning engineer, tackling the business problems requires them going through various stages of machine learning lifecycle. CML plays an important role in simplifying many of the activities in this lifecycle. Depending on the type of user and their requirements, role of CML can vary while supporting complete lifecycle. This demo intends to cover the most common scenarios faced of typical CML user. Intention is to help the audience understand CML capabilities by documenting the journey of a CML user.

It is important to note that this demo does not cover all capabilities of CML. To know all about CML, please refer [documentation](https://docs.cloudera.com/machine-learning/cloud/product/topics/ml-product-overview.html).

## ML Lifecycle

Stages in ML Lifecycle can be categorised into 3 groups:
* Data Engineering
* Data Science
* Machine Learning Operations (MLOps)

<img src="./docs/ml_lifecycle_vanilla.png" width="750" height="300">

### Setting up CML Project (From Git)

---- Add steps from setup.txt ---

### Data Engineering

ML Project begins with defining the problem. Once a problem & goals have been defined, data scientists begin by collecting data from various sources. Cloudera Data Platform supports all data needs including ML projects. CML is integrated with other services in CDP and users can source data from there or access data directly from external sources. 

After identifying data required for the project, data engineers are involved to source data where required to build data pipelines. This is usually performed outside of CML using Cloudera Data Flow (NiFi) or Cloudera Data Engineering (Spark). However, many times it is hard to determine what data is required for this project before hand. Data Scientists have to perform data exploration and work with data teams to identify data that add value to project. This means CML users should have means to access data that is required after acquiring appropriate permissions. SDX plays an important role in enabling this seamless integration between different data services in CDP. With permissions in place, CML users can access data residing in other data services like Cloudera Data Warehouse without relying on data engineers.

**Data Access Patterns** <br>
---- Add notebook link here ----

## Data Science

TODO

### MLOps

TODO


```python

```
