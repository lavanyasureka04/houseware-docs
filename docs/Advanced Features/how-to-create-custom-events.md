---
title: "How to create Custom Events"
slug: "how-to-create-custom-events"
excerpt: "Learn how to combine multiple events together to create new custom events"
hidden: false
createdAt: "Fri Aug 25 2023 07:21:24 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jan 30 2024 11:27:16 GMT+0000 (Coordinated Universal Time)"
---
A custom event is a virtual event that can be created from one or more existing events, filtered down by their properties. Custom events help in:

1. Merging two or more events together into a single event. For example, "user signup" + "account created" can be merged as a single "signup" event.
2. Filtering an event to create a new event. For example, users who have signed up from the website like: "user signup" or "account created" with property filter 'source' as "website". 

Custom events provide flexibility to users to create their own KPIs on top of the existing granular events, relevant for their analysis. Let's look at how we actually create a custom event in Houseware.

[block:html]
{
  "html": "<div style=\"position: relative; padding-bottom: calc(53.20417287630402% + 41px); height: 0; width: 100%;\"><iframe src=\"https://demo.arcade.software/hmvEUN3FQPgUi1NFrNtx?embed\" title=\"Create Custom Events\" frameborder=\"0\" loading=\"lazy\" webkitallowfullscreen mozallowfullscreen allowfullscreen allow=\"clipboard-write\" style=\"position: absolute; top: 0; left: 0; width: 100%; height: 100%;color-scheme: light;\"></iframe></div>\n"
}
[/block]


***

# Step-by-step guide to create a Custom Event

Here is how you can create a Custom Event on your Houseware instance.

## Step 1: Go to the Events page

Go to the Event page through the left-hand navigation bar.

## Step 2: Click on + Custom Events

On the right-hand side of the search bar, select the + Custom Event button, which will navigate you to a new page to create a custom event.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6eaa2a9-Screenshot_2024-01-30_at_4.36.19_PM.png",
        "",
        "Click on **+ Custom Event** button"
      ],
      "align": "center",
      "sizing": "800px",
      "border": true,
      "caption": "Click on **+ Custom Event** button"
    }
  ]
}
[/block]


## Step 3: Select events and filters

After clicking the + custom event button on the events page, you will be redirected to a new page that will allow you to configure your custom event.

On this page, you can give your custom event a name and description and then select the events that you want to combine or filter to create your desired custom event.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0339f92-Screenshot_2024-01-30_at_4.47.53_PM.png",
        "",
        "Select events and event or user properties"
      ],
      "align": "center",
      "sizing": "700px",
      "border": true,
      "caption": "Select events and event or user properties"
    }
  ]
}
[/block]


## Step 4: Click Save

Once you are happy with your events selected or filters on top of it, click on the 'Save' button. Your custom event will now show up under the Custom section on the Events page, as shown in the screenshot below.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6a49cdf-Screenshot_2024-01-30_at_4.52.21_PM.png",
        "",
        "View Custom Events"
      ],
      "align": "center",
      "sizing": "700px",
      "border": true,
      "caption": "View Custom Events"
    }
  ]
}
[/block]


:tada: Your custom event will now be ready to be viewed under the 'Custom Events' tab on the right-hand side of the Events page. These events can be used for both Trends and Funnel types of visualizations.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/548bf82-Screenshot_2024-01-30_at_4.56.13_PM.png",
        "",
        "Use Custom Events in visualizations"
      ],
      "align": "center",
      "sizing": "700px",
      "border": true,
      "caption": "Use Custom Events in visualizations"
    }
  ]
}
[/block]
