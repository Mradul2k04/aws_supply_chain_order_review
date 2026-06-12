import datetime
from sqlalchemy import Column, String, Integer, DateTime, Date, ForeignKey, CheckConstraint
from database import Base

class Customer(Base):
    __tablename__ = 'customers'

    customer_id = Column(String(50), primary_key=True)
    customer_name = Column(String(255), nullable=False)
    customer_region = Column(String(50), nullable=False)

    __table_args__ = (
        CheckConstraint(
            "customer_region IN ('North', 'South', 'West', 'East')", 
            name="chk_region"
        ),
        CheckConstraint(
            "customer_id ~ '^CUS-\\d{5}$'", 
            name="chk_customer_id_format"
        ),
    )


class Product(Base):
    __tablename__ = 'products'

    product_id = Column(String(50), primary_key=True)
    product_name = Column(String(255), nullable=False)
    category = Column(String(100), nullable=False)

    __table_args__ = (
        CheckConstraint(
            "product_id ~ '^PRO-\\d{5}$'", 
            name="chk_product_id_format"
        ),
    )


class Supplier(Base):
    __tablename__ = 'suppliers'

    supplier_id = Column(String(50), primary_key=True)
    supplier_name = Column(String(255), nullable=False)

    __table_args__ = (
        CheckConstraint(
            "supplier_id ~ '^SUP-\\d{5}$'", 
            name="chk_supplier_id_format"
        ),
    )


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(String(50), primary_key=True)
    customer_id = Column(String(50), ForeignKey('customers.customer_id', ondelete='RESTRICT'), nullable=False)
    product_id = Column(String(50), ForeignKey('products.product_id', ondelete='RESTRICT'), nullable=False)
    order_date = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    supplier_id = Column(String(50), ForeignKey('suppliers.supplier_id', ondelete='RESTRICT'), nullable=False)
    order_qty = Column(Integer, nullable=False)

    __table_args__ = (
        CheckConstraint('order_qty > 0', name='chk_order_qty'),
        CheckConstraint(
            "order_id ~ '^ORD-\\d{5}$'", 
            name="chk_order_id_format"
        ),
    )


class Shipment(Base):
    __tablename__ = 'shipments'

    shipment_id = Column(String(50), primary_key=True)
    order_id = Column(String(50), ForeignKey('orders.order_id', ondelete='CASCADE'), nullable=False)
    shipping_date = Column(Date, nullable=False)
    delivery_status = Column(String(50), nullable=False)
    delivery_time_days = Column(Integer, nullable=True)  
    warehouse = Column(String(50), nullable=False)

    __table_args__ = (
        CheckConstraint(
            "delivery_status IN ('Delivered', 'Pending', 'Delayed')", 
            name="chk_status"
        ),
        CheckConstraint(
            "shipment_id ~ '^SHP-\\d{5}$'", 
            name="chk_shipment_id_format"
        ),
    )