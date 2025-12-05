from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.schemas.category_schema import CategoryResponse

class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    short_description: Optional[str] = None
    sku: str = Field(..., min_length=1, max_length=50)
    cost: float = Field(..., gt=0)
    sale_price: float = Field(..., gt=0)
    stock: int = Field(default=0, ge=0)
    unit: Optional[str] = Field(None, max_length=50)
    unit_of_measurement: Optional[str] = Field(None, max_length=50)
    provider_id: Optional[str] = Field(None, max_length=100)
    provider_name: Optional[str] = Field(None, max_length=255)
    image_path: Optional[str] = Field(None, max_length=500)
    category_id: Optional[int] = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    short_description: Optional[str] = None
    sku: Optional[str] = Field(None, min_length=1, max_length=50)
    cost: Optional[float] = Field(None, gt=0)
    sale_price: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)
    unit: Optional[str] = Field(None, max_length=50)
    unit_of_measurement: Optional[str] = Field(None, max_length=50)
    provider_id: Optional[str] = Field(None, max_length=100)
    provider_name: Optional[str] = Field(None, max_length=255)
    image_path: Optional[str] = Field(None, max_length=500)
    category_id: Optional[int] = None

class ProductResponse(ProductBase):
    id: int
    created_at: datetime
    updated_at: datetime
    category: Optional[CategoryResponse] = None
    
    class Config:
        from_attributes = True

class StockUpdate(BaseModel):
    stock: int = Field(..., ge=0)

class ProductSearch(BaseModel):
    name: Optional[str] = None
    sku: Optional[str] = None
    category_id: Optional[int] = None