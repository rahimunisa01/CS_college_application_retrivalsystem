### **Query 1**: *“MIT CS deadline Fall 2025”*

**Narrative**:  
The user is specifically looking for the application deadline for the MIT Computer Science master's program, targeting Fall 2025 enrollment. The user expects to see the official MIT program page that includes a deadline for Fall 2025. Results from other universities or those with deadlines for the wrong year or term are not considered relevant.

**Relevance Judgments**:

| Rank | Title                                  | Deadlines Found                                         | Relevance | Reason                                                                 |
|------|----------------------------------------|---------------------------------------------------------|-----------|------------------------------------------------------------------------|
| 1    | Stanford University - MSCS Deadlines   | Sept 23, Oct 7, Oct 31, Dec 16, 2025; Jan 9, 2026       | ❌         | Wrong school.                             |
| 2    | Carnegie Mellon University - MSCS      | Sept 3, Nov 19, Nov 26, Dec 10, 2025                    | ❌         | Wrong school.                                                         |
| 3    | University of Chicago - MSCS           | Dec 4, 2024; Feb 5, Jul 2, 2025; Jan 8, 2025            | ❌         | Wrong school, wrong focus (many are off-cycle or earlier).            |
| 4    | Brown University - MSCS                | Jan 15, 2025; May 1, 2025                               | ❌         | Wrong school.      |
| 5    | MIT - MSCS Deadlines                   | Sept 15, 2024; Dec 1, 2024                              | ✅         | Correct school. Although for Fall 2024, it's still the correct page.  |

**Notes**:  
- While MIT appears only at rank 5 with a low score (1.945), it is the most relevant result.
- Recency weighting may have pushed older deadlines down, despite the query clearly requesting a specific school.
- Future ranking improvements could include query expansion, relevance feedback, and snippet ranking based on metadata for exact institution matches to improve result positioning.

---

### **Query 2**: *“Ivy League MS application dates”*

**Narrative**:  
The user is looking for application deadlines specifically for Ivy League universities offering master’s programs in computer science. Relevant results should come from the eight Ivy League schools: Harvard, Yale, Princeton, Columbia, Cornell, University of Pennsylvania, Brown, and Dartmouth. Pages from non-Ivy institutions, regardless of their deadline information, are considered non-relevant.

**Relevance Judgments**:

| Rank | Title                                      | Deadlines Found                                           | Relevance | Reason                                                                 |
|------|--------------------------------------------|-----------------------------------------------------------|-----------|------------------------------------------------------------------------|
| 1    | Stanford University - MSCS Deadlines       | Sept 23, Oct 7, Oct 31, Dec 16, 2025; Jan 9, 2026         | ❌         | Not an Ivy League school.                                             |
| 2    | Carnegie Mellon University - MSCS          | Sept 3, Nov 19, Nov 26, Dec 10, 2025                      | ❌         | Not an Ivy League school.                                                     |
| 3    | University of Chicago - MSCS               | Dec 4, 2024; Feb 5, Jul 2, 2025; Jan 8, 2025              | ❌         | Not an Ivy League school.                                                   |
| 4    | UNC Chapel Hill - MSCS Deadlines           | Dec 10, 2024; Jan 9, 2025; Mar 11, 2025                   | ❌         | Not an Ivy League school.                                                   |
| 5    | University of Washington - MSCS Deadlines  | Mar 3, 2025; May 1, 2025                                  | ❌         | Not an Ivy League school.                                                  |

**Notes**:  
- All results returned by the search engine are currently non-relevant because none belongs to Ivy League institutions.
- This highlights a limitation in our system's current ranking logic: it does not yet incorporate university tier recognition.
- Future improvements could include adding metadata tags for university categories or enhancing query understanding to support institution-based filtering.

---


### **Query 3**: *“Deadlines after December 2024”*

**Narrative**:  
The user is intened to find the upcoming deadlines for master’s programs that occur strictly after December, 2024. This query is time-sensitive. Relevant results should contain explicit dates in 2025 or later. Results from the wrong year or with only early/expired deadlines are not useful.

**Relevance Judgments**:

| Rank | Title                                      | Deadlines Found                                           | Relevance | Reason                                                                 |
|------|--------------------------------------------|-----------------------------------------------------------|-----------|------------------------------------------------------------------------|
| 1    | Stanford University - MSCS Deadlines       | Dec 16, 2025; Jan 9, 2026; + more                         | ✅         | All deadlines are after Dec 2024.                                     |
| 2    | Carnegie Mellon University - MSCS          | Dec 10, 2025; Nov 19, Nov 26, Sept 3, 2025               | ✅         | One deadline (Dec 10, 2025) qualifies.                                |
| 3    | University of Chicago - MSCS               | Feb 5, Jul 2, 2025; Jan 8, 2025; Dec 4, 2024             | ✅         | Several deadlines are in 2025.                                        |
| 4    | UNC Chapel Hill - MSCS Deadlines           | Jan 9, Mar 11, 2025; Dec 10, 2024                        | ✅         | Includes valid 2025 deadlines.                                        |
| 5    | University of Michigan–Ann Arbor - MSCS    | Nov 24, Dec 9, 2024                                     | ❌         | All deadlines are before Jan 2025.                                    |

**Notes**:  
- The system generally performed well, successfully surfacing multiple programs with deadlines in 2025.
- The ranking reflects a positive correlation between recency and score, as Stanford and CMU appeared at the top.
- Our interface currently shows deadlines for the Coterminal Application at Stanford, but fails to extract or highlight the deadline for the main Master’s Application. This happened because the Master's deadline is listed as “TBD” on the website, and our extractor skips incomplete or non-date values. To address this, future improvements will include: Flagging “TBD” entries with the correct program label, even if no date is available; Enhancing table parsing to better distinguish between program types; Prioritizing primary programs like “Master’s Application” in result formatting, regardless of whether a date is present.
