---
title: "Best Practices to update ETL pipelines"
slug: "best-practices-to-update-etl-pipelines"
excerpt: "Learn the best practices for updating your event stream which ensures minimum downtime for users and easy update of data"
hidden: true
createdAt: "Thu Feb 01 2024 09:42:26 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Feb 01 2024 10:01:56 GMT+0000 (Coordinated Universal Time)"
---
## Introduction

This doc guides users through the best practices for modifying the `allevents` table in Snowflake while updating your ETL pipelines to minimize downtime and ensure seamless data visualization on the Houseware platform. This doc assumes you have context of the `allevents` table, if not, refer to [this doc](https://housewarehq.slack.com/archives/C05K04DASLS/p1706537689038059).

## Background

Users might need to modify their event stream for many reasons, such as:

1. Adding new attributes
2. Removing old events
3. Adding new events in bulk

Houseware recommends that these operations should be done in a way that ensures there is no downtime for users loading data and building new charts on the app.

## Recommended best practices

To enhance efficiency and avoid any service interruptions, we recommend the following process for updating your events data:

### Step 1: Create a new table

- Instead of dropping the `allevents` table, start by creating a new table (e.g., `allevents_new`) in Snowflake. Load your updated or modified events data into this new table.

### Step 2: Validate the new table

- Ensure that the new table (`allevents_new`) has the correct data structure, and the data loaded is accurate.
- Perform any necessary tests to validate the integrity and correctness of the data.

### Step 3: Rename Tables

- Once you are confident that the `allevents_new` table is ready, rename the original `allevents` table (e.g., to `allevents_old`).
- Immediately rename `allevents_new` to `allevents`.

> ❗️ **Critical Step**: Make sure to execute this step completely and quickly. No new charts will load on Houseware if there's no table with the name `allevents` on the data warehouse.

That's it! With the new `allevents` table in place, Houseware's services will seamlessly transition to the updated eventstream with no downtime.

> 📘 Optionally, after ensuring that the Houseware platform is functioning correctly with the new `allevents` table, the old table (`allevents_old`) can be archived or deleted based on your data governance policies.

## Advantages of This Approach

- **Minimized Downtime:** By avoiding dropping the `allevents` table, there is no interruption in Houseware's services
- **Data Integrity:** This method allows for validation of the new data before it goes live, ensuring accuracy in your analyses.
- **Seamless Transition:** The switch to the new data set is quick and efficient, ensuring continuity in your data analysis activities.

## Conclusion

By following these best practices for updating your ETL pipelines, you can ensure a more reliable and seamless experience on Houseware. Should you have any questions or require further assistance, please feel free to reach out to our support team on Slack or at [support@tryhouseware.com](mailto:support@tryhouseware.com).
