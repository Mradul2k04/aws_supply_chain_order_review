import csv
from faker import Faker
from datetime import datetime, timedelta
import random


fake = Faker()

#total records
num_records = 156


#customer file generaton
customer_file_path = r"data_generation\cus_data.csv"
headers_customers = ["customer_id", "customer_name", "customer_region"]
region = ["North", "South", "West", "East"]

with open(customer_file_path, "w", newline="", encoding="utf-8") as f:
    write = csv.writer(f)
    write.writerow(headers_customers)
    
    for i in range(1, num_records + 1):
        customer_id = f"CUS-{i:05d}"
        customer_name = fake.name()
        customer_region = random.choice(region)
        
        write.writerow([
            customer_id,
            customer_name,
            customer_region
        ])
  
#product file generaton            
product_file_path = r"data_generation\product_data.csv"
headers_products = ["product_id", "product_name", "category"]
product_names = ["Laptop", "Router", "Server", "Storage", "Switch"]
product_category_map = {
    "Laptop": "Computing & Storage",
    "Server": "Computing & Storage",
    "Storage": "Computing & Storage",
    "Router": "Networking Equipment",
    "Switch": "Networking Equipment"
}

with open(product_file_path, "w", newline="", encoding="utf-8") as f:
    write = csv.writer(f)
    write.writerow(headers_products)
    
    for i in range(1, num_records + 1):
        product_id = f"PRO-{i:05d}"
        product_name = random.choice(product_names)
        category = product_category_map[product_name]
        
        write.writerow([
            product_id,
            product_name,
            category
        ])   


#supplier file generaton
supplier_file_path = r"data_generation\supplier_data.csv"
headers_suppliers = ["supplier_id", "supplier_name"]

with open(supplier_file_path, "w", newline="", encoding="utf-8") as f:
    write = csv.writer(f)
    write.writerow(headers_suppliers)
    
    for i in range(1, num_records + 1):
        supplier_id = f"SUP-{i:05d}"
        supplier_name = fake.name()
        
        write.writerow([
            supplier_id,
            supplier_name
        ]) 
 
 
#Orders file generaton       
orders_file_path = r"data_generation\order_data.csv"
headers_orders = ["order_id", "customer_id", "product_id", "order_date", "supplier_id", "order_qty"]

with open(orders_file_path, "w", newline="", encoding="utf-8") as f:
    write = csv.writer(f)
    write.writerow(headers_orders)
    
    for i in range(1, num_records + 1):
        order_id = f"ORD-{i:05d}"
        customer_num = random.randint(1, 156)
        customer_id = f"CUS-{customer_num:05d}"
        product_num = random.randint(1, 156)
        product_id = f"PRO-{product_num:05d}"
        supplier_num = random.randint(1, 156)
        supplier_id = f"SUP-{supplier_num:05d}"
        
        date_time = fake.date_time_between(start_date='-50d', end_date='now')
        order_date = date_time.strftime('%Y-%m-%d %H:%M:%S')
        order_qty = random.randint(1, 50)
        
        write.writerow([
          order_id,
          customer_id,
          product_id,
          order_date,
          supplier_id,
          order_qty
        ])



#Shipment file generaton        
shipment_file_path = r"data_generation\shipment_data.csv"
headers_shipments = ["shipment_id", "order_id", "shipping_date", "delivery_status", "delivery_time_days", "warehouse"]
status_types = ["Delivered", "Pending", "Delayed"]
warehouse_types = ["WH-A", "WH-B", "WH-C"]

with open(shipment_file_path, "w", newline="", encoding="utf-8") as f:
    write = csv.writer(f)
    write.writerow(headers_shipments)
    
    start_window = datetime.strptime('2026-06-01', '%Y-%m-%d')
    end_window = datetime.strptime('2026-06-30', '%Y-%m-%d')
    
    for i in range(1, num_records + 1):
        shipment_id = f"SHP-{i:05d}"
        order_num = random.randint(1, 156)
        order_id = f"ORD-{order_num:05d}"
        date_obj = fake.date_time_between(start_date=start_window, end_date=end_window)
        delivery_date = date_obj.strftime("%Y-%m-%d")
        delivery_status = random.choice(status_types)
        delivery_time_days = "" if delivery_status == "Delivered" else random.randint(1, 14)
        warehouse = random.choice(warehouse_types)
        
        write.writerow([
          shipment_id,
          order_id,
          delivery_date,
          delivery_status,
          delivery_time_days,
          warehouse
        ])