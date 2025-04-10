---
title: "How to Setup Houseware (COPY)"
slug: "how-to-setup-houseware-copy"
excerpt: "This is a step-by-step technical guide for connecting your product events data with Houseware"
hidden: true
createdAt: "Fri Feb 16 2024 15:36:22 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Feb 16 2024 15:36:22 GMT+0000 (Coordinated Universal Time)"
---
# Overview

This guide describes the process of connecting your product events data with Houseware. This connection is required to ensure all your events and user data with all its properties is available to you on your custom Houseware instance to start analyzing. The time to complete the connection with Houseware is contingent upon your current product event collection and storing setup.

The entire setup is divided into two parts:

## Part I: 🛠️ Setting up events to connect with Houseware

Part I helps you transform your raw events data in the required schema, store it in a new database, and share access to the new DB with the Houseware application. Details about this part are covered in the guide below.

> 👀 **Note**: If you are opting for the [Secure Data Share](https://docs.houseware.io/docs/secure-data-share) option to connect your data with Houseware, then **PART II is not relevant for you**.

## Part II: 🎊 Going live with your Houseware instance

Part II will help you connect Houseware with the transformed event data created and stored in Part I above and to a new Snowflake warehouse to run Houseware queries on. Detailed scripts to set up the warehouse, and grant necessary permissions to the Houseware application are given in a separate doc here: [How to Connect Snowflake to Houseware](https://docs.houseware.io/docs/how-to-connect-to-snowflake#step-1-log-in-to-houseware-and-choose-snowflake-as-your-cdw)

> 🚧 **Important Info**: Both Part I and Part II are sequential. Hence, you will first have to complete Part I before moving on to Part II or to Secure Data Share setup to successfully setup your Houseware instance.

## How will this guide help

The primary intent of this guide is to lay out the entire process, step by step, for your team so that we are aware of all requirements and can preempt any bottlenecks.

The exact code snippets will help your IT and data engineering team configure the setup. For any further queries, doubts, or questions that are not covered here, our Houseware team will be available to support you!

***

# Step-by-Step Guide

Follow the steps listed below to prepare your raw events data in the schema compatible with the Houseware application.

## Step 1: Finalize the events to connect with Houseware

Based on the product analytics use cases you want to enable on Houseware, identify the list of events that you will need to drive them. 

This step will ensure that you start connecting with the most important events for you and your team.

## Step 2: Create a separate Snowflake DB

A new database will be needed to store your transformed events data in the required schema described in detail in the next step.

Here is a code snippet that will help you create a new database:

```sql
-- creating variables for database, schema
set db_name='HOUSEWARE_ANALYTICS_DB';
set schema_name='PRODUCT_ANALYTICS';

create database if not exists identifier($db_name);
use database identifier($db_name);
create schema if not exists identifier($schema_name);
```

### Here is how a new DB will help:

- A new database (DB) will be cleaner and easier for your team to give read-write or only read access in case of Secure Data Share to the Houseware application.
- It will also help in the separation of concerns and troubleshooting.

## Step 3: Transform events to a requisite schema

To make all events, users, and their properties available on your Houseware instance to analyze and visualize, convert your raw event data into the schema given below and name it -`allevents`.

[block:parameters]
{
  "data": {
    "h-0": "Column Name",
    "h-1": "Data type",
    "h-2": "Details",
    "0-0": "\\*event_id",
    "0-1": "String (UUID)",
    "0-2": "Unique identifier for the event",
    "1-0": "\\*device_id",
    "1-1": "String (UUID)",
    "1-2": "Identifier for the device from which the event was captured. Can be a cookie/ anonymous user id",
    "2-0": "\\*user_id",
    "2-1": "String (UUID)",
    "2-2": "Unique identifier of the user, generated after the user has logged in. Null values for this field indicate that the user has not logged in",
    "3-0": "\\*device_ts",
    "3-1": "Timestamp in UTC",
    "3-2": "The time when the event was captured on the device. Used for ordering events",
    "4-0": "\\*server_ts",
    "4-1": "Timestamp in UTC",
    "4-2": "The time when the event was received at the server. Used for restricting events to certain periods of interest",
    "5-0": "\\*event_name",
    "5-1": "String",
    "5-2": "Name of the event",
    "6-0": "\\*properties",
    "6-1": "JSON",
    "6-2": "Free-flowing properties associated with the event. Try and stick to event-specific properties only here. Any common event properties or user properties can be kept as a column of their own (as shown below as event_dimension1).  \nUseful for filters or breakdown.",
    "7-0": "\\<event_dimension1>",
    "7-1": "String",
    "7-2": "Event dimension that is applicable for all the events. Useful for filters or breakdown.",
    "8-0": "\\<event_dimension2>",
    "8-1": "String",
    "8-2": "Event dimension that is applicable for all the events. Useful for filters or breakdown. ",
    "9-0": "\\<user_dimension1>",
    "9-1": "String",
    "9-2": "User dimension that is applicable for all the events. Useful for filters or breakdown.",
    "10-0": "\\<user_dimension2>",
    "10-1": "String",
    "10-2": "User dimension that is applicable for all the events. Useful for filters or breakdown."
  },
  "cols": 3,
  "rows": 11,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


> 👀 **Note **: All properties common across all events should be added to the `event_dimension` columns. This helps us leverage Snowflake's columnar storage and run your analysis more efficiently. All properties specific to an event should be part of the properties JSON.

</br>

> 🚧 Important:
> 
> 1. **The table should be named as** `allevents` **only.**
> 2. All columns marked with an `*` are necessary and not optional to include in the table.
> 3. The column names should be exactly the same as given in the schema above. However, event dimension columns like `event_dimension1` and user dimension columns like `user_dimension_1` can be named as per your choice.
> 4. The properties column in the schema should be a JSON with [Object data type](https://docs.snowflake.com/en/sql-reference/data-types-semistructured#object). The data type for the `key` will be a string, and `value` can be a boolean, integer, float, date, or string.** Nested JSON object/array are not supported.**
> 5. The time columns `device_ts` and `server_ts` in the above schema should be in UTC in the following format: `YYYY-MM-DD HH24:MI:SS`, for example `2023-08-06 15:04:06`

This transformed event schema must be stored in the new database created in Step 2 and named`allevents`. 

:star:**Optimized Queries**: To ensure efficient queries run on top of the `allevents` table make sure to **create a cluster key** using the columns `server_ts` and `event_name`. Follow the code snippet given below to add the clustering key to the`allevents` table.

```sql
ALTER TABLE HOUSEWARE_ANALYTICS_DB.PRODUCT_ANALYTICS.ALLEVENTS CLUSTER BY
(SERVER_TS, EVENT_NAME)
```

**To know more about clustering and micro-partitions in Snowflake, read here** :point_right: [What is clustering](https://docs.snowflake.com/en/user-guide/tables-clustering-micropartitions#what-is-data-clustering). 

Once you are done transforming your raw events data in the schema mentioned above, write it to the new database as created in STEP 2.

## Step 4: Share user attributes for cohorts

Houseware needs the latest snapshot of user attributes to create cohorts based on the latest activity of the user.

You can add this as a view from your existing user table or a separate table in the schema mentioned above. Note: The houseware application will need read access to this table.

| Column Name       | Data type                 | Details                                                                  |
| :---------------- | :------------------------ | :----------------------------------------------------------------------- |
| \*user_id         | String (UUID)             | Unique identifier of the user, same as the `user_id` in the events table |
| \<user_property1> | String / Number / Boolean | The latest value of user property 1 corresponding to the user_id         |
| \<user_property2> | String / Number / Boolean | The latest value of user property 2 corresponding to the user_id         |

> 🚧 Important:
> 
> 1. **The table should be named as** `users` **only.**
> 2. All columns marked with an `*` are necessary and not optional to include in the table.
> 3. The column names should be exactly the same as given in the schema above. However, user property columns like `user_property1` and `user_property2` can be named as per your choice.
> 4. User property columns in this table should be **same as the user dimensions** transformed into the events table in Step3.
> 5. This table should be refreshed frequently depending on your analytics workflows, how frequently user properties get updated in your systems so that Houseware application stays up-to-date.

## Step 5 (Optional): For creating a 'first-time users' filter

Sometimes, you might want to filter event trends, funnels, etc., only for the users who performed it for the first time on the product. To create this ready-made filter on your instance, here are the following requirements.

Depending on your organization's analysis timeline, Houseware may only have access to the last 1-2 months of data in the `allevents` table shared above. However, a chunk of your product users can be as old as your product, for example: a couple of years. Hence to make sure that first-time users are picked correctly, we need a mapping of when a user did a particular event for the first time. This can be shared as a table called `first_time_event_mapping` in the Houseware schema:

| Column Name              | Data type     | Details                                                                                                                                                          |
| :----------------------- | :------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \*event_name             | String        | Name of the event. This is the same identifier as `event_name` in the `allevents` table.                                                                         |
| \*device_id              | String (UUID) | Identifier for the device from which the event was captured. This is the same identifier as `device_ts` in the `allevents` table.                                |
| \*first_time_event_id    | String (UUID) | Unique identifier for the event done for the first time. This is the same identifier as `event_id` in the `allevents` table.                                     |
| \*first_time_server_date | Date          | The date when this event was received at the server. Used for efficient queries to this table. This is equivalent to `DATE(server_ts)` in the `allevents` table. |

:star:**Optimized Queries**: To ensure efficient queries run on top of the `first_time_event_mapping` table make sure to **create a cluster key** using the columns `event_name` and `first_time_server_date`. Follow the code snippet given below to add the clustering key to the`first_time_event_mapping` table.

```sql
ALTER TABLE HOUSEWARE_ANALYTICS_DB.PRODUCT_ANALYTICS.FIRST_TIME_EVENT_MAPPING CLUSTER BY
(EVENT_NAME, FIRST_TIME_SERVER_DATE)
```

> 👀 **Note **:  **Houseware's application will need read-and-write access to the new DB** where this transformed event schema is stored. The Houseware application periodically generates and writes metadata to this DB to power your Houseware instance. 
> 
> However, if you are using the secure data share model, no write access will be needed. Secure data share only allows read access. The metdata tables generated will be written to Houseware's Snowflake account only.

As the Note above mentions, your transformed event schema is also used to auto-generate additional metadata tables. 

They are primarily used to generate event and user details like their names, properties, timestamps, and other information to pre-fill this information on your Houseware instance. Data from these tables eases your visualization creation process, as specific event names, properties, etc., will automatically show up in the breakdown and [filter drop-down menus](https://docs.houseware.io/docs/funnels#funnel-filters).  

> 👀 **Note :** The metadata tables will also be stored in the same DB as the transformed events schema and accessible to you. If you have opted for the **Secure Data Share** option, these metadata tables will be stored in Houseware's own Snowflake.

Great start! :tada: You are already done with Part I of the setup process. To connect your transformed event data with Houseware and complete your setup, head over to the Part II guide here : :point_right: [How to Connect Snowflake to Houseware](https://docs.houseware.io/docs/how-to-connect-to-snowflake#step-1-log-in-to-houseware-and-choose-snowflake-as-your-cdw)

If you are opting for the Secure Data Share method, then head over to its detailed setup guide here: :point_right: [How to setup Secure Data Share with Houseware](https://docs.houseware.io/docs/secure-data-share)
