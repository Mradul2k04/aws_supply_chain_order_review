-- Function 1
-- Calculate Delivery Delay

create function calculate_delivery_delay(
    p_order_date DATE,
    p_delivery_date DATE
)
returns int
language plpgsql
as $$
begin
    return p_delivery_date-p_order_date;
end;
$$;

-- Function 2
-- Calculate Profit Margin

create function calculate_profit_margin(
    p_revenue numeric,
    p_cost numeric
)
returns numeric
language plpgsql
as $$
begin
    if p_revenue=0 then
        return 0;
    end if;

    return  ROUND(
        ((p_revenue -p_cost)/p_revenue)*100,
        2
    );
end;
$$;


-- Function 3
-- Calculate Inventory Turnover

CREATE FUNCTION calculate_inventory_turnover(
    p_cogs NUMERIC,
    p_avg_inventory NUMERIC
)
RETURNS NUMERIC
LANGUAGE plpgsql
AS $$
BEGIN
    IF p_avg_inventory = 0 THEN
        RETURN 0;
    END IF;

    RETURN ROUND(
        p_cogs / p_avg_inventory,
        2
    );
END;
$$;