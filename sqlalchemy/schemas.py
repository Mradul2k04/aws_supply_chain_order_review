from pydantic import BaseModel
from datetime import datetime, date


#Customer
class CustomerCreate(BaseModel):
    customer_id: str
    customer_name: str
    customer_region: str


class CustomerResponse(CustomerCreate):
    class Config:
        from_attributes = True


# Product
class ProductCreate(BaseModel):
    product_id: str
    product_name: str
    category: str


class ProductResponse(ProductCreate):
    class Config:
        from_attributes = True


#Supplier
class SupplierCreate(BaseModel):
    supplier_id: str
    supplier_name: str


class SupplierResponse(SupplierCreate):
    class Config:
        from_attributes = True


#Order
class OrderCreate(BaseModel):
    order_id: str
    customer_id: str
    product_id: str
    supplier_id: str
    order_qty: int
    order_date: datetime | None = None


class OrderResponse(OrderCreate):
    class Config:
        from_attributes = True


# Shipment
class ShipmentCreate(BaseModel):
    shipment_id: str
    order_id: str
    shipping_date: date
    delivery_status: str
    delivery_time_days: int | None = None
    warehouse: str


class ShipmentResponse(ShipmentCreate):
    class Config:
        from_attributes = True