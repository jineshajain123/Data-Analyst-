use ecom;
SELECT customer_city,
       category,
       SUM(quantity * price_per_unit) AS total_sales
FROM orders
GROUP BY customer_city, category WITH ROLLUP;

SELECT category,
       COUNT(*) AS total_orders
FROM orders
GROUP BY category WITH ROLLUP;

SELECT
    customer_city,
    category,
    SUM(quantity * price_per_unit) AS total_sales
FROM orders
GROUP BY customer_city, category WITH ROLLUP;