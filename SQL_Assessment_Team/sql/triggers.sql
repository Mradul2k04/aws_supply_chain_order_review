CREATE TABLE  order_audit_log (
    log_id SERIAL PRIMARY KEY,
    order_id VARCHAR(50),
    action_performed VARCHAR(100),
    action_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE products ADD COLUMN IF NOT EXISTS inventory_count INT DEFAULT 1000;

select * from order_audit_log;

--Log Every New Order
CREATE OR REPLACE FUNCTION log_new_order_proc()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO order_audit_log (order_id, action_performed)
    VALUES (NEW.order_id, 'NEW_ORDER_CREATED_SUCCESSFULLY');
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

--update triger after table insert
CREATE TRIGGER trg_log_new_order
AFTER INSERT ON orders
FOR EACH ROW
EXECUTE FUNCTION log_new_order_proc();


select * from orders;

--Update Inventory Automatically
CREATE  FUNCTION update_inventory_proc()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE products
    SET inventory_count = inventory_count - NEW.order_qty
    WHERE product_id = NEW.product_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER trg_update_inventory
AFTER INSERT ON orders
FOR EACH ROW
EXECUTE FUNCTION update_inventory_proc();