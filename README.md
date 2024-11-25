# **Exploring Sales Analytics with SQL and Python**

## **Project Overview**
This project demonstrates the integration of Python and SQL for generating and analyzing sales data. It involves creating a synthetic dataset, inserting it into an SQL database, performing queries for business insights, and conducting exploratory data analysis (EDA) with Python to visualize trends and patterns.

---

## **Objectives**
### **Step 1: Dataset Generation**
- **Task 1: Dataset Creation**
  Generate a dataset of **200 rows** with the following attributes:
  - **Customer ID:** Unique ID ranging from 1001 to 1200.
  - **Customer Name:** Random names generated using `Faker`.
  - **Product ID:** Unique product ID from 1 to 20.
  - **Purchase Date:** Random dates within the last year.
  - **Quantity:** Random numbers between 1 and 10.
  - **Price per Unit:** Random prices between 10.00 and 1000.00.
  - **Region:** Random regions among "North," "South," "East," and "West."

- **Task 2: Dataset Insertion into SQL**
  - Create an SQL database (SQLite/MySQL).
  - Define a table schema corresponding to the dataset attributes.
  - Insert the generated dataset into the table.

---

### **Step 2: SQL Queries**
- **Task 3: Perform the Following Queries**
  1. **Total Sales by Region:** Calculate total sales per region (`quantity * price_per_unit`).
  2. **Top Products:** Retrieve the top 5 products by total sales.
  3. **Monthly Sales:** Calculate total sales for each month.
  4. **Customer Purchase Analysis:** Total amount spent by each customer.
  5. **Product Sales by Region:** List total sales of each product per region.

---

### **Step 3: EDA and Visualization**
- **Task 4: Retrieve Data into Python**
  - Use `pandas` and `sqlite3`/`mysql-connector` to load the SQL data into a DataFrame.

- **Task 5: EDA Tasks**
  - **Summary Statistics:** Compute mean, median, max, min, and standard deviation for `quantity` and `price_per_unit`.
  - **Sales per Region:** Analyze total sales by region.
  - **Top 5 Customers:** Identify the highest spenders.

- **Task 6: Visualizations**
  - **Bar Plot:** Visualize total sales per region.
  - **Pie Chart:** Show the proportion of sales for each product.
  - **Line Plot:** Plot monthly sales trends.
  - **Scatter Plot:** Explore the relationship between quantity and price per unit.

---

## **Technologies and Libraries Used**
- **Python Libraries:**
  - `pandas`: Data manipulation and analysis.
  - `numpy`: Numerical operations.
  - `Faker`: Random data generation.
  - `matplotlib` and `seaborn`: Data visualization.
- **SQL Database:**
  - SQLite or MySQL for data storage and query execution.
- **SQLAlchemy:** Simplified database interaction.

---

## **Setup and Execution**
1. **Run Dataset Generation Script**
   - Execute the Python script to generate synthetic data and populate the SQL database.

2. **Execute SQL Queries**
   - Use the provided SQL script to run queries and gather insights.

3. **Perform EDA**
   - Use the Python notebook/script to retrieve the data and conduct EDA tasks.

4. **Visualize Data**
   - Generate the required plots using Python's visualization libraries.

---

## **Key Insights**
1. **Regional Sales Trends:** Highlight sales dominance or trends across regions.
2. **Top Customers and Products:** Identify key revenue drivers.
3. **Sales Seasonality:** Analyze monthly sales patterns for strategic planning.
4. **Quantity vs. Price Analysis:** Examine correlations and purchasing behavior.

---

## **Deliverables**
1. **Python Script:** 
   - Dataset generation and SQL database insertion.
2. **SQL Script:** 
   - Queries for extracting meaningful insights.
3. **Python Notebook/Script:** 
   - Data retrieval, EDA, and visualizations.
4. **README File:** 
   - Detailed project explanation.

---

## **How to Run**
1. Install required libraries:
   ```bash
   pip install pandas numpy faker sqlalchemy pymysql matplotlib seaborn
   ```
2. Run the Python script for dataset creation and database insertion.
3. Use the SQL script to execute the queries.
4. Load the data into Python for EDA and visualizations.

---
