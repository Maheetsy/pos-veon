from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.config.database import get_db
from app.services.product_service import ProductService
from app.schemas.product_schema import (
    ProductResponse, 
    ProductCreate, 
    ProductUpdate,
    StockUpdate,
    ProductSearch
)
from app.schemas.stock_schema import DecreaseStockRequest
from app.auth.jwt_handler import require_admin, require_auth

router = APIRouter(prefix="/products", tags=["Productos"])

@router.post("/", response_model=ProductResponse, status_code=201)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin)
):
    """Crear un nuevo producto (requiere rol administrador)"""
    service = ProductService(db)
    return service.create(product)

@router.get("/", response_model=List[ProductResponse])
def get_all_products(
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_auth)
):
    """Consultar todos los productos"""
    service = ProductService(db)
    return service.get_all()

@router.get("/{product_id}", response_model=ProductResponse)
def get_product_by_id(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_auth)
):
    """Consultar producto por ID"""
    service = ProductService(db)
    return service.get_by_id(product_id)

@router.get("/search/query", response_model=List[ProductResponse])
def search_products(
    name: Optional[str] = Query(None, description="Buscar por nombre"),
    sku: Optional[str] = Query(None, description="Buscar por SKU"),
    category_id: Optional[int] = Query(None, description="Buscar por categoría"),
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_auth)
):
    """Buscar productos por nombre, SKU o categoría"""
    service = ProductService(db)
    search_params = ProductSearch(
        name=name,
        sku=sku,
        category_id=category_id
    )
    return service.search(search_params)

@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    product: ProductUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin)
):
    """Editar producto (requiere rol administrador)"""
    service = ProductService(db)
    return service.update(product_id, product)

@router.patch("/{product_id}/stock", response_model=ProductResponse)
def update_stock(
    product_id: int,
    stock_update: StockUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin)
):
    """Actualizar stock de manera directa (requiere rol administrador)"""
    service = ProductService(db)
    return service.update_stock(product_id, stock_update)

@router.post("/{product_id}/decrease-stock", response_model=ProductResponse)
def decrease_stock(
    product_id: int,
    request: DecreaseStockRequest,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_auth)
):
    """Descontar stock de un producto (usado por el servicio de ventas)"""
    service = ProductService(db)
    return service.decrease_stock(product_id, request.quantity)

@router.delete("/{product_id}", status_code=200)
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin)
):
    """Eliminar producto (requiere rol administrador)"""
    service = ProductService(db)
    return service.delete(product_id)