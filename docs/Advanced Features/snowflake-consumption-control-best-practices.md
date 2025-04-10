---
title: "Snowflake Consumption Control Best Practices"
slug: "snowflake-consumption-control-best-practices"
excerpt: "Learn how to implement consumption controls for Houseware on top of Snowflake"
hidden: false
metadata: 
  image: []
  robots: "index"
createdAt: "Thu Nov 02 2023 07:48:48 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Nov 02 2023 14:24:13 GMT+0000 (Coordinated Universal Time)"
---
One of the core advantages for customers utilizing the power of warehouse-native product analytics with Houseware is - **complete control over the cost and performance of their experience**. As Houseware is [powered on top of the data warehouse](https://docs.houseware.io/docs/the-warehouse-native-way-for-product-analytics), customers are able to leverage all the power of a data warehouse to track and control their consumption.

This doc explains the different ways in which customers can track their Snowflake consumption driven by Houseware. Users can implement controls in the following ways:

1. Slack updates on Credit Consumption
2. Budgets & Quotas
3. Usage Dashboard on Houseware

## Slack Updates for Credit Consumption

For proactive updates on Snowflake credit consumption, Houseware’s Slack bot can send daily notifications of credit consumption on Slack to customers.

To enable Slack updated, follow the steps mentioned below on the Snowflake instance setup for Houseware:

> 👉 **Pre-requisites**: A Snowflake user, role, and default warehouse have been granted to the Houseware application (as detailed [here](https://docs.houseware.io/docs/how-to-connect-to-snowflake#step-2-grant-necessary-permissions-for-the-houseware-application))

**Step-1:** Setup a Snowflake view on the `ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY`. You can use the following SQL command for this:

```
CREATE SECURE VIEW <HOUSEWARE_DB>.<HOUSEWARE_SCHEMA>.filtered_warehouse_metering AS
SELECT *
FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY
WHERE WAREHOUSE_NAME = '<WAREHOUSE_ASSIGNED_TO_HOUSEWARE_ROLE>';
```

**Step-2:** Grant the Houseware role access to this Snowflake view. You can use the following SQL command for this:

```
GRANT SELECT ON VIEW filtered_warehouse_metering TO ROLE <HOUSEWARE_ROLE>;
```

That's it! You can let the Houseware team know once this is configured, and daily Slack alerts will start flowing in.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c4ee182-image.png",
        null,
        "Houseware Slack bot update for daily credit consumption"
      ],
      "align": "center",
      "caption": "Houseware Slack bot update for daily credit consumption"
    }
  ]
}
[/block]


## Budgets & Quotas

To stay within a limit of consumption, customers can implement **budgets & quotas** on Snowflake, which alerts them if the Snowflake consumption exceeds a certain quota - and allows for necessary mitigation to take place.

We suggest customers to use the following Snowflake features for setting this up:

### Monitor Resources

To help control costs and avoid unexpected credit usage caused by running warehouses, Snowflake provides resource monitors.

A virtual warehouse consumes Snowflake credits while it runs. A resource monitor can be used to monitor credit usage by virtual warehouses and the cloud services needed to support those warehouses. **If desired, the warehouse can be suspended when it reaches a credit limit.**

Check out [Snowflake documentation](https://docs.snowflake.com/en/user-guide/resource-monitors) for more information on this.

> 🌟 **Pro-tip**: Set up a weekly Resource Monitor with notifications enabled, keeping your historical Credit Consumption trend in mind.

Follow the steps below to create a resource monitor on Snowflake:

**Step 1:** Use the ACCOUNTADMIN system role.

**Step 2:** Click on `Account` tab » `Resource Monitors` » `Create Resource Monitor`.

**Step 3:** Set up the resource monitor as required. Refer to the screenshot below.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7926ac2-image.png",
        null,
        "Setup Resource Monitor"
      ],
      "align": "center",
      "sizing": "600px",
      "border": true,
      "caption": "Setup Resource Monitor"
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/cd04836-image.png",
        null,
        "A Resource Monitor setup on Snowflake"
      ],
      "align": "center",
      "sizing": "600px",
      "border": true,
      "caption": "A Resource Monitor setup on Snowflake"
    }
  ]
}
[/block]


### Budgets

A budget defines a monthly spending limit on the compute costs for a Snowflake account or a custom group of Snowflake objects. When the spending limit is projected to be exceeded, a daily notification email is sent to the email addresses designated to receive budget notifications.

> 👀 **Note:**Only a user with the `ACCOUNTADMIN` role can activate the account budget.

Use the following SQL commands to enable a role to create custom budgets for a given schema:

```
GRANT DATABASE ROLE SNOWFLAKE.BUDGET_CREATOR TO ROLE <houseware_role>;
GRANT USAGE ON SCHEMA <houseware_db>.<houseware_schema> TO ROLE <houseware_role>;
GRANT CREATE SNOWFLAKE.CORE.BUDGET ON SCHEMA <houseware_db>.<houseware_schema> TO ROLE <houseware_role>;
```

Once a role has been granted permission to create custom budgets, follow the steps given below to create a budget:

**Step 1**: Select `Admin` » `Usage`

**Step 2:** Select `Budgets`

**Step 3:** Set up the budget as required. Refer to the screenshot, shared below.

![](https://files.readme.io/31eaf64-image.png)

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3687f48-image.png",
        null,
        "A budget setup on Snowflake"
      ],
      "align": "center",
      "sizing": "600px",
      "border": true,
      "caption": "A budget setup on Snowflake"
    }
  ]
}
[/block]


## Usage dashboard on Houseware ( :sparkles: Coming Soon)

Admins on Houseware will soon be able to track the org’s Snowflake consumption in Houseware's admin section.

Here are some metrics that you will be able to track at a weekly level:

1. Total credits consumed in the last 30 days.
2. Credits consumed broken down by visualizations (flows, funnels, trends, retention, etc.)

These best practices will set you up for success in tracking your Snowflake consumption and making sure that the organization stays within the prescribed limits.

Have suggestions? We’re all ears! Reach out to us on Slack or on [support@houseware.io](mailto:support@houseware.io), and we’ll get back in no time. 🙂
