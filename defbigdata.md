# A Bird View on Big Data

## Big Data

We work with different types of data daily. Data can be facts, responses, events, measurements, logs, to name just a few. [Big Data](https://en.wikipedia.org/wiki/Big_data) should be understood that principles, models, techniques and technologies for dealing with *"V data"*. The key issues are to deal with voluminous data that comes to a system, with different speeds (velocities), from  diverse sources. Such big data requires different storage and processing capabilities. From the application side, such data is a must for modern businesses and operations, as various types of insights about environments, people, businesses, activities, etc., can be analyzed through in adhoc, on-demand, scheduled analytics in batch or streaming manners in 24/7 operations. In fact, the success of the current phenomemon of machine learning (ML)/artificial intelligence (AI) is heavily based on  the available of big data platforms and techniques. Furthermore, advanced [data science](https://en.wikipedia.org/wiki/Data_science) and its success would be not possible without big data fundamentals.  

In the literature, big data is often characterized by:

* Volume: indicates the size (big size, large-data set, massive of small data)
* Variety: indicates the complexity (formats, types of data)
* Velocity: indicates the speed (generating speed, data movement speed, processing speed)
* Veracity: indicates the diverse quality (bias, accuracy, etc.)
* Valence: indicates implicit and explicit relationships among different type of data

>You can read further, basic discussions about [big data characteristics](https://www.datasciencecentral.com/profiles/blogs/how-many-v-s-in-big-data-the-characteristics-that-define-big-data) and [what is big data](https://www.oracle.com/big-data/guide/what-is-big-data.html)

In our study, we should not misunderstand that big data means that a *data element* must be *big*. A dataset is constructed from data elements. A data element can be very small, for example a record of environmental sensing, or it can be large, e.g., a video.
>An example of a JSON-based data record for [Base Transceiver Station monitoring](https://version.aalto.fi/gitlab/bigdataplatforms/cs-e4640/-/tree/master/data/bts/README.md) is:
```json
{
  "station_id":"1160629000",
  "datapoint_id":122,
  "alarm_id":310,
  "event_time":"2016-09-17T02:05:54.000Z",
  "isActive":false,
  "value":6,
  "valueThreshold":10
}
```
>if you represent them in the *binary format*, the size is even smaller. However, what if you have a million of such records every day ingested into your system and you have to manage them for a long time (because of yearly analytics)? You will have *big data*! All together small data elements can create the phenomenon of big data. For example, [the open data of 2018 Yellow Taxi Trips in NY taxi includes 112M records](https://data.cityofnewyork.us/Transportation/2018-Yellow-Taxi-Trip-Data/t29m-gskq) (*Note: 112M was based on the time we downloaded. The data has been updated but the number should not change a lot.*)

For some companies (like Twitter, Amazon, or Meta/Facebook), handling few GBs of data per day is nothing. For others, like SMEs or small research groups, it is a big deal due to the lack of knowhow and infrastructures. Hence the interpretation of "big data" should be flexible, based on the context.
> For example:  "5M sensors/monitoring points with ~1.4B events/day~  72GB/day" is big, if compared with ["an average daily download volume of 214 TiB" in Coperinus Open Access Data Hub](https://scihub.copernicus.eu/twiki/do/view/SciHubWebPortal/AnnualReport2019)

Given the "big data", you might wonder which sources create such data? How many data sources do we have to handle? All data sources will provide similar data and all the data belong to the same tenant or not? These questions are very important for studying big data analytics and platforms because:

* Even the number of data sources is large, if the data sources belong to the same owner/tenant, then, from the techniques and technologies perspective, these sources might follow similar way of data representations, data transfer protocols, or security and privacy constraints. Or last least, they might have many things in common w.r.t. infrastructures and data governance processes. Therefore, we might have simpler engineering requirements (*Note: "simpler" in the context of big data*).

* If the number of data sources is small but the data sources are from different owners, these might be specific requirements w.r.t tenant management, privacy, and security. Thus, we might need to have different solutions for different tenants.
* A small number of data sources producing a very big data volume might be very different from a very large number of data sources, each produce a reasonable amount of data. If you replace "the volume" by "the type of data", we will have similar challenges.

>When you deal with big data, you should identify clearly the above-mentioned questions.

### Why do we need to care about big data
We care about big data because of the values of data! The current [data economy](https://en.wikipedia.org/wiki/Data_economy) shows that if we have more data we could have more insights for to make our decisions better, thus bringing more business successes.  On the other hand, from the bottom-up view, we can think about the values of data within our business. If we have more data, we could understand our operations better. Thus, we can optimize our operations and save  costs.

One interesting observation is the the principle of [“The Unreasonable Effectiveness of Data”](http://static.googleusercontent.com/media/research.google.com/en//pubs/archive/35179.pdf) which shows that with more data, the same algorithm performs much better! Many of you also learn machine learning (ML) so you probably know this principle very well: more training data may help to increase the model accuracy. It is one of the reasons why for ML people want to collect and have more and more data for training.
>Alon Halevy, Peter Norvig, and Fernando Pereira. 2009. [The Unreasonable Effectiveness of Data](http://static.googleusercontent.com/media/research.google.com/en//pubs/archive/35179.pdf). IEEE Intelligent Systems 24, 2 (March 2009).


### Big Data Platforms
There are many forms of platforms. Many of us are familiar with computing platforms like Google and Amazon Cloud Services. When talking about platforms, we should keep in mind that the platforms are not just for the end-user to use,  but it is also the developer to develop a new things atop such platforms. Here is an excellent definition of platforms for our study:

*“A platform is a business based on enabling value-creating interactions between external producers and consumers. The platform provides an open, participative infrastructure for these interactions and sets governance conditions for them. The platform’s overarching purpose: to consummate matches among users and facilitate the exchange of goods, services, or social currency, thereby enabling value creation for all participation”*

>Source:  *Geoffrey G. Parker, Van Alstyne, Marshall W. Van Alstyne , Sangeet Paul Choudary, [Platform Revolution: How Networked Markets Are Transforming the Economy - and How to Make Them Work for You](https://www.amazon.com/Platform-Revolution-Networked-Markets-Transforming/dp/0393249131), March 28, 2016*

So what are the key aspects from **platforms** that we should pay attention? We interpret a few key terms from the above-mentioned definition in the context of big data platforms:

  * *"interactions"*: there are many types of interactions that we should support. For example, in big data platforms, we must enable interactions between big data producers and big data consumers. Similarly, we must enable various interactions for management, analysis, and optimization.
  * *"open, participative infrastructures"*: the platform must allow us to integrate and develop new services for new stakeholders. In terms of big data platforms, we see that the big data platforms will have on-demand computing platforms for data-centric products,  analytics service platforms and data management platforms
  * *"governance conditions"*: we must define governance procedures, policies and constraints to allow smooth operations of the big data platforms. This can involve security and privacy, data regulation, or tenant management.
  * *"facilitate the exchange of"*: In big data platforms, we facilitat the exchange of "big data" and "data products" centered around data assets. We see that such exchanges require not just a database or data marketplaces (even they are very big)

To understand core principles of platforms will help us to design our platforms to be scalable, open and reliable for multiple data sources, customers and services.
