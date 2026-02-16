use ecom;
SELECT customer_city, COUNT(*) AS total_orders
FROM orders
GROUP BY customer_city;

SELECT category, 
       SUM(quantity * price_per_unit) AS total_sales
FROM orders
GROUP BY category;

SELECT customer_city, AVG(price_per_unit) AS avg_price
FROM orders
GROUP BY customer_city;

SELECT category, COUNT(*) AS total_orders
FROM orders
GROUP BY category
ORDER BY total_orders DESC;

SELECT customer_city, order_status, COUNT(*) AS count
FROM orders
GROUP BY customer_city, order_status;

SELECT customer_city, COUNT(*) AS total_orders
FROM orders
GROUP BY customer_city
HAVING COUNT(*) > 2;

