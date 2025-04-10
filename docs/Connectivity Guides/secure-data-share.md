---
title: "How to setup Secure Data Share"
slug: "secure-data-share"
excerpt: "Learn how to use secure data share feature of Snowflake to share data with Houseware"
hidden: false
metadata: 
  image: []
  robots: "index"
createdAt: "Mon Aug 28 2023 11:02:52 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 08 2023 06:14:43 GMT+0000 (Coordinated Universal Time)"
---
# Introduction

Snowflake's Secure Data Share feature allows you to share databases, schemas, tables, and views with Houseware without creating additional copies of the data, that too, in real-time.

More simply put, think of the Secure Data Share feature as a magical photo album, and you want to share some of these pictures with your friends without giving away the originals or making physical copies. Your warehouse is this magical album. The photos you want to share are specific data tables, schemas, databases, etc., to which you want access. 

Through Secure Data Share, Houseware will be able to look at, analyze, etc., the data, but it will never physically possess any of it.

# Benefits

Here is how using Secure Data Share to share data with Houseware will benefit you:

1. **Zero-copy cloning:** Snowflake allows for the instantaneous cloning of databases without duplicating the underlying data. This is a significant benefit in terms of both speed and cost. No extra storage layer is needed either for the provider or consumer for data; hence no extra cost, and data is always fresh.
2. **Real-time sharing**: As stated above, updates in the data provider's dataset are immediately available to the data consumer without any delay or additional steps.
3. **Granular Control**: Snowflake provides detailed control over what can be shared, down to specific columns in a table.
4. **Compute and Storage Separation**: Snowflake's separation of storage and compute ensures that sharing data doesn't impact the performance of the primary tasks of the data provider.
5. **No Additional Cost:** Just like how it doesn't cost you any extra to let another friend peek into your magical album, Snowflake doesn't charge extra for the data that's being shared. You're not creating new copies; you're just allowing access.

***

# Step-By-Step Guide

> 🚧 **Important Note:** The person setting up secure data share needs to have `ACCOUNTADMIN` privileges to create a new share.

## Step 1: Create a new share

Create a new share and give it a name. Follow the code snippet below to create a [new share](https://docs.snowflake.com/en/user-guide/data-sharing-gs). Use the database where the `allevents` table for Houseware is transformed and stored, as mentioned in the [setup doc](https://docs.houseware.io/docs/how-to-setup-houseware#step-2-create-a-separate-snowflake-db).

```sql
--need to go to ACCOUNTADMIN
set share_name = 'houseware_analytics_db_share';
CREATE SHARE identifier($share_name);

use database identifier($db_name);
use schema identifier($schema_name);
```

## Step 2: Grant Permissions

Once the share is created, grant usage privileges for the [database and schema](https://docs.houseware.io/docs/how-to-setup-houseware#step-2-create-a-separate-snowflake-db) created for Houseware where the `allevents` schema is stored. Secure Data Share is always **read-only access**. Hence share read-only access with Houseware as reflected in the code snippet shared below. 

Grant select privilege on the `allevents` table. You can do that by following the code snippet given below.

```sql
GRANT USAGE ON DATABASE identifier($db_name) TO SHARE identifier($share_name);
GRANT USAGE ON SCHEMA identifier($schema_name) TO SHARE identifier($share_name);
GRANT SELECT ON TABLE "ALLEVENTS" TO SHARE identifier($share_name);

DESC SHARE identifier($share_name);--optional


```

You can verify the same using the`DESC SHARE identifier($share_name);` but it is optional

## Step 3: Share it with Houseware

Grant Houseware's Snowflake account access to this share by adding the Houseware's account identifier. depending on your Snowflake region. Please confirm with Houseware support first.

> 🚧 **Note**: Both the provider and consumer accounts of the Secure Data Share need to be on the same cloud infrastructure and in the same region. The account locator mentioned below is only valid for Houseware's account in India region.

Here is the code snippet to grant access to Houseware's Snowflake.

```sql
--Direct data sharing is only allowed within the same region. 
ALTER SHARE identifier($share_name) ADD ACCOUNTS=XG59586;
```

## Step 4: Log in to Houseware and choose Snowflake Secure Data Share

You will see the page below on logging in for the first time (before your instance setting up). Choose the "Use Snowflake Secure Data Sharing" option here.

![First landing page, Click on Use Snowflake Secure Data Sharing](https://files.readme.io/95fb03b-secure_data_share.png)

*First landing page, Click on Use Snowflake Secure Data Sharing*


## Step 5: Provide the details

- Once you click on the Snowflake secure data share option, you will be redirected to the page shown below. The script given on the top of the page is the same as attached in the steps above in this document.

![Snowflake Secure Data Share page](https://files.readme.io/bceac8e-Screenshot_2023-09-07_at_7.16.28_PM.png)

*Snowflake Secure Data Share page*


To find your Snowflake organization and Account name, refer to this Snowflake documentation: [Admin account identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier#finding-the-organization-and-account-name-for-an-account)

- After filling in the correct information, just click on the **Connect** button. 

And :tada: through Snowflake Secure Data Share, your event data is now connected to your Houseware application!

Before events start flowing to your Houseware instance, the application will have to auto-run jobs to compute the metadata, as mentioned in the [Houseware setup guide](https://docs.houseware.io/docs/how-to-setup-houseware#step-3-transform-events-to-a-requisite-schema). These metadata tables are important to power your visualization creation process on Houseware.

> 👀 **Note**: Time taken to generate the metadata tables is contingent on your event volume. It usually ranges between a few minutes to couple of hours at max.

As soon as the first run completes and the initial requisite set of metadata tables is generated, your Houseware application will be live with all your event data! :zap:
