## Master’s Program Deadline Search Engine

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

- program or keyword
- intake term
- specific time filter
- school ranking
- institution type
- urgency

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

The expected number of relevant results varies depending on query type and user intent:

For general queries (e.g., “CS Master’s deadlines”), users typically expect around 5 results that cover a range of institutions.

For more specific or filtered queries (e.g., by term, specific university, or ranking), users may expect fewer but more precisely matched results.

Although our interface consistently displays the top 5 ranked results, we include relevance scores to help users interpret how well each result matches their query. This allows users to quickly assess whether a result is a strong match or only loosely related.

---

### **1.4 Result Organization**

Results in our system are presented as a ranked list, with the ranking determined by a combination of BM25 relevance scoring and recency-based weighting. This prioritizes documents that both match the query terms semantically and include more recent application deadlines, which are often more relevant and actionable for users.

In our system, results are ranked based on a combination of three key factors:

BM25 Relevance Score:
The core ranking signal comes from BM25 scoring, computed using bm25.get_scores(query_terms). This score captures the lexical relevance between the query terms and the content of each document.

Recency Weight:
Since application deadlines are time-sensitive, we extract all recognizable date strings from each document and compute a recency-based weight. The most recent deadline is used, and its score is decayed exponentially by the number of days from the current date:
  ```python
  weight = math.exp(-decay * days_old)
  ```
This ensures that more recent or upcoming deadlines are favored in the ranking.

Each result includes:
- Program name
- Institution name
- Application deadline
- A relevance score to indicate confidence
- A screenshot is stored during scraping, aiding manual verification

---

### **1.5 Evaluation Metrics**

To evaluate our system, we consider:
- **Precision@k**: How many of the top-k results are truly relevant. This is particularly important for our use case, since users often only examine the top few results. 
- **NDCG@k**: Measures ranking quality. In our task, deadlines that exactly match the query intent should be prioritized, so graded relevance and rank position matter.
- **Recall**: Proportion of all relevant documents retrieved. This is useful for general queries.

Due to the exploratory nature of the task and lack of a gold-standard dataset, our evaluation relies on manual relevance judgments.

---

### **1.6 Implementation and Performance Analysis**

Our system consists of several components:

- `prepare_urls.py`: Initializes and stores a list of university program URLs for CS master's application pages in JSON format.
- `scrape_deadlines.py`: Uses Selenium to crawl university admissions pages, render dynamic content, and extract text containing application deadlines for CS master's programs.
- `indexer.py`: Loads the scraped university deadline documents from JSON, processes their text, and builds a BM25 index using rank_bm25. This index enables efficient retrieval of documents based on query term relevance.
- `search.py`: Implements document ranking using BM25 and recency-based weighting. A legacy TF-IDF implementation is included but commented out.
- `app.py`: Provides a Streamlit-based web interface for users to enter queries and view ranked application deadline results.

We tested the crawler on 30 program pages and achieved a scraping success rate of 100%. The search engine returns top results in under 1 second, even with basic infrastructure.

---

### **1.7 Completed Milestones**

According to our grading contract, we successfully completed the following milestones in building and evaluating our custom information retrieval system:

- **Web crawler to collect real-world data**  
  We developed a headless browser-based crawler using Selenium to extract live deadline-related information from official university websites. The content is parsed and stored in a structured format within docs.json, forming the core dataset for indexing and retrieval. We also implemented automatic screenshot saving to support debugging and manual validation.

- **Custom search engine with ranking support**  
  Our search engine ranks results using a combination of BM25 relevance scoring and recency-based weighting. BM25 ensures that results match the query terms semantically, while recency weighting prioritizes application deadlines that are more current or upcoming. This hybrid ranking model helps surface the most relevant and timely results for users planning their applications.

- **Frontend web interface for user interaction**  
  We implemented a fully functional web interface using Streamlit. Users can enter natural language queries and receive a ranked list of application deadlines. Each result includes the program title, institution name, and extracted deadlines in a human-readable format. The interface is responsive and easy to use, designed for international students and applicants with varying levels of technical experience.

- **Relevance judgment and performance analysis**  
  We evaluated our system using a set of manually crafted queries reflecting real user needs. For each query, we performed relevance judgments on the output and documented both successful matches and limitations. Our findings are summarized in a report, along with proposed improvements.

---

### **1.8 Team Member Contributions**

- **Danchen He**: Project report, testing search queries for evaluation
- **Rahimunisa Begum**: Initial Setup, Webscraping the college websites, streamlit UI
- **Colin Linehan**: BM25 retreival with recency weight

---

Github: https://github.com/rahimunisa01/CS_college_application_retrivalsystem.git