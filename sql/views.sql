use ecom;
CREATE VIEW delivered_orders AS
SELECT order_id,
       customer_name,
       customer_city,
       product,
       price_per_unit,
       order_date
FROM orders
WHERE order_status = 'Delivered';

SELECT *
FROM delivered_orders;

UPDATE delivered_orders
SET price_per_unit = price_per_unit + 500
WHERE order_id = 1;

-- DROP VIEW delivered_orders;