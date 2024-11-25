CREATE DATABASE cust_product;

USE cust_product;

-- Total sales by region
SELECT region, ROUND(SUM(quantity * price_per_unit),2) AS total_sales
FROM purchases
GROUP BY region;

-- Total sales by product
SELECT product_id, Round(SUM(quantity * price_per_unit), 2) AS total_sales
FROM purchases
GROUP BY product_id
ORDER BY total_sales DESC
LIMIT 5;

-- Total sales by month
SELECT EXTRACT(MONTH FROM purchase_date) AS Month_, ROUND(SUM(quantity * price_per_unit),2) AS total_sales
FROM purchases
GROUP BY Month_
ORDER BY Month_;

-- Total amount spend by each customer
SELECT customer_id, customer_name, ROUND(SUM(quantity * price_per_unit),2) AS total_amount_spent
FROM purchases
GROUP BY customer_id, customer_name;

-- Total sales by region and product
SELECT product_id, region, SUM(quantity * price_per_unit) AS total_sales
FROM purchases
GROUP BY product_id, region
ORDER BY product_id ASC, total_sales DESC;
