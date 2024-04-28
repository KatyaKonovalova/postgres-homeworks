-- SQL-команды для создания таблиц

CREATE TABLE customers
(
	customer_id char(5) PRIMARY KEY,
    company_name varchar(50),
    contact_name varchar(100)
);

CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
    first_name varchar(50),
    last_name varchar,
    title varchar(100),
    birth_date date,
    notes text
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id char(5),
	employee_id int,
	order_date date,
	ship_city varchar(50),
    CONSTRAINT customer_fk FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    CONSTRAINT employee_fk FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);