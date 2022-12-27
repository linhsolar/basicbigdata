# Understanding the source of data

If you look around, you see a lot of open data sources. Many of them are quite big.
>Check [some of the sources we use for study](https://version.aalto.fi/gitlab/bigdataplatforms/cs-e4640/-/blob/master/data/README.md)

So if you are going to analyze big data, which data sources and data management problems will you have to deal with? Concretely, you might ask which databases and data systems that you will send your analytics requests via your programs or existing tools.

In the big data, there are many types of data sources, offered through different data storage, databases, messaging systems, and other forms of big data infrastructures. Some of them might not be designed specifically for big data but they have to be re-architected/adapted for big data. Some are specifically designed for big data.

### Data at rest vs data in motion 

Data sources can provide [data at rest](https://en.wikipedia.org/wiki/Data_at_rest) or [data in motion (or data in transit)](https://en.wikipedia.org/wiki/Data_in_transit) for analytics. Data at rest means that the data is stored in a physical place and assumed to be in the place for various tasks as long as the data is needed. Data at rest is usually delivered via databases, data storages and file systems. Data in motion means that the data is moving from one place to another place, thus the data will stay just a while for the analytics. This temporal aspect can mean a second, an hour or a day. Data in motion is usually delivered via messaging systems. 

Given the data at rest and data in motion, we will have to use different techniques to analyze them. However, often we would like to use common techniques as much as possible for both types of data. Therefore, you may see that we use tables to capture both data at rest and data in motion. Furthermore, for real-world applications, both types of data are usually handled together. Thus, there are various architectures and frameworks supporting both types of data. 

## Polyplot big data sources

When dealing with big data, often we need to deal with different data sources and different types of data. Furthermore, in order to manage a big data platform, we also use different databases. Therefore, [polyplot persistence](https://en.wikipedia.org/wiki/Polyglot_persistence) is what we need to support in big data platforms.


### For data at rest 

Examples of databases/storage systems that we will find suitable for big data analytics:
* [Cassandra](https://cassandra.apache.org/)
* [Apache Druid](https://druid.apache.org/)
* [Hadoop File System](https://hadoop.apache.org/)
* [Apache Hudi](https://hudi.apache.org/)
* [HBase](https://hbase.apache.org/)
* [MongoDB](https://www.mongodb.com/)

any many more!

### For data in motion 

Usually the data is deliverd via messaging systems, such as 
* Systems supporting MQTT: [VerneMQ](https://vernemq.com/), [Mosquitto](https://mosquitto.org/), [EMQ](https://www.emqx.io/), [RabbitMQ](https://www.rabbitmq.com/)
* NATS: [NATS](https://nats.io/)
* Systems support AMQP: [RabbitMQ](https://www.rabbitmq.com/) 
* No protocol standard but widely used systems: [Apache Kafka](https://kafka.apache.org/), [Apache Pulsar](https://pulsar.apache.org/) 

## Data file formats and storage 

### Data file formats

It is easy to think that we mostly deal with CSV data files, due to their abundant availability for data analytics and machine learning. In fact, there are many data file formats employed in big data analytics and platforms. Some of these types of formats are designed for big data requirements.  For example, in many applications in businesses, marketing, manufacturing, and IoT, we may see a lot of data stored in the following formats:

- [Apache Parquet](https://parquet.apache.org/): columnar file format for analytic data.
- [Apache ORC](https://orc.apache.org/): columnar file format.

and of course CSV, JSON, [images](https://image-net.org/), text files. In [big data for remote sensing](https://www.myecole.it/biblio/wp-content/uploads/2020/11/3DK2DS_Big_Data_Remote_Sensing.pdf), we can see the popularity of [LAS file format](https://www.asprs.org/divisions-committees/lidar-division/laser-las-file-format-exchange-activities) or [SAR image files](https://earth.esa.int/eogateway/instruments/sar-ers). In scientific computing, we may see big data sources in [HDF](https://www.hdfgroup.org/). 

Which ones should we use is also dependent on many factors where big data is applied. Another important aspect is that different big data storage and database systems might support different formats in order to optimize their analytics performance and management for different use cases. Naturally, due to the diversity of file formats and the complexity of data sources and processing frameworks, one may be some techniques to support data .[Apache Arrow](https://arrow.apache.org/) is a framework that support a language-independent format which can be used as an interoperability solution for analytics of data in different file formats.


### Column family based Storage in Big Data

In big data, many systems support column family based/wide-column storage. What is it and why?

A common way to organize data in storage and database is to use the table view: we have a row to keep data belong to the same record. And we have multiple rows. It is very good for situations when we need to update data in a record or access a record as a whole, e.g. update the job status of a worker or provide the detail of a worker profile, and every row/record has  the same fields.

With big data, in many use cases, we have to scan and aggregate data from millions of rows but with a few columns (and we do not the update of existing data often). In such cases, storing data based on the columns will help to save space as well as to enable big data analytics. For example, if we want to count how many trips the NY Taxi services have conducted, we can scan millions records but a single column.

Furthermore, other aspects of storage in big data are:

* Different rows can have different schemas (the columns are different).
* A cell stores a value with versioning data, e.g., using timestamp
* Related columns organized into a family are usually stored and sharded together

Therefore, column family based storage is popular in big data. It is also called [wide-column store](https://en.wikipedia.org/wiki/Wide-column_store). 


Many big data systems implement the column family data model, such as:
  * [ Apache HBase](https://www.slideshare.net/larsgeorge/hbase-in-practice)
  * [Apache Accumulo](https://accumulo.apache.org/docs/2.x/getting-started/table_design)
  * [Apache Cassandra](https://cassandra.apache.org/_/index.html)


## Metadata and Data Resources Management

For a big data platform, each tenant will have many databases or datasets. Each database or dataset has different data concerns and other important information characterizing the database/dataset. Therefore, we have to design metadata for databases/datasets.

To give one example, let us assume that a tenant has created a group of datasets "BigDataPlatform". Inside the group, the tenant can have different datasets and different metadata about the dataset, such as  data quality, schema, etc.

A big data platform would provide features for creating metadata. For example, in [Data Catalog from Google Cloud](https://cloud.google.com/data-catalog), your create template for certain types of metadata. Examples are "Data Governance", "Geo Context" and "Data Quality". Metadata can be associated with the whole dataset or individual data columns. For example, in "Data Governance", you see different information, like "Owner", "Classification", "Personally identifiable information", and "Encrypted" or you see "Geo Context" with "Region" and "Country", and "Data Quality" with  "Completeness".

In general, we should provide various features for the customers to manage metadata about their data in our big data platforms. There are many other systems for metadata, such as [Linkedin DataHub](https://github.com/linkedin/datahub) or [Apache Atlas](https://atlas.apache.org/#/)

## How to choose big databases/storage?

So we say there are many different types of databases and storage for big data and we give some examples above. However, a tricky question is "*how do I select a suitable database/storage for my big data work, say to store my data?*". There is no answer for that question: one has to have a good understanding of existing database/storage technologies and to match these technologies with requirements (type of data, cost, performance, etc.). Some sources may be useful for you to check:
* [Choosing A Cloud DBMS: Architectures and Tradeoffs](http://vldb.org/pvldb/vol12/p2170-tan.pdf)
