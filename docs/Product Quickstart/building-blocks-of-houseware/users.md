---
title: "Users"
slug: "users"
excerpt: "Know more about the User Activity page on Houseware"
hidden: false
metadata: 
  image: []
  robots: "index"
createdAt: "Wed Aug 30 2023 08:37:40 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Oct 02 2023 13:02:06 GMT+0000 (Coordinated Universal Time)"
---
Each unique individual performing an event on the product is a user. For example, the unique person who clicks the 'start workout' button will be a product user.

Houseware identifies each unique user from your events schema's `user_id` column. It helps determine the number of users completing any event on each specific timestamp.

***

# User Activity

The User Activity page is available on the left-hand nav bar on Houseware. It lets you go through the entire event stream of a user. It shows the entire sequence of events a user did on each day, along with details of each event performed. Check out the GIF attached below for reference.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/34c3e70-user_activity_hw.gif",
        "",
        "Houseware User Activity page"
      ],
      "align": "center",
      "sizing": "600px",
      "border": true,
      "caption": "Houseware User Activity page"
    }
  ]
}
[/block]


This page can be especially useful for debugging in case a particular user is facing some issue with your product and you want to quickly go through the list of events they did.

***

# Houseware User Roles

Houseware currently supports two types of Houseware user roles - `Admin` and `Member`. An admin member has special privileges that grant them more control over the product like:

1. :heavy_plus_sign: Add new users to the Houseware platform
2. :point_right: Assign the role of admin or member to each Houseware user added
3. :lock: Hide events

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/07694bb-Screenshot_2023-09-20_at_4.42.59_PM.png",
        "",
        "Dropdown for admins to select user role"
      ],
      "align": "center",
      "sizing": "500px",
      "border": true,
      "caption": "Dropdown for admins to select user role"
    }
  ]
}
[/block]


Also, the admin tab on the left-hand nav will be **visible only to the admin users** and not to the members.

More capabilities coming soon! 💪
