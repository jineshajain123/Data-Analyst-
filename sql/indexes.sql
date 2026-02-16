use ecom;
CREATE INDEX idx_orders_city
ON orders (customer_city);
select * from orders;

SELECT *
FROM orders
WHERE customer_city = 'Delhi';

CREATE INDEX idx_orders_city_status
ON orders (customer_city, order_status);
-- Useful when queries filter by both city and order status.



