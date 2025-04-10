---
title: "How to connect Houseware to BigQuery"
slug: "how-to-connect-to-bigquery"
excerpt: "Learn how to connect your BigQuery Data Warehouse to Houseware."
hidden: false
createdAt: "Fri May 31 2024 03:55:29 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Jun 13 2024 07:36:24 GMT+0000 (Coordinated Universal Time)"
---
# Overview

This step-by-step guide will enable the Houseware application to access your events data for product analytics. To maintain separation of concern, we suggest you create a separate BigQuery dataset containing your events and share its access with our application.  

***

## Step-by-Step Guide

### Step 1: Get Houseware's Google Cloud Platform service account

Houseware will create a service account for your organization and provide you with a service account email, typically in the format of \<YOUR_ORG>-serviceaccount@[xyz.iam.gserviceaccount.com](mailto:xyz@abc.com).

### Step 2: Grant required permissions to the service account

To allow Houseware to read and process data from BigQuery, the service account will need the following roles granted to it:

#### 1. BigQuery Job User role

Grant this role to allow the Houseware application to run jobs on BigQuery. This will allow the Houseware application to run SQL on your BigQuery. Follow the steps below to grant this role.

> 📘 **Note**: Granting this permission requires access to the IAM console. You may need to contact your data/infra team to get these permissions.

[block:html]
{
  "html": "<div style=\"position: relative; padding-bottom: calc(57.07482993197279% + 41px); height: 0; width: 100%;\"><iframe src=\"https://demo.arcade.software/jRy6PUFQuN03O6fCQUER?embed&show_copy_link=true\" title=\"Welcome – badger – Google Cloud console\" frameborder=\"0\" loading=\"lazy\" webkitallowfullscreen mozallowfullscreen allowfullscreen allow=\"clipboard-write\" style=\"position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;\"></iframe></div>"
}
[/block]


<br />

#### 2. BigQuery Data Viewer and Editor roles

Grant both roles to the Houseware service account so that the Houseware application can read your events data and write internal metadata tables in your events dataset.

The Houseware service account requires the `BigQuery Data Editor` and `BigQuery Data Viewer` roles. You can follow the below Arcade for reference on how to grant these permissions.

[block:html]
{
  "html": "<div style=\"position: relative; padding-bottom: calc(57.07482993197279% + 41px); height: 0; width: 100%;\"><iframe src=\"https://demo.arcade.software/wsf82pWKSbJgKuANY9Hp?embed&show_copy_link=true\" title=\"Welcome – badger – Google Cloud console\" frameborder=\"0\" loading=\"lazy\" webkitallowfullscreen mozallowfullscreen allowfullscreen allow=\"clipboard-write\" style=\"position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;\"></iframe></div>"
}
[/block]


<br />

That's it! :tada: Houseware will now configure your connection and spin up an instance for your organization to do your analysis.
