from sqlalchemy.orm import Session
from SQL_Assessment_Team.sqlalchemy.orm_models import  Customer, Product, Supplier, Order, Shipment

# Customer 

#create new customer
def create_customer(db: Session,customer_id:str,customer_name:str,customer_region: str):
    customer = Customer(customer_id=customer_id,customer_name=customer_name,customer_region=customer_region)
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer


#get all customer
def get_all_customer(db: Session):
    return db.query(Customer).all()


#get customer by id
def get_customer(db: Session,customer_id:str):
    return db.query(Customer).filter(Customer.customer_id == customer_id).first()


#update customer
def update_customer(db: Session,customer_id:str,customer_name:str,customer_region:str):
    db_cust = db.query(Customer).filter(Customer.customer_id == customer_id).first()
    if db_cust:
        db_cust.customer_name=customer_name
        db_cust.customer_region=customer_region
        db.commit()
        db.refresh(db_cust)

    return db_cust

#delete customer
def delete_customer(db: Session,customer_id:str):
    cust=db.query(Customer).filter(Customer.customer_id == customer_id).first()
    if cust:
        db.delete(cust)
        db.commit()
    return cust


#Product

# create product
def create_product(db: Session,product_id:str,product_name:str,category:str):
    new_product=Product(product_id=product_id,product_name=product_name,category=category)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


# get product by id
def get_product(db: Session,product_id:str):
    return db.query(Product).filter(Product.product_id==product_id).first()


# get all products
def get_all_products(db: Session):
    return db.query(Product).all()


#update products
def update_product_category(db:Session,product_id:str,new_category:str):
    update_product=db.query(Product).filter(Product.product_id==product_id).first()
    if update_product:
        update_product.category = new_category
        db.commit()
        db.refresh(update_product)

    return update_product

# delete product
def delete_product(db: Session,product_id:str):
    product=db.query(Product).filter(Product.product_id==product_id).first()
    if product:
        db.delete(product)
        db.commit()
    return product


# Supplier

#create new supplier
def create_supplier(db:Session,supplier_id:str,supplier_name:str):
    supplier=Supplier(supplier_id=supplier_id,supplier_name=supplier_name)
    db.add(supplier)
    db.commit()
    db.refresh(supplier)
    return supplier


# get  supplier by id
def get_supplier(db: Session, supplier_id: str):
    return db.query(Supplier).filter(Supplier.supplier_id==supplier_id).first()

#get all suppliers
def get_all_suppliers(db: Session):
    return db.query(Supplier).all()


# update supplier name
def update_supplier_name(db:Session,supplier_id:str,new_name:str):
    updated_supplier=db.query(Supplier).filter(Supplier.supplier_id==supplier_id).first()

    if updated_supplier:
        updated_supplier.supplier_name=new_name
        db.commit()
        db.refresh(updated_supplier)

    return updated_supplier


#delete supplier
def delete_supplier(db:Session,supplier_id:str):
    supplier=db.query(Supplier).filter(Supplier.supplier_id==supplier_id).first()
    if supplier:
        db.delete(supplier)
        db.commit()
    return supplier


#Order


# create new order
def create_order(db: Session,order_id: str,customer_id: str,product_id: str,supplier_id: str,order_date,order_qty: int):
    order = Order(order_id=order_id,customer_id=customer_id,product_id=product_id,supplier_id=supplier_id,order_date=order_date,order_qty=order_qty)

    db.add(order)
    db.commit()
    db.refresh(order)

    return order


#get order by id
def get_order(db: Session,order_id:str):
    return db.query(Order).filter(Order.order_id==order_id).first()


#get all orders
def get_all_orders(db:Session):
    return db.query(Order).all()


#get all orders ordered by customer
def get_orders_by_customer(db:Session,customer_id:str):
    return db.query(Order).filter(Order.customer_id == customer_id).all()


# update the order quantity
def update_order_quantity(db:Session,order_id:str,new_qty:int):
    order = db.query(Order).filter(Order.order_id==order_id).first()
    if order:
        order.order_qty=new_qty
        db.commit()
        db.refresh(order)
    return order


def delete_order(db: Session,order_id:str):
    order = db.query(Order).filter(Order.order_id==order_id).first()
    if order:
        db.delete(order)
        db.commit()

    return order


#Shipment

#create shipment
def create_shipment(db: Session,shipment_id:str, order_id:str, shipping_date,delivery_status:str, delivery_time_days:int, warehouse:str):
    shipment = Shipment(shipment_id=shipment_id,order_id=order_id,shipping_date=shipping_date,delivery_status=delivery_status,delivery_time_days=delivery_time_days,warehouse=warehouse)

    db.add(shipment)
    db.commit()
    db.refresh(shipment)

    return shipment

# get shipment by id
def get_shipment(db: Session, shipment_id: str):
    return db.query(Shipment).filter(Shipment.shipment_id==shipment_id).first()


# get all shipments
def get_all_shipments(db: Session):
    return db.query(Shipment).all()

#update shipment status
def update_delivery_status(db: Session,shipment_id:str,new_status:str):
    shipment=db.query(Shipment).filter(Shipment.shipment_id==shipment_id).first()
    if shipment:
        shipment.delivery_status = new_status
        db.commit()
        db.refresh(shipment)

    return shipment


#delete shipment
def delete_shipment(db: Session, shipment_id: str):
    shipment=db.query(Shipment).filter(Shipment.shipment_id==shipment_id).first()
    if shipment:
        db.delete(shipment)
        db.commit()

    return shipment