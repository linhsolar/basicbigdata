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

## Metadata

For a big data platform, each tenant will have many databases or datasets. Each database or dataset has different data concerns and other important information characterizing the database/dataset. Therefore, we have to design metadata for databases/datasets.

To give one example, let us assume that a tenant has created a group of datasets "BigDataPlatform". Inside the group, the tenant can have different datasets and different metadata about the dataset, such as  data quality, schema, etc.

A big data platform would provide features for creating metadata. For example, in [Data Catalog from Google Cloud](https://cloud.google.com/data-catalog), your create template for certain types of metadata. Examples are Data Governance, Geo Context and Data Quality. Metadata can be associated with the whole dataset or individual data columns. For example, in Data Governance, you see different information, like Owner,Classification,Personally identifiable information, Encrypted, ... Geo Context with Region, Cointry, and Quality of Data with  Completeness, quality, issues, etc.

In general, we should provide various features for the customers to manage metadata about their data in our big data platforms. There are many other systems for metadata, such as [Linkedin DataHub](https://github.com/linkedin/datahub) or [Apache Atlas](https://atlas.apache.org/#/)
