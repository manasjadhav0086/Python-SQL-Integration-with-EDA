# **Exploring Sales Analytics with SQL and Python**

## **Project Overview**
This project demonstrates how to integrate Python and SQL for creating, storing, and analyzing sales data. It involves generating synthetic data, performing SQL queries for actionable insights, and conducting Exploratory Data Analysis (EDA) with Python to reveal patterns and trends through visualizations.

---

## **Objectives**
### **Step 1: Dataset Generation**
- **Task 1: Dataset Creation**
  Generate a dataset with the following attributes:
  - **Customer ID:** Unique IDs from 1001 to 1200.
  - **Customer Name:** Random names generated using `Faker`.
  - **Product ID:** IDs from 1 to 20.
  - **Purchase Date:** Random dates from the last year.
  - **Quantity:** Random values between 1 and 10.
  - **Price per Unit:** Prices ranging from 10.00 to 1000.00.
  - **Region:** Randomly assigned as "North," "South," "East," or "West."

- **Task 2: Insert Data into SQL**
  - Define an SQL table schema matching the dataset attributes.
  - Populate the SQL database using Python.

---

### **Step 2: SQL Queries**
Perform the following queries:
1. **Total Sales by Region:** Calculate `quantity * price_per_unit` per region.
2. **Top Products:** Retrieve the top 5 products by total sales.
3. **Monthly Sales:** Calculate monthly total sales.
4. **Customer Analysis:** Find the total amount spent by each customer.
5. **Regional Product Sales:** Show product-wise sales for each region.

---

### **Step 3: Exploratory Data Analysis (EDA)**
- **Retrieve Data to Python:**
  - Use libraries like `pandas` and `sqlite3`/`mysql-connector` to load data into a DataFrame.

- **EDA Tasks:**
  - **Summary Statistics:** Compute mean, median, max, min, and standard deviation for `quantity` and `price_per_unit`.
  - **Sales by Region:** Summarize total sales for each region.
  - **Top Customers:** Identify the 5 highest-spending customers.

- **Visualizations:**
  - **Bar Plot:** Total sales per region.
  - **Pie Chart:** Proportions of sales by product.
  - **Line Plot:** Monthly sales trends.
  - **Scatter Plot:** Relationship between quantity and price per unit.

---

## **Technologies and Libraries**
- **Python:** For data generation, analysis, and visualization.
  - `pandas` for data manipulation.
  - `numpy` for numerical operations.
  - `Faker` for synthetic data generation.
  - `matplotlib` and `seaborn` for plotting.
- **SQL:** SQLite/MySQL for data storage and querying.
  - `SQLAlchemy` for database interaction.

---

## **Setup Instructions**
1. Install necessary Python libraries:
   ```bash
   pip install pandas numpy faker sqlalchemy pymysql matplotlib seaborn
   ```
2. Run the dataset generation script to populate the SQL database.
3. Execute the SQL script for queries.
4. Load the data back into Python for analysis and visualization.

---

## **Sample Visualizations**
### **Bar Plot:** Total Sales by Region  
![Bar Plot](https://github.com/user-attachments/assets/278390be-ba29-4b75-bdaa-cfd1a003ef42)

### **Line Plot:** Monthly Sales Trends  
![Line Plot](https://github.com/user-attachments/assets/e8760166-ade8-4939-8f59-a3623c111371)

### **Pie Chart:** Sales Proportion by Product  
![Pie Chart](https://github.com/user-attachments/assets/e0d752c6-8ad3-4ea4-98b7-ad5d0b95e53f)

### **Scatter Plot:** Quantity vs. Price Relationship  
![Scatter Plot](https://github.com/user-attachments/assets/3c36412b-2be1-40cf-8ccb-96b49f5d820e)

---

## **Insights**
1. **Regional Trends:** Certain regions dominate sales, providing guidance for resource allocation.
2. **Top Products:** High-demand products drive revenue; focus marketing on these items.
3. **Seasonality:** Monthly trends highlight peak sales periods.
4. **Pricing Patterns:** Analyzing quantity vs. price helps understand customer purchasing behavior.

---

## **Deliverables**
- Python scripts for dataset generation and SQL integration.
- SQL script for queries.
- Jupyter notebook or Python script for EDA and visualizations.
- A detailed README for project setup and usage instructions.

---

## **Author**
[Manas Jadhav]  
For any questions or feedback, feel free to reach out!  
