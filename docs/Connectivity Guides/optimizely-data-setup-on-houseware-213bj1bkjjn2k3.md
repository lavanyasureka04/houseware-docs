---
title: "[Link-only Access] Optimizely Data Setup on Houseware"
slug: "optimizely-data-setup-on-houseware-213bj1bkjjn2k3"
excerpt: "An overview of how Optimizely's web experimentation data is setup on Houseware"
hidden: true
createdAt: "Thu Jun 13 2024 01:14:44 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Jun 13 2024 08:20:09 GMT+0000 (Coordinated Universal Time)"
---
This doc details how Optimizely's data is configured and processed within Houseware.

Here's an overview of what we'll cover:

1. Raw tables being used from the Optimizely data
2. Data tables maintained by Houseware for running the Houseware application
3. How this data is maintained by Houseware

## Overview

Houseware has access to specific tables containing Optimizely's web experimentation data, which have been mapped to the [event schema required by the Houseware application](https://docs.houseware.io/docs/how-to-setup-houseware#step-3-transform-events-to-a-requisite-schema).

Houseware accesses the following tables, stored on Optimizely's BigQuery:

| Table name    | Columns (relevant for Houseware schema)                                       |
| :------------ | :---------------------------------------------------------------------------- |
| `conversions` | `event_name, event_type, tags, attributes, timestamp, visitor_id, account_id` |
| `decisions`   | `attributes, timestamp, visitor_id, experiment_id, variation_id, account_id`  |

<br />

## Data Transformation

As part of Houseware's data onboarding, the data from Optimizely's tables has been transformed into Houseware's native event schema. Some key points to note from this process are as follows:

### Step-1: Extracting event names through `event_name` and `event_type` columns

- Houseware maps event names based on the `event_name` field in the provided tables
- For `decisions` table, the `event_name` is derived by prefixing `experiment_id` column with the phrase `decision_exp`
- In cases where `event_name` is not available, the `event_type` field from `conversions` table is used as a fallback (eg.: Houseware event `client_activation`)
- The `decisions` table does not contain the `event_type` column. To maintain consistency with the `conversions` table, an `event_type` column has been created and hard-coded with the value `decision`

### Step-2: Extracting event/user properties through `tags` and `attributes`

- `tag` and `attribute` columns from the source tables contain data that can be used as event or user properties on Houseware
- These columns have been transformed into the required schema for Houseware event/user properties

### Step-3: Mapping data to Houseware Schema

**`ALLEVENTS` table:**

- After the above transformation steps, the data from the 2 tables is combined and materialized as an `allevents` table, stored on Houseware's BigQuery
  > 📘 The schema for the `allevents` table is available on Houseware docs [here](https://docs.houseware.io/docs/how-to-setup-houseware#step-3-transform-events-to-a-requisite-schema).

<br />

## Data Maintenance

Maintaining the integrity and freshness of your data is critical for effective analytics. Houseware ensures that Optimizely's data remains up-to-date and accurate through a systematic approach to data maintenance.

### Data Refresh:

- Data refreshes on Houseware every 6 hours.
  > 👍 Real-time data streaming on Houseware
  > 
  > - Houseware supports real-time data streaming, highly configurable to the requirements of our customers
  > - This process is efficient on Houseware because:
  >   - All data update is incremental. Houseware always only processes new data since the last data update, which saves time and cost during real-time data update

<br />

### Metadata Tables:

Besides the `allevents` table, Houseware also maintains some metadata tables to ensure a great user experience on the Houseware app. These are:

- **Dimensions:** Used for displaying user properties and common event properties on the Houseware application
- **Users:** Used for calculating user cohorts in real-time
- **Event names:** Used for displaying event names and event-specific properties on the Houseware application
- **First-time Events:** Used for supporting the feature `first-time filter` (a feature that counts events only for users who triggered them for the first time)
- **Metadata:** Used for maintaining event time-range data (incremental state metadata)

<br />

That's it! This is how Optimizely data stays up-to-date and snappy on the Houseware application. In case of any questions, reach out to us on Slack or at [sidhant@houseware.io](mailto:sidhant@houseware.io), we'd be happy to help!
