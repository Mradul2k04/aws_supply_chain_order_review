CREATE TABLE customers (
    customer_id VARCHAR(50) PRIMARY KEY NOT NULL check (customer_id ~ '^CUS-[0-9]{5}$'),
	customer_name VARCHAR(255) NOT NULL,
    customer_region VARCHAR(100) NOT NULL
);

CREATE TABLE products (
    product_id VARCHAR(50) PRIMARY KEY NOT NULL CHECK (product_id ~'PRO-[0-9]{5}$'),
    product_name VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL
);

CREATE TABLE suppliers (
    supplier_id VARCHAR(50) PRIMARY KEY NOT NULL CHECK (supplier_id ~'SUP-[0-9]{5}'),
    supplier_name VARCHAR(255) NOT NULL
);

CREATE TABLE orders (
    order_id VARCHAR(50) PRIMARY KEY NOT NULL CHECK (order_id ~'ORD-[0-9]{5}'), 
    customer_id VARCHAR(50) NOT NULL,
    product_id VARCHAR(50) NOT NULL,
    order_date TIMESTAMP NOT NULL,
	supplier_id VARCHAR(50) NOT NULL,
    order_qty INT NOT NULL  CHECK (order_qty > 0),
    
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

CREATE TABLE shipments (
    shipment_id VARCHAR(50) PRIMARY KEY NOT NULL CHECK (shipment_id ~'SHP-[0-9]{5}'),
    order_id VARCHAR(50) NOT NULL ,   
    shipping_date TIMESTAMP,
    delivery_status VARCHAR(50) NOT NULL CHECK (delivery_status IN ('Delivered', 'Pending', 'Delayed')),
	delivery_time_days INT NULL,        
    warehouse VARCHAR(50) NOT NULL,
    
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);



COPY orders(order_id, customer_id, product_id,supplier_id,order_date, order_qty)
FROM 'C:\file\order_data.csv'
WITH (FORMAT CSV, HEADER);


