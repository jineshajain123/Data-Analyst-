use ecom;
SELECT COUNT(*) 
FROM orders;

SELECT SUM(quantity * price_per_unit) AS total_revenue
FROM orders;

SELECT AVG(price_per_unit)
FROM orders;

SELECT MIN(price_per_unit), MAX(price_per_unit)
FROM orders;

SELECT customer_name, ROUND(price_per_unit, 0)
FROM orders;

SELECT UPPER(customer_name)
FROM orders;

SELECT LOWER(customer_name)
FROM orders;

SELECT customer_name, LENGTH(customer_name)
FROM orders;

SELECT CURRENT_DATE;

SELECT order_id, DATEDIFF(delivery_date, order_date) AS delivery_days
FROM orders;

SELECT *
FROM orders
WHERE YEAR(order_date) = 2025;