---
title: "[Old] How to Connect Houseware to BigQuery"
slug: "how-to-connect-to-bigquery-old"
excerpt: "Learn how to connect your BigQuery Data Warehouse to Houseware."
hidden: true
createdAt: "Fri Aug 18 2023 11:56:26 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri May 31 2024 05:42:13 GMT+0000 (Coordinated Universal Time)"
---
# Overview

This step-by-step guide will help you set up + connect a new BigQuery warehouse with the Houseware application. After completing the steps in this guide, you can view all selected product events on your Houseware instance to start analyzing and visualizing them.

***

## Step-by-Step Guide

### Step 1: Log in to Houseware and choose BigQuery as your CDW

- You will see the page below on logging in for the first time (before setting up). Choose the "Plug Houseware to work on your Cloud data warehouse" option here.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b73d134-image.png",
        null,
        "First landing page, click on the \"Connect warehouse\" button"
      ],
      "align": "center",
      "sizing": "700px",
      "border": true,
      "caption": "First landing page, click on the \"Connect warehouse\" button"
    }
  ]
}
[/block]


- Next, select BigQuery as the data warehouse you want to connect on reaching the following page.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/77e84d7-image.png",
        null,
        "Choose your Cloud Data Warehouse"
      ],
      "align": "center",
      "sizing": "700px",
      "border": true,
      "caption": "Choose your Cloud Data Warehouse"
    }
  ]
}
[/block]


> 🚧 To note before connecting
> 
> Before starting the connection process, make sure that you have the necessary access to create and manage **service accounts** (A service account is needed to give access to Houseware to operate on data). Check out the section below to know how to get the correct permissions.

To get the permissions that you need to manage access to a project, folder, or organization, ask your administrator to grant you the following IAM roles on the resource that you want to manage access for (project, folder, or organization):

- To manage access to a project: Project IAM Admin (`roles/resourcemanager.projectIamAdmin`)
- To manage access to a folder: Folder Admin (`roles/resourcemanager.folderAdmin`)
- To manage access to projects, folders, and organizations: Organization Admin (`roles/resourcemanager.organizationAdmin`)
- To manage access to almost all Google Cloud resources: Security Admin (`roles/iam.securityAdmin`)

Now with the necessary permissions, we can move on to **creating a warehouse connection**.

### Step 2: Upload a Service Account Key

For Houseware to interact with the service account of your google cloud project, it needs to connect securely with the account's service identity. This is done by creating a **private service account key in .JSON format**, which is to be uploaded on the Houseware app.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e97dd21-image.png",
        null,
        "An example .JSON key file is attached here"
      ],
      "align": "center",
      "sizing": "700px",
      "border": true,
      "caption": "An example .JSON key file is attached here"
    }
  ]
}
[/block]


### How to get this key?

1. Go to your [google cloud console](https://console.cloud.google.com/welcome?pli=1&project=quizizzer)
2. Select your **organization** and **project** from the top left

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4439de1-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px",
      "border": true
    }
  ]
}
[/block]


3. Go to the navigation menu and go to **Service accounts**

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f4fb117-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px",
      "border": true
    }
  ]
}
[/block]


4. In the service accounts section, **choose the service accoun**t for which they key needs to be generated and click on **manage keys**

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/bb7da26-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px",
      "border": true
    }
  ]
}
[/block]


5. Click on** create a new key**

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/39790ae-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px",
      "border": true
    }
  ]
}
[/block]


6. Create a **JSON keyfile**, and **upload it on Houseware** app

### Step 3: Create a Cloud Storage Bucket

The next step is to ingest a **GCP bucket** to ingest data from Fivetran (our data connector). Also, ensure the bucket is in the exact location of the dataset(US). You will also have to change** bucket access** to **fine-grained**

> 📘 What's a bucket and what exactly are we doing
> 
> A bucket is nothing more than a container for your data. Everything that you store on google cloud storage resides in a bucket. You can use buckets to organize your data and control access to your data. We would be needing **Storage Object Admin** permission for the bucket to read and write data from the bucket. All the models and metrics you create get stored in your own warehouse this way.

> 📘 Access Control: Fine-Grained
> 
> When data is stored together in the cloud, fine-grained access control is essential since it allows data with different access requirements to ‘live’ in the same storage space without running into security or compliance issues. Fine-grained access control uses more nuanced and variable methods for allowing access. [Read More.](https://www.immuta.com/blog/what-is-fine-grained-access-control-and-why-its-so-important/)

### How to set up bucket access control?

1. Click on the top-left menu and go to the **Cloud Storage** section

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d370c47-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px",
      "border": true
    }
  ]
}
[/block]


2. Go to your bucket and open settings, click on **edit access**

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d2d1604-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px",
      "border": true
    }
  ]
}
[/block]


3. Make sure the access control setting is configured to** fine-grained**

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/770f512-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px",
      "border": true
    }
  ]
}
[/block]


4. We need to set up **Storage Object Admin** for the bucket now, click on **add principal**

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/75ff127-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px",
      "border": true
    }
  ]
}
[/block]


5. Here select the** role of the principal** as Storage Object Admin. Go to Cloud Storage -> Storage Object

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/bdacf55-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px",
      "border": true
    }
  ]
}
[/block]


Enter the bucket name on Houseware!

### Step 4:  Name the schema on which you want Houseware to materialize the transformed tables and metrics

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/12f9b6f-image.png",
        null,
        "Name the schema"
      ],
      "align": "center",
      "sizing": "700px",
      "border": true,
      "caption": "Name the schema"
    }
  ]
}
[/block]


Click on the Connect button to complete the connection. 

 :tada: Your BigQuery is now connected to your Houseware application!
