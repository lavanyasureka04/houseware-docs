---
title: "Entities"
slug: "entities"
excerpt: "Learn about Entities in Houseware"
hidden: true
createdAt: "Tue Jun 11 2024 00:56:22 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Jun 13 2024 06:27:30 GMT+0000 (Coordinated Universal Time)"
---
Entities are fundamental components in Houseware that represent distinct objects or items within your business. Houseware enables a more holistic analysis by surfacing these entities for analysis, allowing product managers to understand user behaviour in the larger business context.

For instance, in a gaming application, entities might include games and players; in an e-commerce application, entities might include SKUs and Sellers, each with unique properties and characteristics.

Events rarely contain all the information PMs might need to analyse user behaviour. Entities provide an easy way of marrying event data with other business data already sitting in your data warehouse.

<br />

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/41b3bf0-Web_App_Reference_Architecture_6.png",
        "",
        "Houseware Architecture"
      ],
      "align": "center",
      "sizing": "600px",
      "border": true,
      "caption": "Events and Entities, enabling cross-functional product analytics"
    }
  ]
}
[/block]


<br />

***

# Use Cases & Examples

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c774945-image.png",
        null,
        "Houseware allows users to define and analyse both events and entities, on a single platform"
      ],
      "align": "center",
      "sizing": "650px",
      "border": true,
      "caption": "Houseware allows users to define and analyze both events and entities on a single platform"
    }
  ]
}
[/block]


Houseware empowers product managers to filter and break down their analyses by granular entity properties.

This capability enhances the depth and richness of analytical insights and facilitates a more comprehensive understanding of how different parts of your product interact and perform. Let's explore how these entities and their associated properties can be leveraged in Houseware to drive more informed decision-making.

Below is a digital fitness app where users can purchase subscription plans.

<br />

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/51c662e-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "350px",
      "border": true
    }
  ]
}
[/block]


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d14f901-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "350px",
      "border": true
    }
  ]
}
[/block]


<br />

PMs are interested in analyzing the event `Join Plan Clicked` which gets triggered when the user buys a subscription. Because subscriptions are bought outside the product, the event data alone does not have the transaction context. Hence, `Join Plan Clicked` doesn't contain attributes related to the transaction; it just contains the `transaction_id`. 

However, in this case, transaction data is being synced to the data warehouse. Houseware configures an entity called `Transaction` that contains attributes like `Category`, `Product`, and `Transaction amount`. 

With this entity, users can bring Transaction attributes into their analysis, opening up use cases like - Analyze app activity for users who have made transactions with amounts greater than $30 only.

<br />

***

# How to configure entities?

Configuring an entity on Houseware can be done in the following 3 steps

## Step 1: Define entities on Houseware

Provide the following details on Houseware to define an entity:

- **Name:** Name of the entity; this will be exposed to the users on Houseware charts
- **Description:** A description of what business concept this entity represents with any additional information about when and how to use it
- **Database:** The name of the database containing the entity table/view
- \*Schema:\*\* The schema containing the entity table/view
- **Table:** The name of the table/view to be used on Houseware
- **Unique key:** A column representing each row in the entity table **uniquely**. This key is used for enriching event data with entity attributes. More details on the same are mentioned below.

<br />

> 👀 **Note:**This column should follow the unique key constraint

<br />

## Step 2: Select the entity attributes

- **Select the columns from the entity table**: These columns should be available on Houseware as "entity attributes". These entity attributes will be available on Houseware for users to filter or break down their data
- **Map the entity to your product events:** Define how the entity maps to your event data. To do this, you can:
- **Define Unique Key**: List the event properties containing the entity table's unique key.
  - For example, to create an entity `transaction` for a subscription-based product, `transaction_id` can be an event property for the event `Join Plan Clicked`, which maps to the unique column `id` in the `transaction` entity table
    > 👀 **Note:**
    > 
    > 1. Users can list one or more event properties while defining a mapping with the entity unique key.
    > 2. Events containing any of the above-listed event properties will automatically inherit all the attributes related to the entity.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f3661f3-image.png",
        null,
        "Illustration of 2 entities - Transaction and Class and how they are related to product events"
      ],
      "align": "center",
      "sizing": "650px",
      "border": true,
      "caption": "Illustration of 2 entities - Transaction and Class and how they are related to product events"
    }
  ]
}
[/block]


***

# Entity Model Requirements

All entities defined on Houseware must meet the following requirements:

### Primary Key Requirement

Every entity should have a primary key. This unique identifier facilitates and ensures data integrity. The primary key must be clearly specified while defining the data model.

### Attribute Data Types

Entity attributes (used for filters or breakdowns on the Houseware app) should have one of the following data types:

1. `string`
2. `bool`
3. `integer`
4. `float`
5. `datetime`

# Chained Entities

In some scenarios, you may have entities in your data that are linked to each other by a common key. For example: `transaction` and `invoices`. Houseware supports such entities in the following ways:

1. Defined all chained entities individually on Houseware, as explained above
2. In case one or more chained entities do not have a **unique key** that is present as an event property on Houseware, we recommend applying **denormalization** and maintaining a compound entity (with a **unique key** that is also present as an event property on Houseware). This compound entity should integrate attributes from all the interlinked entities, ensuring faster and more efficient querying

That's it! This is how you can use and define entities on Houseware. Feel free to reach out to the Houseware team on Slack or Email in case of any doubts.
