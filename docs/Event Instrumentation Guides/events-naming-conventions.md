---
title: "Events Naming Conventions"
slug: "events-naming-conventions"
excerpt: "Best practices on how to name your events while capturing it so that it serves both the implementation team & stakeholders who will be using this data."
hidden: false
metadata: 
  image: []
  robots: "index"
createdAt: "Wed Oct 11 2023 07:45:47 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Oct 17 2023 08:29:02 GMT+0000 (Coordinated Universal Time)"
---
Defining and naming events for tracking user actions in a product is essential to product analytics. The aim is to capture meaningful data that allows for insightful analysis while also ensuring that event names and structures are clear and understandable for all stakeholders, such as product managers and analysts.

It is important to define naming conventions upfront and not every time you define instrumentation for a new feature.

# Factors to keep in mind

Here are a few points to consider while creating a structure for naming events.

1. **Audience**: Event naming needs to be easily understood by people who may not have been involved in the implementation but will be using the data for analysis or decision-making.
2. **Scalability**: The system should be able to accommodate new types of events or modifications to existing ones without causing confusion.
3. **Reusability**: Naming conventions should be applicable across different parts of the application to reduce cognitive load.
4. **Flexibility**: The naming should not be too specific to allow for future changes, nor too vague that it becomes meaningless.

Below we describe a step-by-step process to think through your event naming standards and how to execute it.

***

# How to set naming conventions

Thinking through and deciding the following things will help you create your event naming convention. These decisions will make sure that your event names are not created in a haphazard way, making them difficult for end users to understand and discover. 

1. **Event case**: Decide upfront whether you want snake_case, Proper Case, or camelCase for event names and property names. Tools like Amplitude will display 'Female' and 'female' as different values unless you create and maintain manual transformations in the tool's interface.
2. **Object-Action or Action-Object:** It is important to decide if you will name your events starting with an action or starting with the object it refers to. For example: `Clicked Page` or `Page Clicked`. [Segment also talks about this framework in its documentation also](https://segment.com/academy/collecting-data/naming-conventions-for-clean-data/) with the help of examples.
   1. To do this, it is also important to list out all possible actions on the product, like click, view, sign-up, and more.
3. **List out important contextual information**: Each event might have contextual information that could be vital for understanding the event, such as 'ScreenName', 'ButtonType', etc. Hence using screen type or button type in the event name can be important to help end users understand the event better.
4. **Think through cross-platform events actions: **For example, interacting with a button UI element can be a 'click' on a desktop but a 'tap' on a mobile or tablet. However, qualitatively if it represents the same user interaction, it should have the same name. This will also help you see correct data if you split an event by device type.

> 👀 **Note**: Avoid using developer of designer jargon like 'nav', 'modal', interstitial or acronyms as they may not be universally understood.

Use the above pointers to set your naming standards, and keep the names human-readable. This is the fundamental groundwork that you will need to do thoroughly to reap the true benefits of product analytics.
