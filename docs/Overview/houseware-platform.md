---
title: "The Houseware Platform"
slug: "houseware-platform"
excerpt: "Learn about the modular components in Houseware, and how they enable a platform-first approach for the Houseware experience!"
hidden: false
createdAt: "Tue Jun 11 2024 13:05:29 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Jun 13 2024 07:36:42 GMT+0000 (Coordinated Universal Time)"
---
# Overview

Houseware is a no-code, warehouse-native platform designed to streamline product analytics workflows.

 Houseware eliminates the need for complex data transfers and modeling by working directly within your data warehouse. The platform-first approach ensures a modular, scalable, and secure solution that can be tailored to various analytical needs. This architecture allows for easy integration with multiple data sources, providing flexibility and a promise of accuracy to the product teams while maintaining strong governance and observability on the data warehouse for data teams.

By leveraging the center of gravity of data in your organization, Houseware offers real-time insights and comprehensive analytics capabilities. The platform's modular components enable customization and extensibility, making it suitable for diverse use cases. With a strong emphasis on security and compliance, Houseware ensures that your data is protected while delivering actionable insights. 

***

# Building Blocks

Here are the key building blocks that power the Houseware Platform

- **Events**: Represent unique user actions on your product.
- **Event Properties**: Attributes that describe events.
- **Users**: Unique individuals performing events on your product.
- **User Properties**: Attributes that describe users.
- **Cohorts**: Specific groups of users segmented by properties or behaviors.
- **Entities**: Fundamental components representing distinct objects or items within your product ecosystem.
- **Event Schema**: The structured format required to make events and user data available for analysis in Houseware.

For detailed information on each building block, please refer to our comprehensive documentation [here](https://docs.houseware.io/docs/building-blocks-of-houseware).

***

# Composability

Houseware's platform is designed for composability, allowing you to build a flexible and scalable analytics environment that meets your specific needs. This modular approach allows individual components to be integrated, extended, and replaced without affecting the overall system, ensuring seamless compatibility with your existing data infrastructure. This approach ensures that Houseware can integrate seamlessly into your existing data infrastructure and grow with your business.

We follow the principle of "**Configuration over Convention**", allowing maximum flexibility to the end users to best design their use cases and solve their specific challenges:

- **Choice of Warehouse**: Houseware supports integration with multiple data warehouses, providing flexibility and scalability for your analytics needs. Whether you are using Snowflake, BigQuery, or another data warehouse solution, Houseware ensures a consistent product experience.
- **Flexible Schema**: Houseware’s schema is designed to be customizable to most event streams and flexible to any frequency, whether batch or real-time. This ensures that your data is always ready for analysis regardless of how it is ingested.
- **Warehouse-Native**: Leverage the center of gravity of data in your organization by working natively within your existing data warehouse. This enables product teams to derive cross-functional insights by merging disparate data sources like clickstream events, transactional data, and SaaS datasets, all on the trusted data warehouse.
- **Customizable**: Houseware allows users to build custom events, cohorts, and other analytics components tailored to their specific needs. This customization ensures that the analytics setup aligns perfectly with the business requirements.
- **Integrations**: The composable platform approach enables inbound integrations(with CDPs/transaction DBs) and writeback syncs with a wide range of marketing, sales, and business tools, allowing for a best-of-breed approach to building your stack. These integrations can be managed programatically, allowing developers to build unique workflows.
- **Access Controls**: Access controls in Houseware are defined once and applied everywhere up the stack, ensuring consistent and secure data access across the platform. This centralized approach simplifies the management of permissions and enhances security, allowing organizational admins to build their own access policies.

***

# Data Platform

Houseware's data platform is designed to provide a robust, scalable, and secure environment for product analytics. A warehouse-native architecture demanded a unique perspective at building multiple workloads, that worked agnostic of the storage layer or the query engines. 

Listed below are some of the workloads supported by the Data Platform

## Data Schema

Houseware employs an activity schema-esque data schema that organizes events into a set of mandatory and optional attributes. This enables:

- **Scalability**: Efficiently handles large volumes (up to tens of billions) of event data at runtime. The schema supports high-throughput data ingestion and processing, maintaining robust performance as data scales.
- **Flexibility**: Accommodates new event types and attributes without requiring schema changes. This allows for seamless integration of new data points as the product evolves, avoiding extensive redesigns.
- **Simplicity**: The schema is user-friendly and adaptable to various scenarios, making it easy to model and query data. It minimizes the learning curve for users and simplifies data management.
- **Efficiency**: Optimizes query performance by structuring data for fast retrieval and analysis. The schema supports efficient indexing, clustering and partitioning, which speeds up query execution times.
- **Consistency**: Ensures uniform data formatting and structuring across the organization. This standardization simplifies data integration, governance, and compliance.
- **Reduced Complexity**: Minimizes the complexity of data transformations by using a straightforward schema that maps easily to various data sources. This simplification accelerates the ETL process and reduces the potential for errors.

## Metadata:

Metadata in Houseware refers to data about events/entities. It serves several critical functions:

- **Query Optimization**: Enhances query performance by providing statistics, indexing information, and other query-related metadata. This allows the query engine to make informed decisions about query execution plans, improving efficiency and reducing execution times.
- **Incremental Processing**: Tracks changes and updates in data, enabling efficient incremental query processing. By identifying and processing only the data that has changed since the last update, it minimizes data reprocessing and reduces load on the data warehouse.
- **Enhanced User Experience**: Metadata allows users to know specific details about their event names, event dimensions, user properties, date ranges, hence informing the users about the available options for analysis.

### Key Metadata Components

- **Dimensions**: Metadata about event attributes that are first-class columns in the events table. This includes information such as the dimension name, possible values, data type, and cardinality.
- **Event Names and Properties**: Metadata about event names and their associated properties, including property values, data types, and cardinality. This is stored in a dedicated table to facilitate efficient querying and analysis.
- **Event Time Range**: Metadata about the earliest and latest timestamps of events, allowing for time-based filtering and analysis. This is essential for temporal queries and understanding data recency.
- **First-Time Event Mapping**: Tracks the first occurrence of specific events for each user, enabling analysis of first-time user actions. This mapping is crucial for understanding user onboarding and initial interactions.
- **ID Mapping**: Maps device identifiers to user identifiers, resolving multiple occurrences of events from different devices to a single user. This ensures accurate user tracking and analysis.
- **Custom Enrichment**: Allows users to add custom metadata such as event tags, descriptions, and dimension types, enhancing the analytical capabilities and contextual understanding of the data.

## Real-Time Analytics

Realtime analytics in Houseware enables immediate data processing and analysis, providing up-to-date insights as data is generated. This capability is essential for applications requiring timely decision-making based on the latest events.

Realtime analytics is achieved through continuous data ingestion, processing, and querying. Data is streamed from various sources into the data warehouse, where it is immediately available for analysis.

### Architecture

The reference architecture for realtime analytics in Houseware, supporting both BigQuery and Snowflake, is as follows:

- **Data Ingestion**: Data is continuously ingested from various sources, such as user interactions, IoT devices, or application logs. This data is sent to a cloud storage service like Google Cloud Storage (GCS) or AWS S3.
- **Data Processing Pipeline**:
  - GCP DataFlow: For environments using BigQuery, GCP DataFlow processes the ingested data in real-time, applying necessary transformations such as parsing, filtering, and enrichment.
  - AWS Kinesis / Apache Kafka: For environments using Snowflake, streaming data is processed using AWS Kinesis or Apache Kafka with AWS Lambda or Apache Flink for transformations.
- **Metadata Update:** As new data arrives, metadata in the warehouse is updated in real-time. This includes updating dimension tables, event names, and property values, ensuring that the latest data is available for querying.

## Caching

Houseware employs multiple caching strategies to enhance performance for end users of the platform:

- **Application Cache**: Caches visualization queries and metadata requests to reduce load on the warehouse and improve response times. Visualization queries are cached for 365 days, while metadata queries are cached for 1 hour.
- **Warehouse Cache**: Utilizes native warehouse caching mechanisms (e.g., Snowflake's result cache, local disk cache, and remote disk cache) to speed up queries.

## Deployment models for "Query Compute"

Houseware offers flexible deployment models to suit different organizational needs. While the customer connects their own data warehouse, they still have the flexibility to choose between the following models:

**Bring-your-own-Compute**: In the Bring-your-own-Compute model, customers utilize their existing data warehouse compute resources for query execution. This model provides several advantages:

- Control: Customers maintain full control over their compute resources, allowing them to manage performance, scaling, and cost directly.
- Optimization: Enables customers to optimize query execution based on their specific workload and performance requirements.
- Integration: Seamlessly integrates with existing data governance and security policies within the customer's environment.

**Houseware-Compute**: In the Houseware-Compute model, Houseware leverages "Snowflake Secure Data Sharing" or "BigQuery Data Sharing" to simplify the compute process for customers. In this model, Houseware absorbs the compute costs and abstracts it away from the customer. Key benefits include:

- Simplified Management: Customers do not need to manage or optimize compute resources, as Houseware handles all aspects of query execution.
- Cost Efficiency: Houseware absorbs the compute costs, providing a predictable pricing model and reducing the customer's operational overhead.

## Identity Resolution

Houseware provides advanced identity resolution capabilities to unify user identities across different data sources, helpful for digital applications where non-loggedin user behavior is critical to their product flows.

- **Device and User ID Mapping**: Houseware's algorithms map device identifiers to user identifiers to track user activities across multiple devices. This mapping enables accurate tracking and analysis of user behavior, even when users switch between devices, ensuring accurate user insights.
- **First-Time Event Mapping**: Houseware identifies the first occurrence of specific events for each user. This mapping helps in understanding user onboarding and initial interactions with the product, which is crucial for optimizing user experience and engagement strategies.

## Cost Management (Budgeting, Quotas, and Cost Observability)

Houseware offers robust tools to manage and observe costs associated with data processing and analytics. These capabilities ensure that customers can maintain fine-grained control over their data warehouse expenditures while optimizing query performance.

- **Cost Observability**: Costs are broken down by specific query patterns, allowing customers to see which queries or analytical operations are consuming the most resources. The platform continuously monitors compute costs and detects anomalies. If there is an unusual spike or unexpected pattern in costs, alerts are sent to the designated Slack channels, enabling prompt investigation and resolution.
- **Budgeting & Quotas**: Customers can define usage quotas and budgets directly on their Data Warehouse(Snowflake/BigQuery). Budgets can be defined for overall data warehouse usage as well as for specific query types or runtimes. This helps in tracking and controlling spending, ensuring that costs remain within the planned limits.

## Query Observability

The Houseware Data Platform has internal query observability to monitor and optimize query performance. These capabilities ensure that queries run efficiently, resource usage is optimized, and any issues are quickly identified and resolved.

**Query Logging** Houseware tracks and logs all query executions, providing a detailed record of each query's lifecycle:

- Execution Tracking: Logs the start time, end time, and duration of each query, along with the query text and execution context.
- Error Logging: Captures any errors or exceptions that occur during query execution, facilitating troubleshooting and root cause analysis.
- User and Session Information: Logs metadata about the user and session that initiated the query, helping to correlate queries with specific users or applications.

These logs provide a comprehensive history of query activity, which is essential for both performance analysis and security auditing.

**Performance Metrics**: Houseware collects detailed performance metrics for each query, enabling the identification and resolution of performance bottlenecks:

- Resource Utilization: Tracks metrics such as CPU usage, memory consumption, and I/O operations for each query.
- Execution Plan Analysis: Analyzes the execution plan of each query to identify inefficiencies, such as suboptimal joins or missing indexes.
- Latency Metrics: Measures the response times and latency of queries to ensure they meet performance expectations.

***

# API-first Platform

Houseware is built with a "platform-first" approach, offering a robust and flexible foundation that can be extended to accommodate a wide range of use cases. The APIs are designed to support the Product teams' use cases via the Houseware UI, but are also extensible to build custom analytics interfaces, integrate with, or develop entirely new applications.

**All Use Cases, available via APIs**: Houseware provides a wide array of API endpoints that cover all essential product analytics use cases:

- **Event Tracking**: Endpoints to ingest and query user events in real-time, allowing for immediate visibility into user interactions.
- **Funnel Analysis**: APIs to create and analyze conversion funnels, helping teams understand user drop-off points and optimize conversion rates.
- **Retention Analysis**: Endpoints for building retention cohorts and tracking user engagement over time, aiding in the measurement of user stickiness and long-term engagement.
- **Cohort Analysis**: APIs to define, manage, and sync user cohorts based on behaviors and properties, enabling targeted analysis and personalized user experiences.
- **Advanced Use Cases**: Aside from the aforementioned use cases like "funnels", "retention", "cohorts", there are furthermore use cases that are available:
  - **Aggregations on Properties**: Perform advanced aggregations on event and user properties to derive detailed insights.
  - **First-time User Analysis**: Identify and analyze the first-time occurrence of specific events for users.
  - **User Activity Lookup**:  Retrieve detailed records of user activities for a specific user, searchable by a custom identifier
  - **Joins **: Execute complex queries that join events and entities for cross-functional product analysis.

<br />

**Ease of Integration**: Houseware APIs are designed to be easily integrated with your existing systems and applications:

- **Authentication**: Supports both API Key and JWT (JSON Web Token) authentication methods to secure access and ensure that only authorized users and applications can interact with the API.
- **Documentation**: Comprehensive and clear API documentation is provided to guide developers through integration, including example requests and responses, parameter descriptions, and use case scenarios.

To get started with the Houseware Platform API, refer to our detailed guide [here](https://docs.houseware.io/reference).

***

# Security

Houseware prioritizes security to provide a safe platform for viewing, exploring, and building your product analytics workflows. We adhere to global industry standards to ensure the highest level of consumer data protection.

- **Bring-Your-Own-Warehouse**: Houseware operates on a bring-your-own-warehouse model, where only user and application configuration data is stored by Houseware. All clickstream events and datasets remain within the customer's data warehouse, ensuring that sensitive data never leaves your controlled environment.
- **Governance**: Houseware implements a minimum-access policy, granting users only the permissions necessary to perform their tasks. Our multi-tenant architecture ensures complete segregation of data and execution environments between clients, providing robust data isolation and security.
- **SOC 2 Type II Compliance**: Houseware is SOC 2 Type II compliant, with annual renewals and rigorous security practices.

Read here to know more: [Houseware's Security and Compliance Principles](https://docs.houseware.io/docs/houseware-security-overview)

***

:rocket: By understanding these building blocks and leveraging Houseware’s API's flexibility, you can drive insightful and secure product analytics that adapt to your evolving business needs.
