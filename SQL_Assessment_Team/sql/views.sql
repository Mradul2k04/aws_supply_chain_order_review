--Customer Order Summary View
create view Customer_Summary as 
select c.customer_id,
    c.customer_name,
    c.customer_region,
	COUNT(o.order_id) AS total_orders_placed
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name, c.customer_region;


--Product Revenue View
CREATE view view_product_revenue as
SELECT 
    p.product_id,
    p.product_name,
    p.category,
    COUNT(o.order_id) AS times_ordered,
	COALESCE(SUM(o.order_qty), 0) AS total_quantity_sold
FROM products p
LEFT JOIN orders o ON p.product_id = o.product_id
GROUP BY p.product_id, p.product_name, p.category;

--Shipment Performance View
CREATE view view_shipment_performance AS
SELECT 
    sh.shipment_id,
    sh.order_id,
    o.order_date,
    sh.shipping_date,
    sh.delivery_status,
    sh.warehouse,
    COALESCE(sh.delivery_time_days, 0) AS logistics_delay_days,
    o.order_qty AS items_in_transit
FROM shipments sh
JOIN orders o ON sh.order_id = o.order_id;