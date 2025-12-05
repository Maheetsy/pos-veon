from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.config.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    short_description = Column(Text, nullable=True)
    sku = Column(String(50), unique=True, nullable=False, index=True)
    
    # Precios y Stock
    cost = Column(Float, nullable=False)
    sale_price = Column(Float, nullable=False)
    stock = Column(Integer, default=0, nullable=False)
    
    # Unidades y Proveedor
    unit = Column(String(50), nullable=True)
    unit_of_measurement = Column(String(50), nullable=True)
    provider_id = Column(String(100), nullable=True)
    provider_name = Column(String(255), nullable=True)
    
    image_path = Column(String(500), nullable=True)

    # Clave Foránea con ON DELETE SET NULL
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="SET NULL"), nullable=True)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    
    # Relación
    category = relationship("Category", back_populates="products")