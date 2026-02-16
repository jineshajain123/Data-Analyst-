use ecom;
select * from employees;
alter table employees
add (
city varchar(20)
);
update employees 
set city = case
when emp_id = 1 then 'indore'
when emp_id = 27 then 'pune'
when emp_id = 28 then 'banglore'
end 
where emp_id in (1,27,28);

SELECT *
FROM employees
WHERE city IN ('Delhi', 'pune', 'Banglore');


SELECT *
FROM orders
WHERE customer_city IN ('Delhi', 'Mumbai', 'Bangalore');

SELECT *
FROM orders
WHERE payment_mode NOT IN ('Cash', 'UPI');

SELECT *
FROM orders
WHERE price_per_unit BETWEEN 1000 AND 10000;

SELECT *
FROM orders
WHERE price_per_unit NOT BETWEEN 1000 AND 10000;

SELECT *
FROM orders
WHERE customer_name LIKE 'A%';

SELECT *
FROM orders
WHERE product LIKE '%Table%';

SELECT *
FROM orders
WHERE city LIKE 'D_lhi';

SELECT *
FROM orders
WHERE category IN ('Electronics', 'Furniture')
AND price_per_unit NOT BETWEEN 5000 AND 20000;



