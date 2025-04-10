---
title: "Stickiness"
slug: "stickiness"
excerpt: "Learn how to create stickiness blocks on Houseware"
hidden: false
createdAt: "Tue Nov 28 2023 18:50:10 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Nov 29 2023 08:28:13 GMT+0000 (Coordinated Universal Time)"
---
Stickiness blocks measure the frequency with which users engage with your product within a specific time frame. They are essential for understanding user engagement in your product.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2728bbc-Stickiness_on_Houseware.gif",
        null,
        "Stickiness on Houseware"
      ],
      "align": "center",
      "caption": "Stickiness on Houseware"
    }
  ]
}
[/block]


Stickiness is important because it indicates how often and consistently users engage with a product. High stickiness suggests strong user engagement, which is crucial to ensure that a product is providing value to its users.

## How does Houseware measure stickiness?

In Houseware, stickiness is calculated **non-cumulatively**.

This calculation shows you the percentage of users who did the event **at least once** for the **exact number of days** listed on the X-axis.

**For eg:** users in the `Day 3` bucket have triggered the event on exactly three days over the course of a week (or month) in the time frame of your analysis, while those in the `Day 4` bucket have done it for exactly four days in a week.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/cb38ae5-image.png",
        null,
        "Stickiness on Houseware"
      ],
      "align": "center",
      "caption": "Stickiness on Houseware"
    }
  ]
}
[/block]


***

# Step-by-step guide to creating a Stickiness block

Follow the steps given below to create a stickiness curve on Houseware.

## Step 1: Add a new Stickiness visualization block to your workspace

Add a new visualization block on your workspace and choose **Stickiness** as the visualization type. Once the block is created, configure it based on how you want to measure user engagement.

## Step 2: Select an event of interest

Select the event you're interested in in the config menu on the right side (as shown in the GIF above).

> ℹ️ **Note**: Unlike other Houseware visualisations, you are limited to analyzing a single event in a Stickiness block.

## Step 3: Select frequency and date range

Choose the frequency for your analysis: **week** or **month** and the time frame for your analysis.

> ℹ️ **Note:**
> 
> - To ensure consistency and reduce variability in your analysis, Houseware automatically resolves the selected date range to complete weeks (or months) depending on the frequency of analysis.
> - For example: if the frequency of analysis is weekly, and the selected date range is Wed, 29th Nov - Thu 30th Nov, it resolves to Mon, 27th Nov - Sun 3rd Dec.

These are the only necessary steps to create your stickiness block. Once completed, you can click on the Apply Configuration at the bottom of the config modal, and your stickiness block will be up. :tada:

***

# Configuration Features available for Stickiness

## Filter by time

You can choose the time frame you want stickiness to be computed. Currently, only `Between Dates` filter is enabled in the Stickiness visualization.

### Between Dates

Choose a start date and an end date. Stickiness will be calculated over events data **for the complete weeks or months in this date range** (as mentioned above).

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2551430-image.png",
        null,
        "Between Dates filter on Houseware"
      ],
      "align": "center",
      "caption": "Between Dates filter on Houseware"
    }
  ]
}
[/block]


## Add Filters

You can use the configure menu for Stickiness blocks to add cohorts and user/event properties as filters.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/05ae702-image.png",
        null,
        "Add event property filters on Houseware"
      ],
      "align": "center",
      "sizing": "500px",
      "caption": "Add event property filters on Houseware"
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b6ca3b8-image.png",
        null,
        "Add user property filters on Houseware"
      ],
      "align": "center",
      "sizing": "500px",
      "caption": "Add user property filters on Houseware"
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/cb53942-image.png",
        null,
        "Add cohort filters on Houseware"
      ],
      "align": "center",
      "sizing": "500px",
      "caption": "Add cohort filters on Houseware"
    }
  ]
}
[/block]


## Add Breakdown

Breakdowns enable you to go deeper and compare the drivers for certain user actions on the product. On the stickiness blocks, you can set breakdowns on user cohorts, and event/user properties.

> ℹ️ **Notes:**
> 
> 1. Houseware returns the top 8 dimension values based on the average number of users who did the event over the time frame of analysis. To restrict the breakdown to a specific set of dimension values, you can apply relevant filters on the visualisation for the same dimension.
> 2. Currently, for user cohorts, Houseware only enables a **single cohort breakdown**. Eg.: if the cohort `Active Users` is added as a breakdown, you would see stickiness broken down for: `Users in Active Users cohort` and `Users not in Active Users cohort`.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4bee851-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "500px"
    }
  ]
}
[/block]


***

That's it! Hope this helps you to build stickiness blocks on Houseware and visualize your user engagement. Got questions or feedback? Reach out to us on Slack or at [support@tryhouseware.com](mailto:support@tryhouseware.com).
