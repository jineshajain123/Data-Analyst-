use ecom;
CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(150) UNIQUE,
    name VARCHAR(100) NOT NULL,
    age INT CHECK (age >= 18),
    department VARCHAR(50) DEFAULT 'General',
    salary DECIMAL(10,2) CHECK (salary > 0),
    joining_date DATE DEFAULT (CURRENT_DATE)
);
INSERT INTO employees (email, name, age, salary)
VALUES ('rahul@company.com', 'Rahul Khan', 16, 30000),
('pooja@company.com', 'Pooja Nair', 26, 50000),
('neha@company.com','neha', 24, 40000);