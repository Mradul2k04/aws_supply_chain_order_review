
-- Procedure 1
-- Get Customer Order History

create procedure get_customer_order_history(
    IN p_customer_id int
)
language plpgsql
as $$
begin
    select order_id,order_date,product_name,quantity,unit_price
    from orders
    where customer_id = p_customer_id
    order by order_date desc;
end;
$$;

-- Procedure 2
-- Get Product Performance

create procedure get_product_performance(
    in p_product_id int
)
language plpgsql
as $$
begin
    select product_id,product_name,sum(quantity) AS total_sold,sum(quantity * unit_price) AS total_revenue
    from orders
    where product_id = p_product_id
    group by product_id, product_name;
end;
$$;


-- Procedure 3
-- Monthly Revenue Summary

create procedure monthly_revenue_summary()
language plpgsql
as $$
begin
    select
        DATE_TRUNC('month', order_date) as month,SUM(quantity * unit_price) AS revenue
    FROM orders
    GROUP BY month
    ORDER BY month;
END;
$$;