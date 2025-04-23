## **1. Master’s Program Deadline Search Engine**

### **1.1 Task Overview and Importance**

The goal of our project is to develop a search engine that helps students, especially international students and undergraduates preparing for graduate school, find application deadlines for master’s programs. While applying for graduate programs ourselves, we realized how difficult and stressful it is to track application timelines—especially since there is no centralized website that aggregates and orders deadlines across different schools and programs.

This lack of centralized information can lead to missed opportunities, rushed applications, and increased anxiety. By developing a dedicated information retrieval system, we aim to reduce this friction, enabling users to easily view, sort, and plan their applications based on up-to-date deadline data.

---

### **1.2 Nature of User Queries**

Through our own experience and user observations, we identified several recurring patterns in student queries related to Master’s program application deadlines. These queries vary in specificity, structure, and intent, and our search engine is designed to support them all. Below are examples of query types our system aims to support, along with their intended meaning:

- **General Topic Queries**
  - Example: *"Computer Science Masters Application Deadlines"*
  - Intent: The user is looking for any relevant application deadlines across universities offering computer science master’s programs. Expected results include official university pages, program requirement pages, and aggregated listings.

- **Term-Specific Queries**
  - Example: *"Computer Science Masters Application Deadlines Fall 2025"*
  - Intent: The user is looking for deadlines specific to the Fall 2025 intake. The system must filter out irrelevant entries from other terms.

- **Time-Based Queries**
  - Example: *"Computer Science Masters Application Deadlines After Christmas 2025"*
  - Intent: The user only wants deadlines that occur after a specific date. This requires not just keyword matching but temporal filtering based on parsed deadline values.

- **Application Stage Queries**
  - Example: *"Masters Deadlines for Early Applications"*
  - Intent: Users want to find priority or early decision deadlines and may expect the results to be sorted from earliest to latest. This highlights the importance of structured date extraction and sorting.

- **Program-Specific Queries**
  - Example: *"MSCS deadlines US"*
  - Intent: A broad query focusing on Master of Science in Computer Science programs offered in the U.S. The user expects a nationwide overview of relevant deadlines.

- **Season-Specific Queries**
  - Example: *"Master’s applications in US for Spring 2026"*
  - Intent: Filtered results limited to programs beginning in Spring 2026. This requires term recognition and dataset filtering.

- **School-Type-Specific Queries**
  - Example: *"Ivys MSCS US application dates"*
  - Intent: The user wants to view deadlines for Ivy League computer science programs only. The system must be able to identify and filter for a curated group of schools.

- **Rank-Based Queries**
  - Example: *"Computer Science Masters’ Program 2025 TOP 10 US News Universities Application Deadlines"*
  - Intent: The query targets deadlines from elite institutions ranked at the top of U.S. News rankings. The system must be capable of associating school rankings with deadline data.

- **Urgency-Focused Queries**
  - Example: *"Latest Computer Science Masters Application Deadlines"*, *"Master’s in computer science deadlines today"*
  - Intent: The user seeks the most urgent or up-to-date deadlines, possibly those due today or very soon. These queries require real-time filtering and freshness-aware ranking.

These examples demonstrate that supporting effective information retrieval in this domain requires handling a range of query types—from open-ended exploratory queries to precise, time-sensitive searches. Our system incorporates flexible keyword matching, date normalization, and filter-aware ranking to serve these diverse user needs.

From above, we observed that user queries often fall into the following categories:

- **By program or keyword** – e.g., *“Computer Science Masters Application Deadlines”*
- **By intake term** – e.g., *“Fall 2025”*, *“Spring 2026”*
- **By specific time filter** – e.g., *“Deadlines after Christmas 2025”*, *“Deadlines today”*
- **By school ranking** – e.g., *“Top 10 US News CS programs 2025 deadlines”*
- **By institution type** – e.g., *“Ivy League MSCS deadlines”*
- **By urgency** – e.g., *“Masters deadlines today”*, *“early application deadlines”*

These categories reflect the practical needs and time-sensitive nature of the graduate school application process, which our system is designed to address.

---

### **1.3 Relevant Results and Quantity Expectations**

The relevance of search results in our system is determined by how well they align with the user’s intent, the specific query issued, and the credibility and accuracy of the source. Based on relevance annotations across a wide range of queries, we identify a result as relevant if it satisfies the following criteria:

- It provides a valid application deadline for a Master’s program in Computer Science.
- It comes from an official university website.
- It specifically matches the intent of the query—such as program focus, intake term, or date range.
- It links to authoritative pages such as admissions websites, departmental program pages, or verified deadline summary portals.

#### **Examples of Relevant vs. Irrelevant Results**

For a query like "Computer Science Masters Application Deadlines", relevant results include:
- Northeastern University: Master’s Apply – Khoury College of Computer Sciences
- Harvard University: How to Apply
- NYU Computer Science: Master’s Program Admission

In contrast, irrelevant results include:
- Reddit forum discussions lacking official links.
- Archived or outdated deadlines from previous cycles.
- Results about unrelated programs (e.g., MBA, Ph.D., Data Science).

We also observed that relevance is not strictly binary. For example, a general “Graduate Application Deadlines” page might be partially relevant if it includes CS programs but lacks program specificity.

#### **Expected Number of Relevant Results**

The expected number of relevant results varies by query type and user expectations:

- For general queries, users expect about 10 results spanning diverse institutions.
- For filtered or specific queries (e.g., term-specific, Ivy-only, deadlines today), users prefer around 5 results that are more precisely tailored.

Below is a summary table illustrating expected result quantities by query type:

### Query Types and Expected Number of Relevant Results

| Query Category                                      | Example Query                                             | Expected Number of Relevant Results | Notes                                                                 |
|-----------------------------------------------------|-----------------------------------------------------------|-------------------------------------|-----------------------------------------------------------------------|
| General Program Search                              | Computer Science Masters Application Deadlines            | 10–20                                | Broad queries; users expect a variety of schools and sources         |
| Term-Specific                                       | Computer Science Masters Application Deadlines Fall 2025  | 8–12                                | Must filter by intake cycle                                          |
| Time-Filtered (e.g., after a date)                  | Deadlines after Christmas 2025                            | 5–10                                | Requires parsing and comparison of dates                             |
| Early Application Focus                             | Masters Deadlines for Early Applications                  | 5–10                                | Prioritize priority/early action deadlines                           |
| National Scope for a Specific Program               | MSCS deadlines US                                          | 8–15                               | Comprehensive results from many U.S. universities                    |
| Spring Intake                                       | Master’s applications in US for Spring 2026               | 5–10                                | Requires filtering by semester/start term                            |
| Ivy League Filtered                                 | Ivys MSCS US application dates                            | 6–8                                 | Must exclude non-Ivy institutions                                    |
| Top-Ranked Programs Only                            | 2025 TOP 10 US News Universities CS deadlines             | 6–10                                | Filtered by ranking; must ensure accuracy and exclusivity            |
| Latest/Recently Updated Deadlines                   | Latest Computer Science Masters Application Deadlines     | 5–10                                | Must retrieve the most up-to-date information                        |
| Urgent/Imminent Deadline Search                     | Master’s in computer science deadlines today              | 3–5                                 | Show only deadlines due today or within a day or two                 |

This relevance and quantity framework helps shape how we evaluate our system’s performance, how we design query handling and result filtering, and how we annotate and assess system output. Supporting accurate and appropriately scoped results is essential to ensuring usability and trustworthiness for student users who rely on this information to make high-stakes academic decisions.

---

### **1.4 Result Organization**

Results are displayed in a ranked list, sorted by deadlines by default. We also plan to support alternative sorting modes, such as alphabetically by university or grouped by country.

Each result includes:
- Program name
- Institution name
- Application deadline
- A clickable link to the original source

In addition to deadline-based ranking, we also plan to support alternative sorting and grouping options to accommodate different user preferences:

- Alphabetical order by university name: helpful for users who are already targeting specific institutions.

- Grouped by country or region: useful for international students considering geographical constraints or visa policies.

- Filterable by intake term, university tier, or deadline type (e.g., early decision, final round deadline).
---

### **1.5 Evaluation Metrics**

To evaluate our system, we consider:
- **Precision@k**: How many of the top-k results are truly relevant
- **NDCG** (Normalized Discounted Cumulative Gain): Measures ranking quality
- **Recall** (if using a known dataset): Proportion of all relevant documents retrieved

Due to the exploratory nature of the task and lack of a gold-standard dataset, our evaluation relies on manual relevance judgments.

---

### **1.6 Implementation and Performance Analysis**

Our system consists of several components:

- `prepare_urls.py`: Initializes the list of university and program URLs.
- `scrape_deadlines.py`: Crawls web pages and extracts deadline information using BeautifulSoup.
- `indexer.py`: Indexes the scraped data into a searchable format.
- `search.py`: Uses TF-IDF scoring to rank documents based on query relevance.
- `app.py`: Provides a Flask web interface for users to input queries and view ranked results.

We tested the crawler on around 100 program pages and achieved a scraping success rate of ~80%. The search engine returns top results in under 1 second, even with basic infrastructure.

---

### **1.7 Completed Milestones**

According to our grading contract, we successfully completed the following:
- Web crawler to collect real-world data
- Custom search engine with ranking support
- Frontend web interface for user interaction
- Relevance judgment and performance analysis
- Group collaboration with peer review

---

### **1.8 Team Member Contributions**

- **Member A (International Student)**: 
- **Member B (International Student)**: 
- **Member C (Undergraduate applying to grad school)**: 
