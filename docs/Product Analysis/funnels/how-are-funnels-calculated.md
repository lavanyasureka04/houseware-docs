---
title: "How are Funnels calculated"
slug: "how-are-funnels-calculated"
excerpt: "This document answers all questions about how Funnels in Houseware are calculated"
hidden: false
createdAt: "Wed Nov 22 2023 17:14:06 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Nov 22 2023 20:29:33 GMT+0000 (Coordinated Universal Time)"
---
# How can the conversion criteria in Houseware be configured?

While configuring a Funnel in Houseware, you can select conversion criteria through two primary options:

1. **Counting Criteria**: It determines how many times a particular user's activity counts towards conversion. It can be of two types - Uniques and Totals.
2. **Conversion Window**: The Conversion Window determines how much time a user has to convert through all steps of the funnel after entering it.

Details about each are given below.

## Counting Criteria

In Funnel, the percentage and absolute count of users converting at each step is dependent on the type of counting criteria selected. There are two types of counting criteria that you can select:

### Uniques

The Uniques option accounts for the unique number of users who completed the funnel. Even if the user completes the funnel multiple times within the configured date range, within the configured conversion window, the user is only counted towards conversion once. Funnels in Houseware, by default, are calculated using Uniques as the counting criteria.

> 👀 **Note:** Only the first user attempt is counted in Houseware's funnel. Hence all the steps completed in the first attempt will only be counted towards conversion, irrespective of the configured conversion window and selected time range. 
> 
> If in the first occurence, the user fails to complete all steps of the funnel, it will not be counted as converted, even if it converts in second, third, or later attempts within the selected time period.
> 
> Hence, **choose your conversion window wisely,** based on the contextual information of your events selected for a Funnel!

### Totals

The Totals option accounts for all the number of times users converted through the Funnel and counts multiple entries per user. Users can re-enter the funnel and are counted for conversion every time they enter it. 

A re-entry into the funnel begins every time a user performs the first step of the funnel, and each time this happens, the previous funnel entry is assumed to be completed.

For example, imagine a 3-step funnel: A, B, and C. User 1 does A -> A-> B-> C. In Totals, the user will be counted twice for step A, whereas for B and C, it will be counted as 1, and conversion will be counted as 1. Also, the time to convert will be counted from the second occurrence of the Step 1 event and not the first A in this example.

## Conversion Window

The Conversion Window determines how much time a user has to convert through all steps of the funnel after entering it. It allows for a more precise analysis of user behavior in relation to specific actions or goals within a given timeframe. 

For example, imagine a 4-step funnel to track a user journey from landing on a home page to making a purchase. If no conversion window is added, the funnel will count a user converted if they add a product to the cart today and purchase it a month later. This could misinterpret the effectiveness of this 4-step process on your product. If a 7-day window is set, it will only count users who completed the funnel in 7 days and will be more useful to understand how good or bad the funnel is performing.

***

# How are steps in the Houseware funnel ordered or connected?

For a funnel analysis, a user must complete the steps you designate in your Funnel in loose order. Loose order means a customer can engage in other actions between Funnel steps as long as they complete them in order.

Let's start with an example where the Funnel has steps: A, B, C, D, E and go through a few cases:

1. The customer does step A -> B -> C -> D -> E in exact order. Houseware counts this as a conversion.
2. The customer does step A -> B -> F -> C -> D -> E. Houseware counts this as a conversion and is also an example of loose ordering.
3. The customer does A -> B -> D -> C -> D -> E. Houseware will count this as conversion. Even though the customer did a D before the first time they did C, they will continue to convert because they eventually did a D after C within the conversion window.
4. The customer does step A -> B -> C -> E. Houseware will not count this as a conversion for E but will measure conversions for B and C, and the customer will not appear in the Funnel after step C. The customer's completion of step E is excluded from the Funnel because step D did not occur.
5. Only users who have gone through each former event in the configured Funnel will appear in any step. For Funnel A->B->C, users going from A to C directly will not show up in the Funnel.

To be counted as converted in a Houseware Funnel, all steps configured in the Funnel must be completed, starting from the first step event selected, within the time interval, and within the conversion window selected by the user.

***

# How is the conversion rate calculated?

To be counted as converted in a Houseware Funnel, all steps configured in the Funnel must be completed, starting from the first step event selected and within the time interval selected by the user.

For example, you created a Funnel with steps A -> B -> C with a conversion window of 1 hour.

If the user does A at 4 pm and then A again at 4:30 pm, before doing B at 4:45 pm and C at 5:15 pm, they would count as converting to B but will not be counted as completing the entire Funnel to C. This is because 4 pm to 5:15 pm is longer than one hour.

When counting for uniques (unique users), the conversion window for a given Funnel trial starts with the first instance of A and is not reset by later instances of A in the same trial. B and C need to be completed within the conversion window from the first instance of A to be counted as conversions.

In Totals (total events), each time the first step event gets triggered, the conversion window gets reset and starts from the latest occurrence of A.

As explained above, the steps configured in the Funnel are also loosely ordered.

***

# How does Houseware connect events in a funnel?

Houseware sequences the events of a funnel together by using device ID (device_id) and device timestamp (device_ts). Using these two data points, it links the sequences of the events together between a start and endpoint to generate a funnel and calculate the conversion rate at each step.

***

# How are the time intervals calculated in the 'Time to Convert' view?

Time intervals in the 'Time to Conver' view are calculated based on the 'Steps' and 'Interval size' configured by the user, which then allocates converted users into respective interval buckets.

In the case of Uniques: Each unique user is accounted for in one specific time-interval bucket. This is because the system recognizes and counts a single entry of a user, starting from its first occurrence and consequent completion of the steps in the time range as selected.

In the case of Totals: Each user might belong to multiple time interval buckets as they are counted every time they re-enter the funnel within the selected time range.

***

# What happens when a property used to break down a Funnel does not apply to an event in the Funnel?

 Houseware funnels follow 'first-touch attribution', which means if the property is not associated with the first step, even if it is associated with other steps of the Funnel, it will not break down the funnel. Hence, choose the breakdown attributes that are associated with the first step of the funnel events, or it will not break down into desired segments.

If a property is associated only with the first step and not with the consecutive second and third steps, the conversion will still be counted as is. Only the breakdown will be available for the first step and not for the rest of the steps.
