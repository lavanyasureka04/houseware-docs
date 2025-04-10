---
title: "Building Blocks of Houseware"
slug: "building-blocks-of-houseware"
excerpt: "Key concepts that will help you analyse and use your product data on Houseware"
hidden: false
createdAt: "Thu Aug 17 2023 07:23:21 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Jun 13 2024 07:39:13 GMT+0000 (Coordinated Universal Time)"
---
# Overview

Are you excited to start your product analytics journey with Houseware?! If yes, you are at the right place. Houseware is proactively designed to optimize your product analytics workflow - it lets you understand user behavior, optimize features, or get insights into how your product is being used. 

Before deep-diving into all its features and functionalities, let's understand its core building blocks, which will help you quickly navigate your product data and analyze it in multiple ways on Houseware. 

# Building Blocks

The key concepts listed here will help familiarize you with Houseware's core concepts and definition and be able to use the product at its best.

## [Events](https://docs.houseware.io/docs/events)

An event is a data point representing each unique action the user takes on your product. For example, clicking the 'start workout' button on a fitness app will be recorded as an event. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f5a7eea-Screenshot_2023-08-24_at_1.36.56_PM.png",
        "",
        "Houseware's Events tab"
      ],
      "align": "center",
      "sizing": "36px",
      "border": true,
      "caption": "Houseware's Events tab"
    }
  ]
}
[/block]


On Houseware, events are the fundamental unit of each product analytics visualization, like funnels, flows, retention charts, etc.

> 🌟 **Feature highlights**
> 
> 1. View event details & its properties
> 2. Create custom events
> 3. Hide and show events

To learn more about connecting your events data to Houseware, refer to this article here: :point_right: [How to set up Houseware.](https://docs.houseware.io/docs/how-to-connect-your-product-data-to-houseware#step-by-step-guide)

## [Users](https://docs.houseware.io/docs/users)

Each unique individual performing an event on the product is a user. For example, the unique person who clicks the 'start workout' button will be a product user.

Houseware identifies each unique user from your events schema's `user_id` column. It helps determine the number of users completing any event on each specific timestamp.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/63a43be-Screenshot_2023-08-24_at_2.01.05_PM.png",
        "",
        "Houseware's User Activity feed"
      ],
      "align": "center",
      "sizing": "484px",
      "border": true,
      "caption": "Houseware's User Activity feed"
    }
  ]
}
[/block]


## Properties

Properties are characteristics that help you define an **Event **or a **User**.

### Event Property

Attributes that describe the events are referred to as event properties. For example, '**type of workout**' can be an event property with values such as - yoga, strength & conditioning, etc. They can be specific to each event or generic and applicable to all product events.

### User Property

Attributes describing a user are called user properties. For example, a user's '**plan type**' is a user property with values such as - trial, paid, pro, etc. It could be their name, region, age, any detail that describes them.

> 🌟 **Feature Highlight**
> 
> Both event and user properties can be used to add filters and breakdown Houseware's visualizations in groups as desired. These properties help in getting more granular insights.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/aea5dcf-Screenshot_2023-08-24_at_2.32.19_PM.png",
        "",
        "User and Event properties present in visualization's config"
      ],
      "align": "center",
      "sizing": "302px",
      "border": true,
      "caption": "User and Event properties present in the visualization's config"
    }
  ]
}
[/block]


## [Cohorts](https://docs.houseware.io/docs/cohorts)

A cohort is a specific group of users segmented based on certain user properties or exhibit similar behavior on the product by performing similar events or sequences of events. For example, 'highly engaged users in Chicago' can be a cohort with user property 'city' selected as Chicago, and an event behavior can be 'completed training' more than 5 times a week.

Houseware lets its users create these cohorts by specifying the user property or event behavior through an intuitive UI and using it to drive focused product analytics.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/39e0a4f-create_cohorts.png",
        "",
        "Cohort Creation View on Houseware"
      ],
      "align": "center",
      "sizing": "600px",
      "border": true,
      "caption": "Cohort Creation View on Houseware"
    }
  ]
}
[/block]


> 🌟 **Feature Highlight**
> 
> Cohorts can be used as filters or used to breakdown flows, funnels, retention, trends, etc. visualizations on Houseware to analyze data only for a specific set of users.

## [Workspaces](https://docs.houseware.io/docs/how-to-create-your-workspace)

A workspace in Houseware is where you can start doing your analysis by adding visualizations (flows, funnels, trends, etc.), texts, or any other embeds you want.

As the name describes, it acts as your personal workspace where you can experiment, monitor, view, and analyze your product analytics data. Your workspace stays accessible only to you unless you share its access with someone, just like docs in G-Drive.

> 🌟 **Feature Highlight**  
> A Houseware workspace facilitates collaboration through features like-
> 
> - **Notifications**: Whenever a user tags you on any visualization, notification will show up on your workspace.
> - **Annotations**: All annotations marked on your visualizations will show up on the Homepage of your Houseware workspace.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a83d051-image_16.png",
        "",
        "Houseware Workspace Home"
      ],
      "align": "center",
      "sizing": "500px",
      "border": true,
      "caption": "Houseware Workspace Home"
    }
  ]
}
[/block]


Excited to start using Houseware?! :zap: Refer to the [Product Analysis](https://docs.houseware.io/docs/funnels) section of the docs to learn more about each visualization :bar_chart: available to analyze your product analytics data on Houseware.
