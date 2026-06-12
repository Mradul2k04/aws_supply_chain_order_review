-- INNER JOIN
-- Retrieve:
-- Customer + Order Details
select o.order_id,c.customer_id,
c.customer_name
from orders as  o
inner join customers as c
on o.customer_id=c.customer_id;


-- LEFT JOIN
-- Retrieve:
-- Customers without Orders
select c.customer_id,c.customer_name,c.customer_region
from customers as c left join orders as  o
on c.customer_id = o.customer_id
where o.customer_id is null;


-- RIGHT JOIN
-- Retrieve:
-- Products not Ordered
select p.product_id,p.product_name,p.category
from orders o
right join products p
    on o.product_id=p.product_id
where o.product_id is null;


-- SELF JOIN
-- Find:
-- Suppliers operating in same region
alter table suppliers
add column region VARCHAR(50);
selects1.supplier_name as supplier_1,s2.supplier_name as supplier_2,s1.region
from suppliers s1
join suppliers s2
on s1.region=s2.region and s1.supplier_id<s2.supplier_id;

-- Subqueries
-- Use Case 1
-- Find customers whose orders exceed average quantity.
select distinct c.customer_id,c.customer_name,o.order_qty
from customers c
join orders o
    on c.customer_id = o.customer_id
where o.order_qty>(SELECT AVG(order_qty)
    FROM orders
);

-- Use Case 2
-- Find products with revenue greater than overall average revenue.
select p.product_id,p.product_name,sum(o.order_qty*p.unit_price) as revenue
from products p
join orders o
on p.product_id = o.product_id
group by p.product_id, p.product_name
having sum(o.order_qty*p.unit_price)>
(select avg(order_qty*unit_price)
from products p join orders o on p.product_id=o.product_id);


-- Use Case 3
-- Find top supplier based on shipment volume.
select supplier_id, sum(order_qty) AS shipment_volume
from orders
group by supplier_id
order by  shipment_volume desc
limit 1;
