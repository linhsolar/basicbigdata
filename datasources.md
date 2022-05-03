# Understanding the source of data

If you look around, you see a lot of open data sources. Many of them are quite big.
>Check [some of the sources we use for study](https://version.aalto.fi/gitlab/bigdataplatforms/cs-e4640/-/blob/master/data/README.md)

So if you are going to analyze big data, which data sources and data management problems will you have to deal with? Concretely, you might ask which databases and data systems that you will send your analytics requests via your programs or existing tools.

In the big data, there are many types of data sources, offered through different data storage, databases, and other forms of big data infrastructures. Some of them might not be designed specifically for big data but they have to be re-architected/adapted for big data. Some are specifically designed for big data.


## Polyplot big data sources
When dealing with big data, often we need to deal with different data sources and different types of data. Furthermore, in order to manage a big data platform, we also use different databases. Therefore, [polyplot persistence](https://en.wikipedia.org/wiki/Polyglot_persistence) is what we need to support in big data platforms.

Examples of databases/storage systems that we will find suitable for big data analytics:
* [Cassandra](https://cassandra.apache.org/)
* [Apache Druid](https://druid.apache.org/)
* [Hadoop File System](https://hadoop.apache.org/)
* [Apache Hudi](https://hudi.apache.org/)
* [HBase](https://hbase.apache.org/)
* [MongoDB](https://www.mongodb.com/)

any many more!

## Column family based Storage in Big Data
In big data, many systems support column family based/wide-column storage. What is it and why?

A common way to organize data in storage and database is to use the table view: we have a row to keep data belong to the same record. And we have multiple rows. It is very good for situations when we need to update data in a record or access a record as a whole, e.g. update the job status of a worker or provide the detail of a worker profile, and every row/record has  the same fields.

With big data, in many use cases, we have to scan and aggregate data from millions of rows but with a few columns (and we do not the update of existing data often). In such cases, storing data based on the columns will help to save space as well as to enable big data analytics. For example, if we want to count how many trips the NY Taxi services have conducted, we can scan millions records but a single column.

Furthermore, other aspects of storage in big data are:
* Different rows can have different schemas (the columns are different).
* A cell stores a value with versioning data, e.g., using timestamp
* Related columns organized into a family are usually stored and sharded together

Therefore, column family based storage is popular in big data. It is also called [wide-column store](https://en.wikipedia.org/wiki/Wide-column_store). Many big data systems implement the column family data model, such as:
  * [ Apache HBase](https://www.slideshare.net/larsgeorge/hbase-in-practice)
  * [Apache Accumulo](https://accumulo.apache.org/docs/2.x/getting-started/table_design)
  * [Apache Cassandra](https://cassandra.apache.org/_/index.html)


## Metadata

For a big data platform, each tenant will have many databases or datasets. Each database or dataset has different data concerns and other important information characterizing the database/dataset. Therefore, we have to design metadata for databases/datasets.

To give one example, let us assume that a tenant has created a group of datasets "BigDataPlatform". Inside the group, the tenant can have different datasets and different metadata about the dataset, such as  data quality, schema, etc.

A big data platform would provide features for creating metadata. For example, in [Data Catalog from Google Cloud](https://cloud.google.com/data-catalog), your create template for certain types of metadata. Examples are "Data Governance", "Geo Context" and "Data Quality". Metadata can be associated with the whole dataset or individual data columns. For example, in "Data Governance", you see different information, like "Owner", "Classification", "Personally identifiable information", and "Encrypted" or you see "Geo Context" with "Region" and "Country", and "Data Quality" with  "Completeness".

In general, we should provide various features for the customers to manage metadata about their data in our big data platforms. There are many other systems for metadata, such as [Linkedin DataHub](https://github.com/linkedin/datahub) or [Apache Atlas](https://atlas.apache.org/#/)

## How to choose big databases/storage?

So we say there are many different types of databases and storage for big data and we give some examples above. However, a tricky question is "*how do I select a suitable database/storage for my big data work, say to store my data?*". There is no answer for that question: one has to have a good understanding of existing database/storage technologies and to match these technologies with requirements (type of data, cost, performance, etc.). Some sources may be useful for you to check:
* [Choosing A Cloud DBMS: Architectures and Tradeoffs](http://vldb.org/pvldb/vol12/p2170-tan.pdf)
