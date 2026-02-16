use ecom;
DELIMITER //
CREATE PROCEDURE get_delivered_orders()
BEGIN
    SELECT *
    FROM orders
    WHERE order_status = 'Delivered';
END //
DELIMITER ;

CALL get_delivered_orders();


DELIMITER //

CREATE PROCEDURE get_orders_by_customer_city(IN customer_city_name VARCHAR(50))
BEGIN
    SELECT *
    FROM orders
    WHERE customer_city = customer_city_name;
END //

DELIMITER ;

CALL get_orders_by_customer_city('Delhi');