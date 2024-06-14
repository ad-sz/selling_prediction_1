create database data_base_1
use data_base_1

CREATE TABLE products (
    id_product INT PRIMARY KEY IDENTITY(1,1),
    category_product VARCHAR(255),
    name_product VARCHAR(255),
    unit_price DECIMAL(10, 2)
);

CREATE TABLE sales_transactions (
    id_transaction INT PRIMARY KEY IDENTITY(1,1),
    name_customer VARCHAR(255),
    name_product VARCHAR(255),
    quantity_sold INT,
    date_transaction DATE,
    category_product VARCHAR(255),
    unit_price DECIMAL(10, 2),
    transaction_amount DECIMAL(10, 2),
    region VARCHAR(255),
    id_seller VARCHAR(50)
);

CREATE TABLE sellers (
    id_seller VARCHAR(50) PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    date_employment DATE,
    date_birth DATE,
    region VARCHAR(255)
);

CREATE TABLE customers (
    id_customer VARCHAR(50) PRIMARY KEY,
    name_customer VARCHAR(255),
    date_added_customer DATE,
    region VARCHAR(255),
    id_seller VARCHAR(50)
);

CREATE TABLE inventory_status (
    id_product INT,
    quantity_in_stock INT,
    pallet_space VARCHAR(50),
    date_posting DATE,
    PRIMARY KEY (id_product, pallet_space)
);

select * from inventory_status