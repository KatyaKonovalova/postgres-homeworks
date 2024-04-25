-- SQL-команды для создания таблиц

CREATE TABLE customers
(
	customer_id char PRIMARY KEY,
    company_name varchar(50),
    contact_name varchar(100)
);

CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
    first_name varchar(50),
    las_name varchar,
    title varchar(100),
    birth_date date,
    notes text
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id varchar,
	employee_id int,
	order_date date,
	ship_city varchar(50)
);

ALTER TABLE orders
ALTER COLUMN customer_id SET DATA TYPE varchar,
ADD CONSTRAINT customer_fk FOREIGN KEY (customer_id)
REFERENCES customers(customer_id),
ADD CONSTRAINT emploeey_fk FOREIGN KEY (employee_id)
REFERENCES employees(employee_id);