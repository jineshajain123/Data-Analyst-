use ecom;
CREATE TABLE sellers (
    seller_id INT PRIMARY KEY AUTO_INCREMENT,
    seller_name VARCHAR(100) UNIQUE NOT NULL,
    city VARCHAR(50)
);
ALTER TABLE orders
ADD COLUMN seller_id INT;

ALTER TABLE orders
ADD CONSTRAINT fk_orders_seller
FOREIGN KEY (seller_id)
REFERENCES sellers(seller_id);

INSERT INTO sellers (seller_name, city)
VALUES ('TechWorld', 'Delhi');

INSERT INTO orders (seller_id, product, quantity, price_per_unit)
VALUES (1, 'Laptop', 1, 65000);

-- INSERT INTO orders (seller_id, product, quantity, price_per_unit)
-- VALUES (999, 'Laptop', 1, 65000);
select * from sellers;
select * from orders;
-- DELETE FROM sellers
-- WHERE seller_id = 1;