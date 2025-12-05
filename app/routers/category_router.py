from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.config.database import get_db
from app.services.category_service import CategoryService
from app.schemas.category_schema import CategoryResponse, CategoryCreate, CategoryUpdate

router = APIRouter(prefix="/categories", tags=["Categorías"])

@router.post("/", response_model=CategoryResponse, status_code=201)
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db)
):
    """Crear una nueva categoría"""
    service = CategoryService(db)
    return service.create(category)

@router.get("/", response_model=List[CategoryResponse])
def get_all_categories(
    db: Session = Depends(get_db)
):
    """Consultar todas las categorías"""
    service = CategoryService(db)
    return service.get_all()

@router.get("/{category_id}", response_model=CategoryResponse)
def get_category_by_id(
    category_id: int,
    db: Session = Depends(get_db)
):
    """Consultar categoría por ID"""
    service = CategoryService(db)
    return service.get_by_id(category_id)

@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(
    category_id: int,
    category: CategoryUpdate,
    db: Session = Depends(get_db)
):
    """Editar categoría"""
    service = CategoryService(db)
    return service.update(category_id, category)

@router.delete("/{category_id}", status_code=200)
def delete_category(
    category_id: int,
    db: Session = Depends(get_db)
):
    """Eliminar categoría"""
    service = CategoryService(db)
    return service.delete(category_id)

