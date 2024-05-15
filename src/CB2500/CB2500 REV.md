# CB2500 Information Management - Review

## 1. Importance of IM

### 5 Laws of Technology

- **Moore's Law**: The number of transistors on an integrated chip doubles every 18 months. (Computing power)
- **Metcalfe's Law**: The value of a network is proportional to the square of the number of users. (Network effect)
- **Nielsen's Law**: Network connection speeds for high-end users will increase by 50% per year. (Bandwidth)
- **Kryder's Law**: The storage density on magnetic disks is increasing at an exponential rate. (Storage)
- **Bell's Law**: New classes of computers establish a new industry each decade. (Innovation)

### Jobs and Skills

- **Marketable Skill**:
    - **Abstract reasoning**: create a model and representation
    - **System thinking**: understand components and their interactions
    - **Collaboration**
    - **Ability to experiment**

### MIS

Use → Manage → Achieving Strategies

- **Use** (general employees): TPS (Transaction Processing System)
- **Manage** (middle managers): MIS (Management Information System), DSS (Decision Support System), ES (Expert System), AI (Artificial Intelligence)
- **Achieving Strategies** (top managers): EIS (Executive Information System)

#### Components of IS

**Hardware, Software, Data, Procedures, People**

IS = IT + procedures + people

| Profession | Certification Institution | Certificate |
| --- | --- | --- |
| Project Managers | PMI | PMP |
| Business Analysts | SAS |
| IS Auditors | ISACA | CISA |

## 2. Business Process

**Business Process**: A network of activities for accomplishing a business function.

Process quality is measured by **effectiveness** and **efficiency**.

- **Effectiveness**: enables the organization to accomplish its strategy
- **Efficiency**: ratio of benefits to costs

### BPMN

- Thin Circle: Start
- Thick Circle: End
- Rectangle: Activity
- Rectangle with Plus: Sub-process
- Parallelogram: Data Repository (Database)
- Diamond: Decision
- Solid Line: Control Flow
- Dotted Line: Data Flow

### Quality Information

**Information** is

- knowledge derived from data (= recorded facts or figures)
- data presented in a meaningful context
- processed data

Characteristics of **Quality Information**: **STRAW**

- Just barely **S**ufficient
- **T**imely
- **R**elevant
- **A**ccurate
- **W**orth its cost

## 3. Organizational Strategy

**Industry Structure → Competitive Strategy → Value Chains → Business Processes → Information Systems**

### Porter's Five Forces

- Competitive Forces
    - **Existing Rivarly**
    - **Threat of New Entrants**
    - **Threat of Substitutions**
- Bargaining Power
    - **Bargaining power of suppliers**
    - **Bargaining power of customers**

### Competitive Strategies

- **Cost Leadership**
- **Differentiation**
- **Cost Focus**
- **Differentiation Focus**

### Value Chain

**Value chain**: a network of value-creating activities

- **Primary Activities**
    - Inbound Logistics
    - Operations
    - Outbound Logistics
    - Sales and Marketing
    - Customer Service
- **Support Activities**
    - Procurement (raw materials)
    - Technology
    - Human Resources
    - Firm Infrastructure (administration, legal, finance)

Each business process implements value chains or portions of value chains.

Each value chain is supported by one or more business processes.

### Competitive Advantage

- **Product Implementations**
    - Create
    - Enhance
    - Differentiate
- **Process Implementations**
    - Lock in customers
    - Lock in suppliers
    - Raise barriers to market entry
    - Establish alliances
    - Reduce costs

## 4. Database

### Software

- Categories
    - **Horizontal-market applications**
    - **Vertical-market applications**
    - **One-of-a-kind applications**
- Sources
    - **Off-the-shelf**
    - **Off-the-shelf with alterations**
    - **Custom-developed**

### Database

**Database**: a self-describing collection of integrated records

- Database = Files (tables) + Relationships between rows + Metadata (data about data)
- Table = row (record) + column (field)
- **Primary key**: a (or a group of) column(s) that uniquely identifies a row
- **Foreign key**: the primary key of another table that creates a relationship

**Entity-Relationship Data Model**

- Entity: something users want to track
- Attribute: characteristic of an entity
- Relationship: association between entities (types: one-to-one, one-to-many, many-to-many)

**Normalization**: the process of converting a poorly structured table into two or more well-structured tables

- Goal: construct tables with data about a single theme or entity
- Purpose: to minimize data integrity problems
- Issue: can be slower to process. The best design depends on the user's needs.

**Data Integrity Problem**: only occurs when data is duplicated

### DBMS

**DBMS**: a program used to create, process, and administer a database

- User → Database Application → DBMS → Database
- 4 operations: **Read, Insert, Modify, Delete**

## 5-6. Business Intelligence

### Smart Banking

7 features of smart banking:

- Balance sheet efficiency
- M&A
- **Growth**: Investing in customer analytics, improve customer experience, learn from non-banking tech companies
- **Payments transformation**:specalized promotions and services, differentiated customer experience
- **Compliance and risk management**: Incorporate risk management into performance management and employee training
- **Data management**: Central regulatory management office, chief data officer
- **Cybersecurity**

3 types of e-payment:

- Credit card
- **Direct debit**: FPS, PPS
- **Stored Value Facilities** (SVF): Octopus, Alipay
    - A government-licensed third-party digital wallet

### Business Intelligence

BI refers to technologies, applications, and practices for the collection, integration, analysis, and presentation of business information.

BI supports decision making. Also known as **Data-Driven Decision Support System**.

Data → BI Application → Knowledge Worker → Decision

Typical uses of BI:

- Identify changes in purchasing patterns (life event marketing)
- Market basket analysis (cross-selling)
- BI for entertainment (Netflix, Amazon)
- Predictive policing

### Data Warehouse

**Big Data**: data defined by four Vs

- **Volume**: large amounts of data (petabytes)
- **Velocity**: rapid analysis of streaming data
- **Variety**: different forms of data
- **Veracity**: uncertainty of data

**ETL**: Extract, Transform, Load

Data sources (Operational, Purchased, Social Data) → ETL → Data Warehouse → BI Tools

Comparing Operational DB, Data Warehouse, and Data Mart:

- Scope
    - Operational DB: day-to-day operations
    - Data Warehouse: many subjects across the enterprise
    - Data Mart: single subject for a single department
- Data
    - Operational DB: detailed OLTP (Online Transaction Processing)
    - Data Warehouse: detailed OLAP (Online Analytical Processing)
    - Data Mart: summarized OLAP
- Source
    - Operational DB: internal operations
    - Data Warehouse: multiple internal and external sources
    - Data Mart: subset of data warehouse
- Model
    - Operational DB: normalized, relational
    - Data Warehouse: denormalized (feeds dimensional model)
    - Data Mart: denormalized, dimensional
- Time span
    - Operational DB: current
    - Data Warehouse: historical (years)
    - Data Mart: historical (months)
- Purpose
    - Operational DB: day-to-day operations
    - Data Warehouse: decision support
    - Data Mart: decision support for a specific group

### BI Techniques

- **Multidimensional Data Analysis**: OLAP
    - **Dimension**: an attribute of a cube
    - **Cube**: multi-dimensional array of data
    - Slicing: with one dimension fixed
    - Dicing: with multiple dimensions fixed
    - Rolling up: summarizing data
    - Drilling down: viewing data at a more detailed level
- **Cluster Analysis**: divides information set into mutually exclusive groups
    - Intra-cluster similarity
    - Inter-cluster differences
- **Association Detection**: reveals the relationship between variables
    - Market basket analysis

### Project Management

Project Management Professional (PMP) certification issued by PMI

Domain knowledge:

- **Initiating** the project
    - Assess project, risk and benefit analysis
    - Develop project charter
    - Meet with sponsors (internal or external)
- **Planning** the project
    - Assess requirements, constraints, assumptions
    - Define scope
    - Develop schedule, budget, HR plan
- **Executing** the project
    - Acquire resources
    - Execute tasks
    - Implement approved changes
- **Monitoring and Controlling** the project
    - Measure performance
    - Ensure deliverables meet quality standards
- **Closing** the project
    - Obtain final acceptance
    - Transfer ownership and formal closure

5 stages in SDLC (Software Development Life Cycle):

- **System Definition** - (project plan) ->
- **Requirements Analysis** - (approved user requirements) ->
- **Component Design** - (system design) ->
- **Implementation** - (system) ->
- **System Maintenance**

### Change Management

**Change management** is a vital component of IS development and implementation projects, to increase the chances of success.

Common issues:

- Resistance to change
- Organizational culture
- Stakeholder management

5 steps in change management:

**Set and agree on objectives** → **Devise plans** → **Implement** → **Monitor** → **Review**

Challenges in system development:

- Requirement is hard to define
    - Solution: requirement analysis (PM use diagrams to illustrate key features, supplement with detailed specifications)
- Changing requirements
    - Solution: PM determine what changes can be handled within resource constraints
- Scheduling and budgeting difficulties
    - Solution: PM report ROI
- Changing technology
    - Solution: PM carry out impact analysis to determine whether to adopt new technology
- Diseconomies of scale
    - Solution: PM plan for team size and timelines

## 7-8. Social Media

**SMIS**:

- Use of IS to support sharing of content among networks of users
- enables communities (= people related by common interests)

3 SMIS roles: **Social Media Providers**, **Users**, **Communities**

5 components of SMIS:

- **Hardware**: (SMP) servers, data centers
- **Software**: (SMP) application, DBMS, analytics
- **Data**:
    - (SMP) content and connection data storage
    - (Users/Communities) connection data, user-generated content
- **Procedures**: (Users/Communities) create and manage content
- **People**

Note: connection data = system-generated data about relationships (likes, shares, comments)

### Organizational Strategy with SMIS

- **Sales and Marketing**: CRM; each customer actively creates a relationship with the firm
    - Downside: loss of credibility, poor public relations
- **Customer Service**: customers can help each other
    - Downside: loss of control over P2P communication
- **Inbonud and Outbound Logistics**: solutions to supply chain problems
    - Downside: loss of privacy
- **Manufacturing and Operations**:
    - (external with customers) crowdsourcing
    - (internal) ESN (Enterprise Social Network)
- **Human Resources**: evaluate job candidates
    - Downside: forming erroneous opinions

### Social Capital

**Social capital**: investment in social relations with the expectation of returns in the marketplace

Social captial = social network size × relationship strength × resources in the network

Value of social capital for individuals:

- **Information**: opportunities, awareness, alternatives
- **Influence**: influence decision-makers
- **Social Credentials**: linked to influential people
- **Reinforcement**: support personal and professional identity

Value of social capital for organizations:

- Increase strength of relationships
    - continuing and frequent interactions would strengthen relationships
- Connect with people with more resources
    - resources must be relevant

### SM Revenue Models

- **Advertising**: pay-per-click, pay-per-conversion
- **Freemium**: basic services free, premium services paid
- **Sales**: Apps and virtual goods, affiliate commissions, donations

### SM and Strategic Goals

3 steps in developing SMIS:

- Create relationships with customers, employees, and partners
- Transform organization-centric interactions to mutually beneficial relationships
- Align with organizational strategy

Social media plan development:

1. define your goals
2. identify success metrics
3. identify target audience
4. define your value
5. make personal connections
6. gather and analyze data

Goals:

- Increase brand awareness
- Increase conversion rates (click-through rates)
- Increase website traffic
- Increase user engagement (interaction)

**Vanity Metrics**: metrics that don't improve decision-making

### ESN

**Enterprise Social Network**: a software platform that uses social media to facilitate cooperative work of people within an organization

McAfee's SLATES:

- Search
- Links (links to enterprise resources)
- Authoring (create content)
- Tags (folksonomy)
- Extensions (usage-based recommendations)
- Signals (user-subscribed notifications)

Successful ESN implementation:

- Strategy
- Sponsorship
- Support
- Success

### Digital Marketing

**Digital Marketing**: uses digital media to develop communication and exchanges with customers

Compared to traditional marketing:

- More measurable
- More dynamic and adjustable
- Higher conversion rates
- Cheaper

4 types of digital marketing:

- Social media ads (**retargeting**: display ads to users who have visited your website)
- Search engine marketing (SEO, PPC)
- Digital analytics (the process in tracking, monitoring, and measuring visitors' behavior)
- Qualification

## 9. IS Audit and Risk Management

### IS Audit

**COBIT**: Control Objectives for Information and Related Technology

COBIT is a reference framework by ISACA for IT governance and management

CISA (Certified Information Systems Auditor) is a certification issued by ISACA

Domain knowledge:

- **IS Auditing Process**: provide audit services with standards
    - Knowledge: relevant IT and business processes; laws and regulations
- **Governance and Management of IT**: assure leadership and organizational structure that support organizational strategies
    - Knowledge: Business Impact Analysis (BIA) and BCP, risk management
- **IS Acquisition, Development, and Implementation**: acquire, develop, test, and implement IS
    - Knowledge: SDLC, acquisition practices (horizontal, vertical, one-of-a-kind, open-source)
- **IS Operations and Business Resilience**: manage and operate IS
    - Knowledge: performance monitoring
- **Protection of Information Assets**: ensure confidentiality, integrity, and availability of information
    - Knowledge: monitoring and responding to security incidents; storing, retrieving, transporting, and disposing of information

### IS Threats

Cost (safeguard) vs. Risk (loss)

Elements of IS security:

- Threat: Initiator (person or organization) of an attack
- Vulnerability: opportunity for threats to gain access
- Safeguard: measure taken to block a threat from obtaining an asset
- Target: asset desired by the threat

Sources of threats:

- Human error
- Computer crime
- Natural disasters

5 types of security loss:

- **Unauthorized data disclosure**
    - pretexting (pretending to be someone else), phishing (pretending to be a trustworthy entity), sniffing (intercepting computer communications), hacking
- **Incorrect data modification**
- **Faulty service** (incorrect system operation)
    - usurpation (replace legitimate applications with malicious ones)
- **Denial of service** (DoS)
- **DDoS attack** (Distributed DoS)
    - flooding a network with many requests

### IS Safeguards

- **Technical Safeguards** (hardware and software)
    - Identification and authentication
    - Encryption
        - symmetric (same key for encryption and decryption)
        - asymmetric (public and private key)
    - Firewalls
        - internal firewalls (block LAN traffic)
        - perimeter firewalls (block traffic between internal and external networks)
    - Malware protection
        - Virus, spyware, adware
    - Design for secure applications
- **Data Safeguards**
    - Data rights and responsibilities
        - **Data administration**: organization-wide function developing data policies and enforcing data standards
        - **Database administration**: function that pertains to a particular database (ERP, CRM)
    - Passwords
    - Encryption
    - Backup and recovery
- **Human Safeguards** (procedures and people)
    - Position definition (separate duties and authorities, least privilege)
    - Hiring and screening
    - Dissemination and enforcement
    - Termination

> •	_________________________ and _________________________ are the organization units responsible for data safeguards, which is aimed at protection against _________________________________.

Answer: Data administration, database administration, security threats

### BCP

**Business Continuity Planning**: a plan to enable business to continue offering critical services and survive a disastrous interruption.

BCP requires rigorous planning and commitment to resources.

Role of IS auditors in BCP:

- Identify critical services
- Help planning for resources and procedures for recovery in the shortest possible time

### Information Ethics

- **Copyright**: the legal protection afforded an expression of an idea
- **Fair Use Doctrine**: allows limited use of copyrighted material without permission
- **Pirated Software**: Unauthorized use, reproduction, distribution, or sale of copyrighted software
- **Counterfeit Software**: Software that is manufactured to look like the real thing and sold as such

Mitigation of ethical problems: Governament laws + Personal Data (Privacy) Ordinance

Organizational policies:

- Ethical computer use policy
- Acceptable use policy
- Email privacy policy (employer regularly monitors email)

## 10. Organizational Use of IS

Scope of IS:

- Personal
- Workgroup (10-100 users)
- Enterprise (100-1000 users)
- Inter-enterprise (1000+ users)

### Information Silos

**Information Silo**: the condition that exists when data are isolated in separated information systems

Issues:

- Data duplication, inconsistency (data integrity)
- Disjointed business processes
- Lack of intergeated (enterprise-view) information
- Decisions are isolated
- Increased expense

### SCM

**Supply Chain**: supplier → manufacturer → distributor → retailer → customer

**Bullwhip Effect**:

- Variability in size and timing of orders increases at each stage up the supply chain
- Large demand fluctuations force distributors, manufacturers, and suppliers to carry extra inventory
- Reducing the overall profitability of the supply chain

### CRM

**Customer Relationship Management**: a system (application + database + processes) that integrates customer-facing processes

Applications:

- Sales
- Customer support
- Relationship management
- Solicitation and lead management

Evaluate CRM and SCM:

- **Benchmarking**: a process of measuring performance against the best in the industry
- **Metrics**: the assessment criteria
- SCM metrics: Backorder, Customer order promised/actual cycle time, transmit time (= time to send an order)
- CRM metrics: Sales metrics, customer service metrics, marketing metrics

### ERP

**Enterprise Resource Planning**: a suite of applications, a database, and a set of inherent processes for consolidating business operations into a single, consistent computing platform

- Integrate all departments and functions
- Support enterprise-wide decision making

Advantages:

- A logical solution to incompatible applications
- Global information sharing and reporting
- Avoid fixing legacy systems

Components:

- Core ERP components
    - Accounting and finance
    - Production and materials management
        - demand forecasting, production scheduling, job cost accounting, quality control
    - Human resources
        - track employee information, assume compliance
- Extended ERP components
    - Business intelligence
    - Customer relationship management
    - Supply chain management
    - E-business

## 11-13. Disruptive Technologies

**Digital Darwinism**: implies that organizations that cannot adapt to the new demands placed on them for surviving in the information age are doomed to extinction

Disruptive technologies: a new way of doing things that initially does not meet the needs of existing customers

Examples of disruptive technologies: 3D printing, Internet of Things, Blockchain, AI, Robotics

**Long tail**: the tail of a typical sales curve. A large number of niche products are sold in small quantities, collectively making up a significant market share.

### Globalization

Collaboration tools:

- Internal collaboration:
    - Collaboration system: set of tools that supports the work of teams or groups by facilitating the sharing and flow of information
    - Knowledge management system: capturing, classifying, evaluating, retrieving, and sharing information assets in a way that provides context for effective decisions and actions
    - Benefit: enable generalist to do specialist work
- External collaboration: video conferencing

**Globalization**: the integration and interdependence of economic, social, cultural, and ecological facets of life, enabled by rapid advances in information technology

Globalization benefits:

- Worldwide opportunities (industry structure)
- International market and product differentiation (competitive strategy)
- Production and distribution anywhere (value chain + business processes)
- Work anytime, anywhere (business processes + IS)

Components of International IS:

- Hardware: sold worldwide
- Software: localized
- Data: choose a language for data description
- Procedures: reflect local laws, norms, and culture

Challenges of Globalization:

- ETL (Extract, Transform, Load) process: language problems
- Software design: internationalization
- Procedure design: multiple layers of apporval

Issues of global databases:

- A single database can only use one language
- Must use multiple databases
- Export and import data
- Slow transmission (solution: make distributed databases)

### Outsourcing

**Outsourcing**: a business practice that a company hires another company/individual to perform tasks

Advantages:

- Management advantages
    - Obtain expertise
    - Free management time
- Cost reduction
- Risk reduction (improve quality and service)

New tasks: quality control, risk management and contract management

Disadvantages:

- Loss of control
- Benefits outweighed by long-term costs
- No easy exit
    - Knowledge are in the hands of the outsourcer
    - Expensive and risky to change vendors

### Cloud

**Computer Network**: a collection of computers that communicate with one another over transmission lines or wirelessly
- **Personal Area Network (PAN)**: connects devices around a single person (~10m)
- **Local Area Network (LAN)**: connects computers in a small geographic area (~1km)
- **Internet**: network of networks using standardized communication protocols
- **Intranet**: internal network within an organization
- **Extranet**: extension of an intranet that is partially accessible to authorized outsiders
- **Protocol**: a set of rules and data structures for exchanging information
- **Virtual Private Network (VPN)**: a secure connection between two points on the internet

VPN provides secure, encrypted connections between private networks over the internet.

**Cloud**: Elastic leasing of pooled computer resources over the internet

- **Elastic**: automatically adjusts for unpredictable demand
- **Pooled**:
    - many users share the same physical hardware through virtualization
    - economies of scale (low average cost, web farm)

Advantages:

- Small capital requirements
- Speedy development
- Flexibility
- Known cost structure
- Cheap
- Disaster recovery

Disadvantages:

- Dependency on vendor
- Loss of control over data location
- Little visibility into true security and disaster recovery capabilities

Laws may enforce data location or to have physical control over data.

### Freeconomics

**Freeconomics**: the leveraging of digital technologies to provide free goods and services to customers as a business strategy for gaining a competitive advantage

How does freeconomics work?

- Marginal cost of production is zero
- The company influences price setting

Approaches:

- Advertising (providing PPC ads)
- Freemium (basic services free, premium services paid)
- Cross-subsidies (one product is sold at a loss to increase sales of another product)

**Internet of Things**: a world where interconnected, Internet-enabled devices or "things" can collect and share data without human intervention

**Fashion Tech**: a combination of appareal and accessories with smart technology

**Smart home**: a home equipped with technology to enable remote monitoring and control of appliances and systems

**Smart city**: a city integrating IoT and ICT (Information and Communication Technology) to enhance the quality and performance of urban services

**Nonfungible Token (NFT)**: a digital asset that represents ownership of a unique item or piece of content (VR interface, digital ownership, avatars)

**Metaverse**: a collective virtual shared space, created by the convergence of physical and virtual reality

## Tutorial Readings

Why some jobs are more vulnerable to automation:

- They are on the same level of routine, repetitive and predictable tasks
- They do not require marketable skills
- They can and will be outsourced to lowest bidder

Internet+ Technologies: Big Data, SMACIT (Social, Mobile, Analytics, Cloud, Internet of Things), AI, Blockchain

Internet+ Characteristics: Fan economy, seamless online & offline experience, customized experience, user-oriented pricing, QR shopping, seamless service with smart devices

SMACIT integrates existing retail channels. Keys in successful adoption of SMACIT:

- Integrate SMACIT into existing business processes
- Digitalize the business model to achieve business strategy
- Create new products and services to meet customer needs

Limitations of Big Data: Big data only reveals correlations, not causations.

Solution: Deep Data (= Big Data + Theory) - theoretical foundation, reliable in decision-making, more practical relevance

Pros of e-payment: cashless, convenient, efficient, higher turnover rate, interconnectivity (cross-platform and cross-border)

Cons of e-payment: security risks, privacy concerns, not easily transferable (from one platform to another), have to integrate with existing systems

Social commerce: the use of social media in the context of e-commerce transactions

- Buy now button
- Content-sharing and recommendation
- Shoppable posts and stories
- Social commerce plugins and apps
- Encourage user engagement (like, share, comment)

Digital analytics: the process of tracking, monitoring, and measuring visitors' behavior on a website (descrptive, diagnostic, predictive, prescriptive)

Importance: to understand and quantify the effectiveness of digital marketing campaigns; to focus on right customer segments

Metrics: vanity metrics (unique visitors, frequency of visits, time spent on site) vs. actionable metrics (geographic of customers, mobile vs. desktop, conversion rate)

Vanity metrics: no direct correlation to business strategy; misleading and can be manipulated; lack of actionable insights

SaaS: Software as a Service / AaaS: Analytics as a Service

Pros: cost-effective, scalable, flexible, easy to use, automatic updates / Cons: security concerns, limited customization, dependency on vendor

Globalization bring opportunities and challenges:

- Opportunities: market expansion, global stability, market equalization
- Challenges: market floods, global market chain reaction, internationalized competition

## Practice Questions

1. In 2016, the electronic wallet WeChat Pay HK was launched in Hong Kong by Tencent. WeChat Pay HK allows for direct money transfer from a user’s bank account to another’s. It facilitates cashless payment and acts as a replacement for a bank card. Users of WeChat Pay HK can simply use QR codes and make cashless transactions with ease. Unlike the Octopus card, another popular e-payment solution, which requires users to deposit money to it before use, WeChat Pay HK has no such requirement. 

Apart from partnering with many banks, WeChat Pay HK also links with thousands of local retail partners, such as McDonald's, KFC, PARKnSHOP, UA Cinema. Figure 1 shows a typical business process of a customer who uses WeChat Pay HK (linked with debit cards) to buy food in the restaurants.

(a) Is WeChat Pay HK a kind of SVF? Explain.

> WeChat Pay HK is a kind of Stored Value Facilities, which is used to store value for further payments. Since WeChat Pay HK allows linking with debit cards and paying through the platform, it can use stored value to do purchases.

(b) How does WeChat Pay HK facilitate banks in Hong Kong to catch up with TWO of the characteristics of smart banking that we discussed in class? Explain.

> **Growth**: WeChat Pay HK is a platform connecting banks and customers to provide seamless transactions. It integrates digital analytics and helps banks to understand customer behavior and preferences. Banks can use the data to improve customer experience and provide personalized services.

> **Payments transformation**: WeChat Pay HK provides a platform for banks to offer specialized promotions and services. Banks can differentiate themselves by offering unique services and promotions to attract customers.

> **Data management**: WeChat Pay HK can help banks to manage data effectively. Banks can use the platform to store, retrieve, and transport data securely. They can also use the platform to analyze data and make informed decisions.

> **Cybersecurity**: WeChat Pay HK can help banks to improve cybersecurity. Banks can use the platform to monitor and respond to security incidents. Cloud backup and recovery services can help banks to protect data and ensure business continuity.

(c) Referring to the typical business process of WeChat Pay HK in Figure 1 (Note: the names of data are omitted), identify and describe TWO major problems. Furthermore, give TWO suggestions with explanations that resolve the identified problems correspondingly so as to improve the existing business process.

> Problem 1: No password verification. There should be a password verification step before the payment is processed. This is to ensure that the user is the legitimate owner of the account and to prevent unauthorized transactions. Solution: Add a password or biometric verification step before the payment is processed. This minimizes the cybersecurity risk and ensures that the transaction is secure.

> Problem 2: Direct log-off after transaction failure. Since customers are expected to retry immediately after a transaction failure, the system should not log off the user immediately. Solution: Provides error messages and allows users to retry the transaction without logging off. This improves the user experience and reduces the time taken to complete the transaction.

(d) Tencent currently does not charge for the WeChat Pay HK service. It is speculated that it will launch some profit-making functions in the future. Knowing that WeChat Pay HK will capture a lot of customer and transaction data and that the company can make good use of them, suggest one business intelligence technique AND briefly describe how it can help Tencent make money. Plus, what data do you need for such a technique?

> **Data mining**: Data mining is a business intelligence technique that can help Tencent make money. By analyzing customer and transaction data, Tencent can identify patterns and trends that can be used to improve the service and increase revenue. For example, Tencent can use data mining to identify customer preferences and offer personalized promotions and services. The data needed for data mining includes customer data (e.g., demographics, preferences, behavior) and transaction data (e.g., purchase history, payment methods).

Recall: BI techniques include multidimensional data analysis, cluster analysis, association detection, and data mining.

- Multidimensional data analysis: Create a cube of data to analyze patterns and trends
- Cluster analysis: Divide information set into mutually exclusive groups
- Association detection: Reveal the relationship between variables

(e) To attract more people to use WeChat Pay HK, suppose the company plans to implement ascratch card function in the app. For every single purchase of HK$10 or above through WeChat Pay HK, a customer is eligible for an electronic scratch card and can win a big prize. To implement this new function, Tencent forms a project team and expects to finish the project within a month. Imagine you are the project manager. What task should you perform first? Describe and explain. We discussed five challenges to system development in class. Please describe TWO challenges for this project. Explain.

> The first task is to set and agree on objectives. This involves defining the goals of the project, identifying the success metrics, and aligning the project with the organizational strategy. By setting clear objectives, the project team can focus on the most important tasks and keep the project on track.

Recall: 5 stages in project management: initiating, planning, executing, monitoring and controlling, closing.

> Challenge 1: Requirement is hard to define. The scratch card function is a new feature that requires detailed specifications. This includes, what should be the prize, and the probability of winning.

> Challenge 2: Scheduling and budgeting difficulties. Since the project has a tight deadline, it may be difficult to allocate resources and manage the project within the budget. The project manager must carefully plan the schedule and budget to ensure that the project is completed on time and within budget.

Recall: 5 challenges in change management: requirement is hard to define, changing requirements, scheduling and budgeting difficulties, changing technology, diseconomies of scale.

2. John CHAN is the owner of Crown Honor, a logistics company based in Hong Kong. Crown Honor is specialized in offering logistics solutions in Guangdong – Hong Kong – Macao Greater Bay Area. As COVID-19 cases spread in Hong Kong and Mainland China from 2020, John must develop a Business Continuity Plan to protect his business. His company has a total of 50 heavy truck drivers and 20 officers.

(a) You are working in a consulting firm to provide risk management advice to John. Please help him evaluate FIVE potential impacts of disruptions to his company and staff.

> Impact 1: Loss of revenue. COVID-19 may cause a decrease in demand for logistics services, leading to a loss of revenue.

> Impact 2: Communication difficulties. Face-to-face communication may be limited due to social distancing measures, leading to communication difficulties both internally and externally.

> Impact 3: Longer delivery times. COVID-19 may cause delays in transportation and logistics, leading to longer delivery times.

> Impact 4: Increased costs. COVID-19 may lead to increased costs due to additional safety measures and precautions.

> Impact 5: Employee health and safety. COVID-19 may pose a risk to the health and safety of employees, leading to absenteeism and reduced productivity.

(b) In order to survive the challenge of COVID-19 without an approximate end date, John is considering outsourcing part of the IS services (e.g., maintenance and data storage) to external third parties. Please list and explain SIX potential threats that such a practice imposes on corporate governance.

> Threat 1: Unauthorized data disclosure. Outsourcing IS services may expose sensitive data to unauthorized access, leading to data breaches and privacy violations.

> Threat 2: Incorrect data modification. Outsourcing IS services may lead to incorrect data modification, leading to data integrity issues and inaccurate information.

> Threat 3: Faulty service. Outsourcing IS services may result in incorrect system operation, leading to system failures and disruptions.

> Threat 4: Loss of control. Outsourcing IS services may result in a loss of control over data and systems, leading to security risks and compliance issues.

> Threat 5: Long-term costs outweigh benefits. Outsourcing IS services do not benefit the organization in the long run, because the knowledge and expertise are in the hands of the outsourcer, while in-house staff may not have the necessary skills to manage the systems.

> Threat 6: No easy exit. Outsourcing IS services may make it difficult to change vendors or bring the services back in-house, leading to dependency on the vendor and lack of flexibility.

> Threat 7: Potential third-party risks. Should the outsourcer face financial difficulties or go out of business, the organization may face disruptions in services and data loss.

> Threat 8: Vendor management issues. Outsourcers do not necessarily handle data and systems in the same way as the organization, leading to potential conflicts and unnecessary work.

(c) What advice would you give to John to better safeguard their data and ensure that they can provide regular services to their customers in three different ways (Data safeguard, Technical safeguard, and Human safeguard)?

> Data safeguard 1: Implement encryption. Asymmetric encryption can be used to secure data in transit and at rest, ensuring that sensitive information is protected from unauthorized access.

> Data safeguard 2: Backup and recovery. Regularly backup data to an off-site location and test the recovery process to ensure that data can be restored in the event of a disaster.

> Technical safeguard 1: Implement firewalls. Firewalls can be used to block unauthorized access to the network and prevent malware from entering the system.

> Technical safeguard 2: Malware protection. Install antivirus software and keep it up to date to protect against malware and other security threats.

> Human safeguard 1: Position definition. Separate duties and authorities to prevent unauthorized access and ensure that employees only have access to the data they need to perform their job.

> Human safeguard 2: Training and awareness. Provide training to employees on data security best practices and raise awareness of the importance of data protection.

3. TAG Heuer, a wholly owned subsidiary of France’s LVMH, is one of the world’s most recognizable luxury watch brands founded in Switzerland. It is famous for luxury and innovative sports watches. The competition in the luxury watches market is intense and customers expect products to be avant-garde and show individual personalities. TAG Heuer’s competitors include Breguet, Rolex, Cartier, etc.

In 2020, TAG Heuer debuted the third generation of its Connected smartwatch. Powered with Wear OS by Google, wearers are given access to a wide selection of Google Play apps. This smartwatch also possesses various customizable features, such as voice-command, built-in calls, text, social media notification, and contactless payment service. Besides, wearers can adjust watch faces and displayable functions with TAG Heuer’s official app. The new product shows that technology and social connectivity can be seamless, glamorous, and effortless.

(a) Based on Porter’s competitive strategies, which strategy is the most suitable for TAG Heuer to gain competitive advantage over its rivals in the industry? Why? Name the strategy and justify.

> The most suitable competitive strategy for TAG Heuer is differentiation focus. While its competitors focus on traditional luxury watches, TAG Heuer has differentiated itself by introducing the Connected smartwatch, which combines luxury and technology. On the other hand, luxury smartwatches are a niche market, and TAG Heuer can focus on this segment to gain a competitive advantage.

(b) Suggest TWO Internet+ technologies that may help TAG Heuer. Give examples. How do your two suggested Internet+ technologies help create competitive advantages? Explain.

> Technology 1: Online shopping. TAG Heuer can implement online shopping to allow customers to purchase watches directly from its website. This technology helps create competitive advantages by providing convenience to customers and increasing sales.

> Technology 2: Augmented reality. TAG Heuer can use augmented reality to allow customers to try on watches virtually. This technology helps create competitive advantages by providing a unique and interactive shopping experience for customers.

Recall: Internet+ characteristics include Fan economy, seamless online and offline experience, customized experience, user-oriented pricing, QR shopping, seamless service with smart devices.

(c)  Assume that you are the social media coordinator of TAG Heuer. You are preparing a new marketing campaign to promote the new smartwatch to (potential) customers. In the lecture, we discussed six steps to develop a social media plan. The first step is to define a goal and the second step is to identify success metrics. What social media strategic goal is suitable to TAG Heuer? Explain.

> The social media strategic goal suitable for TAG Heuer is to increase website traffic. TAG Heuer is already a well-known luxury watch brand, and increasing website traffic can help drive more customers to its website to learn about the new smartwatch. By increasing website traffic, TAG Heuer can generate more leads and increase sales.

> Metrics: Website traffic quantity, frequency, duration and depth of visits; click-through rates.

Recall: 6 steps in developing a social media plan: define your goals, identify success metrics, identify target audience, define your value, make personal connections, gather and analyze data. (goal, metrics, audience, value, connections, data)

Recall: 4 social media strategic goals: increase brand awareness, increase conversion rates, increase website traffic, increase user engagement.

(d) Based on your answer in part (c), design a social marketing campaign to promote the new smartwatch, and describe your proposed IM/IS solution(s) to achieve the goal.

> Purchasing the new smartwatch will be rewarded with a chance to win a surprise prize. This campaign will increase website traffic and drive more customers to the website to learn about the new smartwatch. The IM/IS solution to achieve this goal is to implement a scratch card function on the website. The lucky draw is an economic incentive to attract customers to visit the website as well as retain existing customers.

(e) Apart from social marketing in (d), suggest TWO other digital marketing techniques that TAG Heuer can use AND explain how can they help promote the new smartwatch?

> Technique 1: Search engine marketing (SEM). TAG Heuer can use SEM to increase visibility and drive traffic to its website. Search Engine Optimization (SEO) can help improve the website's ranking in search engine results, while Pay-Per-Click (PPC) advertising can drive targeted traffic to the website.

> Technique 2: Social media advertising. TAG Heuer can use social media advertising to reach a wider audience and promote the new smartwatch. By targeting specific demographics and interests, TAG Heuer can increase brand awareness and drive traffic to its website. Retargeting can also be used to reach customers who have visited the website but have not made a purchase.

> Technique 3: Digital analytics. TAG Heuer can use digital analytics to track and measure the effectiveness of its marketing campaigns. By analyzing website traffic, user behavior, and conversion rates, TAG Heuer can optimize its marketing efforts and improve ROI.

Recall: 4 types of digital marketing: social media ads, search engine marketing, digital analytics, qualification.

4. Walmart China opened its first store in Shenzhen in 1996. Today it operates over 400 retail units nationwide. You are now applying for a summer internship position at Walmart China Home Office based in Shenzhen. Your prospective manager asks the following questions on global information management.

(a) Walmart has already built and now maintains mature information systems in the USA. To avoid reinventing the wheel, Walmart China has been referring to the IS design and implementation from its USA counterpart. Based on the five-component framework of information systems, please explain what you need to do regarding each component, except for the people component.

> Hardware: The hardware should be similar to the USA counterpart to ensure compatibility and interoperability. This includes servers, computers, and networking equipment.

> Software: The software should be the same as the USA counterpart to ensure consistency and standardization. This includes applications, databases, and operating systems. This facilitates data sharing and integration.

> Data: The data should be consistent with the USA counterpart to ensure data integrity and accuracy. Walmart China should collect more data including amount of sales, customer preferences, and inventory levels. Except for localized data, the data should be stored in the same format and structure.

> Procedures: The procedures should be aligned with the USA counterpart to ensure consistency and efficiency. However, the procedures should be adapted to Chinese laws, regulations, and business practices. This includes data management, security, and compliance procedures.

(b) Walmart China plans to build a payment solution into their mobile application to improve checkout experience for consumers. The management team is considering an IT outsourcing approach for this plan. Please identify TWO advantages and TWO risks associated with IT outsourcing that Walmart China may experience.

> Advantage 1: Cost reduction. As Walmart is not specialized in payment solutions, outsourcing the development of the payment solution can reduce costs and improve efficiency. This allows Walmart China to focus on its core business and strategic initiatives.

> Advantage 2: Focus on core competencies. IT outsourcing allows Walmart China to focus on its core competencies and strategic initiatives. By outsourcing non-core functions, Walmart China can free up resources and time to focus on its core business.

> Advantage 3: Increased efficiency. IT outsourcing can help Walmart China improve efficiency by leveraging the expertise and resources of external vendors. This can help Walmart China streamline processes and improve service delivery.

> Risk 1: Loss of control. IT outsourcing may result in a loss of control over the development and maintenance of the payment solution. This can lead to delays, quality issues, and security risks.

> Risk 2: No easy exit. IT outsourcing may make it difficult to change vendors or bring the services back in-house. The critical knowledge is on the vendor side but not in-house, which may lead to dependency on the vendor and lack of flexibility. Additionally, switching vendors may be costly and time-consuming.

(c) While Walmart was one of the first big international brands entering the Chinese market, it has had challenges and difficulties in the goal of dominating the grocery business given thevery different market environment from the US. Indeed, global project management is very difficult. Considering the case for Walmart (US and China), please describe TWO challenges of managing such global projects. Which organizational information systems would you recommend to help managing global projects? Name TWO and explain with valid reasons.

> Challenge 1: Project integration. Managing global projects requires coordination and integration across different regions, cultures, and time zones. This can be challenging due to differences in communication, collaboration, and decision-making processes.

> Challenge 2: Cost management. Managing global projects can be costly due to differences in labor costs, currency exchange rates, and regulatory requirements. This can lead to budget overruns and delays in project delivery.

> Challenge 3: Cultural differences. Managing global projects requires understanding and respecting cultural differences. This can be challenging due to differences in language, customs, and business practices.

> Solution 1: Enterprise Resource Planning (ERP) system. An ERP system can help Walmart manage global projects by providing a centralized platform for planning, tracking, and reporting on project activities. This can help Walmart streamline processes, improve collaboration, and ensure consistency across projects.

> Solution 2: Customer Relationship Management (CRM) system. A CRM system can help Walmart manage global projects by providing a centralized platform for managing customer relationships and interactions. This can help Walmart track customer preferences, improve customer service, and drive sales.

> Solution 3: Supply Chain Management (SCM) system. An SCM system can help Walmart manage global projects by providing a centralized platform for planning, sourcing, and delivering goods and services. This can help Walmart optimize its supply chain, reduce costs, and improve efficiency.
