# Stream Analytics

Nowadays we need to deal with streaming data. Streaming data processing becomes a very important issue for big data:
* We need to ingest a lot of streaming data into big data platforms for later analytics. If you look at big data databases or data lakes, you see that streaming data ingestion is an important issue, such as [Hudi Delta Streamer](https://hudi.apache.org/docs/hoodie_deltastreamer/), [Druid Kafka Ingestion](https://druid.apache.org/docs/latest/development/extensions-core/kafka-ingestion.html)
* We need to analyze streaming data on the fly - analytics of big data in motion. Examples are to analyze IoT data, real time logs, and customer's ecommerce transactions

Although streaming analytics has had long history, dealing with big streaming data is challenging, especially when analytics must be done in sub-seconds for million requests.

## Key concepts

Key concepts in streaming analytics would be:

* Data connectors: how can we obtain streaming data? will we use connectors/libraries via standard protocols like [MQTT](https://mqtt.org/) and [AMQP](https://www.amqp.org/about/what)? Or will we use powerful advanced, sometimes all-inclusive, message brokers/pubsub systems, like Apache Kafka,  Apache Pulsar, or [Amazon Kinesis](https://aws.amazon.com/kinesis/).
* Windows analytics: streaming analytics often is based on a window of data. A window can be defined by length, time or other ways. Furthermore, data can selected through keys. Which types of windows are suitable? How to define them? If we have a window of data, what kind of analytics we can apply for a window? It is very often based on specific requirements and many experiments.
* Which engines can we use for executing stream analytics? How do such engines work with existing distributed computing resources to enable fast, reliable stream analytics?
* How to deal with message delay? faults of processing components? How to ensure that we dont reprocess of messages twice?


## Some paths for study

* Path 1: if you don’t have a preference and need challenges, you can choose Apache Flink Stream API (e.g., with  RabbitMQ/Kafka connectors)
  - See the [Base Transceiver Station stream analytics example](https://github.com/rdsea/bigdataplatforms/tutorials/streamingwithflink)

* Path 2: many of you have worked with Kafka: you can select [Kafka Streams DSL](https://kafka.apache.org/20/documentation/streams/developer-guide/dsl-api.html), [Kafka SQL](https://www.confluent.io/product/ksql/) (everything can be  done with Kafka)

* Path 3: for those of you who are working with [Apache Spark Structured Stream](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html) (and Python is the main programming language)
  - See [A basic Spark Stream example](https://github.com/rdsea/bigdataplatforms/tutorials/spark-streaming)

* Path 4: for those who deal with MQTT brokers: you can use [Apache Storm ](https://storm.apache.org/)  Spout and Bolt API or Stream API

## Understanding data from messaging systems 

Large-scale messaging systems for big data are complex. There are many such systems that one should be familiar with in order to integrate streaming analytics with such messaging systems:

* Systems supporting MQTT: [VerneMQ](https://vernemq.com/), [Mosquitto](https://mosquitto.org/), [EMQ](https://www.emqx.io/), [RabbitMQ](https://www.rabbitmq.com/)
* NATS: [NATS](https://nats.io/)
* Systems support AMQP: [RabbitMQ](https://www.rabbitmq.com/) 
* No protocol standard but widely used systems: [Apache Kafka](https://kafka.apache.org/), [Apache Pulsar](https://pulsar.apache.org/) 