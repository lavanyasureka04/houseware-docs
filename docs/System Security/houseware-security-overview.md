---
title: "Houseware Security"
slug: "houseware-security-overview"
excerpt: "Houseware's security & compliance principles guide how we deliver our products and services, enabling people to simply and securely access the digital world."
hidden: false
createdAt: "Thu Aug 10 2023 11:26:45 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Mar 12 2024 15:01:36 GMT+0000 (Coordinated Universal Time)"
---
# Overview

Houseware is built to scale, but security always comes first. We aim to provide a secure platform to view, explore, and build your product analytics workflows. This document lists Houseware’s security practices and how you can reach a member of our security team if you have any questions.

Houseware has adopted global industry standards to ensure a high bar of consumer data protection. Our internal practices include the following:

- Houseware is S0C 2 Type II compliant. We actively maintain and renew it annually. Documentation for the same can be made available by writing to us at [security@houseware.io](mailto:security@houseware.io)
- The Houseware application effectively segregates user information, and stringent authentication and authorization measures safeguard access to your data.
- Houseware checks the changes made to the application at every step of its development. This includes conducting thorough architecture and stringent code reviews, both automated and manual.
- Houseware is cloud-hosted on Amazon Web Services, a highly secure and well-established environment.
- Houseware has many tools to support monitoring and event logging to minimize product outages for our customers like:
  - AWS cloud watch
  - Sentry

***

# Certifications

## SOC 2 Type 2 Certification

![](https://files.readme.io/0873ab6-socII_image.jpeg)


Houseware undergoes an annual SOC2 (Service Organization Control 2) Type 2 review by a qualified auditor, covering all the trust principles (Security, Confidentiality, and Availability) that apply to our operations. It ensures all our practices across different aspects of the business maintain the security and confidentiality of customer data. 

Houseware was audited by [Prescient Assurance](https://www.prescientassurance.com/), a leader in security and compliance certifications for B2B, SAAS companies worldwide. Prescient Assurance is a registered public accounting in the US and Canada and provides risk management and assurance services which include but are not limited to SOC 2, PCI, ISO, NIST, GDPR, CCPA, HIPAA, CSA STAR, etc.

> 👍 **Audit Results**
> 
> An unqualified opinion on a SOC 2 Type II audit report demonstrates to the CMD CTR, Inc.’s current and future customers that they manage their data with the highest standard of security and compliance.

You can ask for our audit reports on request while signing the NDA.

***

# Information Security

As a platform that connects with your warehouse and integrates with all your other precious data sources, we are committed to maintaining the highest forms of information security for our customers.

Our core information security principles are as follows:

1. **Ensuring Robust Security with a Feature-Rich Platform: **Strive to provide a platform that's not only full of useful features but also highly secure. All your systems should have strong protection to prevent any unauthorized access.
2. **Maintaining Reliable Operations: **Ensure the platform operates smoothly and dependably, with minimal downtime. Any disruptions could potentially expose data or impede user experience, hence we strive for reliable service.
3. **Promoting Continuous Improvement and audits:** The world of data security is always evolving, hence we strive to stay ahead of potential threats through:
   1. Regularly reviewing and updating our security practices
   2. Consistently assess our security measures to identify potential vulnerabilities or improvement areas.
   3. Keep customers informed about how their data is stored and protected.

## Practices Followed

Following are the security practices and guidelines which are strictly adhered to maintain security as a company value

### Secure Personnel

Houseware takes the security of its data and that of its clients and customers seriously and ensures that only vetted personnel are given access to their resources.

- All Houseware contractors and employees undergo background checks prior to being engaged or employed by us in accordance with local laws and industry best practices.
- Confidentiality or other types of Non-Disclosure Agreements (NDAs) are signed by all employees, contractors, and others who have a need to access sensitive or internal information.
- We embed the culture of security into our business by conducting employee security training & testing using current and emerging techniques and attack vectors.

### Secure Development

- All development projects at Houseware, including on-premises software products, support services, and our own Digital Identity Cloud offerings follow secure development lifecycle principles.
- All development of new products, tools, and services, and major changes to existing ones, undergo a design review to ensure security requirements are incorporated into the proposed development.
- All team members who are regularly involved in any system development undergo annual secure development training in coding or scripting languages that they work with as well as any other relevant training.
- Software development is conducted in line with [OWASP Top 10](https://owasp.org/www-project-top-ten/) recommendations for web application security.

### Secure Testing

Houseware deploys third-party penetration testing and vulnerability scanning of all production and Internet-facing systems on a regular basis.

- All new systems and services are scanned prior to being deployed to production.
- We perform penetration testing both by internal security engineers and external penetration testing companies on new systems and products or major changes to existing systems, services, and products to ensure a comprehensive and real-world view of our products & environment from multiple perspectives.
- We perform static and dynamic software application security testing of all code, including open-source libraries, as part of our software development process.

### Compliance

Houseware is committed to providing secure products and services to safely and easily manage billions of digital identities across the globe. Our external certifications provide independent assurance of Houseware's dedication to protecting our customers by regularly assessing and validating the protections and effective security practices Houseware has in place.

***

# Data Protection & Storage

## Data Protection

The Houseware application effectively segregates user information, and stringent authentication and authorization measures safeguard access to your data.

Houseware also offers customers the choice of hosting their data in our India- or US-based AWS environments.

## Cloud Security

Houseware Cloud provides maximum security with complete customer isolation in a modern, multi-tenant cloud architecture. It also leverages the native physical and network security features of the cloud service and relies on the providers to maintain the infrastructure, services, and physical access policies and procedures.

- All customer cloud environments and data are isolated using Houseware's isolation approach. Each customer environment is stored within a dedicated trust zone to prevent any accidental or malicious co-mingling.
- All data is also encrypted at rest and in transmission to prevent unauthorized access and data breaches. Our entire platform is also continuously monitored by dedicated, highly trained Houseware experts.
- We separate each customer's data and our own, utilizing unique encryption keys to ensure data is protected and isolated.
- Client’s data protection complies with SOC 2 standards to encrypt data in transit and at rest, ensuring customer and company data and sensitive information is protected at all times.
- We implement role-based access controls and the principles of least privileged access and review revoke access as needed.

> 🌟 Feature Highlight
> 
> **Secure Data Sharing**: Houseware uses the [secure data sharing feature](https://docs.snowflake.com/user-guide/data-sharing-gs) for organizations who use Snowflake as their data warehouse. 
> 
> It is a powerful feature that allows customers to share data with Houseware without copying or tranferring any data. Hence no extra storage is needed, and customer data is completely safe and separated from what is shared with Houseware.

## Data Encryption

Customer data stored within our systems is encrypted using Amazon’s built-in encryption services, which utilize AES-256. Encryption keys are managed via AWS KMS.

***

# Data Management & Access Control

### Access Control

The Admin Access Control helps customers invite users and organizations. Workspace owners can also define viewer and editor permissions to safeguard data access.

### SSO

Single sign-on is available to our customers on the enterprise plan. Houseware uses WorkOS, a modern API platform, to enable SSO on our platform. We support the following type of logins:

- Google
- Okta
- Microsoft

***

# Privacy

### Data Ownership

Houseware customers own the data. Houseware does not store any customer data and only connects with customer data sources like warehouse and other applications configured via admin permissions.

Houseware collects and analyzes data about its customers' use of its own platform, but that data does not include the data sent to the platform by its customers for analysis on their behalf.

### Access to customer accounts

To ensure prompt and effective service, Houseware can access customer accounts. The privacy of our customers is of the utmost importance to us, and the scope of this access is limited to:

1. Checking any bugs, issues, or requests around the Houseware platform
2. Working sessions with customers (under customer supervision)

***

# Contact

For more questions about security and compliance, please contact [security@houseware.io](mailto:security@houseware.io) or [aryan@houseware.io](mailto:siddhant@houseware.io)
