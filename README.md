# 🎵 Digital Music Store Analysis (SQL)

## 📌 Project Overview
This project analyzes the **Chinook Database** (a digital media store model) to answer critical business questions regarding **Revenue**, **Customer behavior**, and **Inventory management**. 

Using **Complex SQL Queries** via Python's `sqlite3` library, I extracted actionable insights to help the management team optimize their marketing strategies.

## 🛠️ Tech Stack
* **Database:** SQLite (Chinook DB)
* **Language:** SQL (Joins, Window Functions, Aggregations), Python
* **Libraries:** `pandas`, `sqlite3`

## 🔍 Key Business Questions & SQL Solutions

### 1. Where should we throw our next marketing event?
**Objective:** Identify the city generating the highest revenue.
* **SQL Skills:** `GROUP BY`, `ORDER BY`, `AGGREGATE FUNCTIONS (SUM)`
* **Insight:** **Prague** is the top-performing city, followed closely by Paris and Mountain View. The marketing budget should be allocated to the Czech Republic and France.

### 2. Which artists should we stock more of?
**Objective:** Determine top-selling artists to optimize inventory.
* **SQL Skills:** `MULTI-TABLE JOINS` (InvoiceLine → Track → Album → Artist)
* **Insight:** **Iron Maiden** is the #1 best-selling artist (140 sales). The store should prioritize Rock/Metal inventory over other genres.

### 3. Who are our VIP customers?
**Objective:** Calculate Customer Lifetime Value (CLV) for loyalty rewards.
* **SQL Skills:** `Joins`, `Calculated Fields`
* **Insight:** The top customer, **Helena Holý**, has spent $49.62 across 7 separate transactions.

## ⚙️ How to Run
1.  **Clone the repo:**
    ```bash
    git clone [https://github.com/Mridul711/Digital-Music-Store-Analysis-SQL.git](https://github.com/Mridul711/Digital-Music-Store-Analysis-SQL.git)
    ```
2.  **Run the Analysis:**
    ```bash
    python sql_project.py
    ```
    *The script will automatically download the database file if missing and generate 3 CSV reports.*
