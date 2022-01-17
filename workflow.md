# Workflows

## What is a workflow?
Workflows are a key model that we can use in many different purposes in big data analytics and big data platforms. Workflows are well-known and well-developed. In a big data platform, workflows can be used for

* Data Processing: data analytics, extraction, transformation, data transfers
* Machine learning: collecting data, orchestrating training experiments, implementing tasks in serving machine learning algorithms
* Automation in big data platforms: service deployment, elasticity, incident management
* Service integration with big data platforms: integration with customer service, communications of analytics

For example, [a security-related information and metrics from distributed customers](http://highscalability.com/blog/2015/9/3/how-agari-uses-airbnbs-airflow-as-a-smarter-cron.html) consists of multiple tasks, from data ingestion to notification to data analytics.



### Workflows, Tasks/Activities and Worker/Invoked Services

Before using workflows, we should note the terms

* Workflows:
 coordinates many tasks, tasks are not really “carried out” by workflows
workflow can be simple, like a pipeline of a sequence of tasks or complex with fork/loop

* Workflow Engine

* Tasks or Activities: task can be simple or complex (e.g., a task running an AI algorithm). Tasks are performed by software and humans triggers and sinks can be humans

* Invoked Applications: Task Workers

In many cases, we also use the term "data workflows": which means that the workflow is a set of activities dealing with data. We also call data pipelines.

>Big Data Pipeline: often we use big data pipeline to tell how different components are linked together to support big data. Atop of such components, many workflows can be executed. However, big data pipelines can also use to specify tasks (data pipelines).


## Key requirements for workflow frameworks in big data platforms

To be successful for different applications, workflows need rich connectors to various data sources. To be able to support different scenarios of big data, we need big data computation engines for running different workload: ML and (batch/stream) big data processing. Such engines and workflow tasks require highly dynamic, powerful underlying cloud infrastructures.

There are many frameworks for workflows. From the study we can focus on some common ones like:
* Apache Oozie: http://oozie.apache.org/
designed to work with Hadoop: orchestrating Hadoop jobs
it is important if you need to manage a lot of Hadoop/MapReduce jobs
Fluent Job API & XML-based workflows
* Serverless-based: Function-as-a-Service
e.g., Microsoft, Google, AWS serverless/function-as-a-service
* Apache Airflow: a generic workflow framework
* Candace:
* Argo: Workflows for managing machine learning pipelines
