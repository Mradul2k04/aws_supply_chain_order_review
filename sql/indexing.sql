SELECT * FROM customers;
--Indexing

--customer_id
EXPLAIN analyze
select customer_id from customers where (customer_id= 'CUS-00001');
create index idx_orders_customer_id ON orders (customer_id);
EXPLAIN analyze
select customer_id from customers where (customer_id= 'CUS-00001');


--product_id
CREATE INDEX idx_orders_product_id ON orders (product_id);

--order_date
CREATE INDEX idx_orders_order_date ON orders (order_date);

--supplier_id
CREATE INDEX idx_shipments_order_id ON shipments (order_id);