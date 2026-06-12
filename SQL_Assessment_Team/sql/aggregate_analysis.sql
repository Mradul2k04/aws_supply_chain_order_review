-- Use Case 1
-- Top 10 Selling Products

select product_name,sum(quantity) as total_sold
from orders
group by product_name
order by total_sold DESC
limit 10;


--highest revenue
select region,sum(quantity*unit_price) as revenue
from orders GROUP BY region
ORDER BY revenue DESC
LIMIT 1;

--average delivery time
select avg(delivery_time_days) from shipments;


-- Use Case 4
-- Supplier Performance Ranking

select supplier_name,count(*) AS total_orders,avg(delivery_date - order_date) as avg_delivery_days
from orders
group by supplier_name
order by avg_delivery_days;

-- Use Case 5
-- Monthly Sales Trend
select DATE_TRUNC('month',order_date) AS month, sum(quantity*unit_price) AS sales
FROM orders
GROUP BY month
ORDER BY month;

