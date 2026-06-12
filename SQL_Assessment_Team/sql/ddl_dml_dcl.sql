-------------------------------------------------------------DDL-------------------------------------------------------------------
--Creating Staging table for data processing
CREATE TABLE Staging_Orders (
    staging_id INT  PRIMARY KEY,
    order_id INT,
    quantity INT,
    status VARCHAR(50)
);

-- ALTER: Add operational column to track modifications
ALTER TABLE Staging_Orders ADD COLUMN last_updated_by VARCHAR(100);

-- TRUNCATE: Delete all data from table
TRUNCATE TABLE Staging_Orders;

-- DROP: Remove the table
DROP TABLE IF EXISTS Staging_Orders;

------------------------------------------------------------DML----------------------------------------------------------------------------

-- INSERT: Standard row population
INSERT INTO Customers (customer_id, customer_name, customer_region)
VALUES ('CUS-00156', 'Global Logistics Corp', 'North ');

-- UPDATE: Bulk condition adjustment
UPDATE Shipments 
SET delivery_status = 'Delayed' 
WHERE shipping_date < '2026-06-01' AND delivery_status = 'Pending';

-- DELETE: Remove cancelled records
DELETE FROM Shipments WHERE delivery_status = 'Pending';


--------------------------------------------------------------DCL--------------------------------------------------------------------------
-- 1. GRANT: Give the Operations user permission to view and update the Orders table
GRANT SELECT, INSERT, UPDATE ON Orders TO SupplyChain_Operations;

-- 2. REVOKE: Explicitly strip away the update permission from the Operations user
REVOKE UPDATE ON Orders FROM SupplyChain_Operations;