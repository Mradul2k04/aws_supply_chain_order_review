--PRIMARY KEYS

ALTER TABLE customers ADD PRIMARY KEY (customer_id);
ALTER TABLE products ADD PRIMARY KEY (product_id);
ALTER TABLE suppliers ADD PRIMARY KEY (supplier_id);
ALTER TABLE orders ADD PRIMARY KEY (order_id);
ALTER TABLE shipments ADD PRIMARY KEY (shipment_id);

-- Foreign Keys

ALTER TABLE orders
ADD FOREIGN KEY (customer_id) REFERENCES customers(customer_id);

ALTER TABLE orders
ADD FOREIGN KEY (product_id) REFERENCES products(product_id);

ALTER TABLE orders
ADD FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id);

ALTER TABLE shipments
ADD FOREIGN KEY (order_id) REFERENCES orders(order_id);

-- Unique Keys
ALTER TABLE customers
ADD CONSTRAINT unique_customer_name UNIQUE (customer_name);

--Not Null
ALTER TABLE customers
ALTER COLUMN customer_name SET NOT NULL;

--Check Constraints
ALTER TABLE orders
ADD CONSTRAINT check_qty CHECK (order_qty > 0);

--default
ALTER TABLE shipments
ALTER COLUMN delivery_status SET DEFAULT 'Pending';








