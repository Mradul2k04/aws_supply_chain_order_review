-- CREATE
-- Insert:
-- 20 New Customers
-- 20 New Orders

INSERT INTO customers (customer_id, customer_name, customer_region)
VALUES
('CUS-00157', 'Amit Sharma', 'North'),
('CUS-00158', 'Riya Singh', 'South');

INSERT INTO orders (order_id, customer_id, product_id, supplier_id, order_date, order_qty)
VALUES
('ORD-00157', 'CUS-00010', 'PRO-00005', 'SUP-00002', NOW(), 12);


-- READ
-- Retrieve:
-- Orders by Region
SELECT o.*
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.customer_region = 'North';

-- Orders by Product
SELECT o.order_id, p.product_name, o.order_qty
FROM orders o
JOIN products p ON o.product_id = p.product_id
WHERE p.product_name = 'Laptop';


-- UPDATE
-- Update:
-- Delivery Status
UPDATE shipments
SET delivery_status = 'Delivered'
WHERE shipment_id = 'SHP-00010';

-- Product Category
UPDATE products
SET category = 'IT Equipment'
WHERE product_name = 'Router';

-- DELETE
-- Delete:
-- Cancelled Orders

DELETE FROM orders
WHERE order_qty = 0;

-- Duplicate Customers
DELETE FROM customers
WHERE customer_id NOT IN (
    SELECT MIN(customer_id)
    FROM customers
    GROUP BY customer_name
);






