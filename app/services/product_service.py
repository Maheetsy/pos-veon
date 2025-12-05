from sqlalchemy.orm import Session
from app.repositories.product_repository import ProductRepository
from app.repositories.category_repository import CategoryRepository
from app.schemas.product_schema import (
    ProductCreate, 
    ProductUpdate, 
    ProductResponse, 
    StockUpdate,
    ProductSearch
)
from typing import List, Optional
from fastapi import HTTPException, status

class ProductService:
    def __init__(self, db: Session):
        self.repository = ProductRepository(db)
        self.category_repository = CategoryRepository(db)

    def get_all(self) -> List[ProductResponse]:
        """Obtiene todos los productos"""
        products = self.repository.get_all()
        return [ProductResponse.model_validate(prod) for prod in products]

    def get_by_id(self, product_id: int) -> ProductResponse:
        """Obtiene un producto por ID"""
        product = self.repository.get_by_id(product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Producto con ID {product_id} no encontrado"
            )
        return ProductResponse.model_validate(product)

    def search(self, search_params: ProductSearch) -> List[ProductResponse]:
        """Busca productos por nombre, SKU o categoría"""
        products = self.repository.search(
            name=search_params.name,
            sku=search_params.sku,
            category_id=search_params.category_id
        )
        return [ProductResponse.model_validate(prod) for prod in products]

    def create(self, product: ProductCreate) -> ProductResponse:
        """Crea un nuevo producto con validaciones"""
        # Validar stock no negativo
        if product.stock < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El stock no puede ser negativo"
            )
        
        # Validar que la categoría existe si se proporciona
        if product.category_id:
            category = self.category_repository.get_by_id(product.category_id)
            if not category:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Categoría con ID {product.category_id} no existe"
                )
        
        # Validar SKU único (se hace en el repositorio)
        try:
            db_product = self.repository.create(product)
            return ProductResponse.model_validate(db_product)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )

    def update(self, product_id: int, product: ProductUpdate) -> ProductResponse:
        """Actualiza un producto con validaciones"""
        # Validar que el producto existe
        existing_product = self.repository.get_by_id(product_id)
        if not existing_product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Producto con ID {product_id} no encontrado"
            )
        
        # Validar stock no negativo si se actualiza
        if product.stock is not None and product.stock < 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El stock no puede ser negativo"
            )
        
        # Validar que la categoría existe si se actualiza
        if product.category_id is not None:
            category = self.category_repository.get_by_id(product.category_id)
            if not category:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Categoría con ID {product.category_id} no existe"
                )
        
        # Validar SKU único si se actualiza
        try:
            db_product = self.repository.update(product_id, product)
            if not db_product:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Producto con ID {product_id} no encontrado"
                )
            return ProductResponse.model_validate(db_product)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )

    def update_stock(self, product_id: int, stock_update: StockUpdate) -> ProductResponse:
        """Actualiza el stock de un producto directamente"""
        try:
            db_product = self.repository.update_stock(product_id, stock_update.stock)
            if not db_product:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Producto con ID {product_id} no encontrado"
                )
            return ProductResponse.model_validate(db_product)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )

    def decrease_stock(self, product_id: int, quantity: int) -> ProductResponse:
        """Descuenta stock de un producto (usado por el servicio de ventas)"""
        try:
            db_product = self.repository.decrease_stock(product_id, quantity)
            if not db_product:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Producto con ID {product_id} no encontrado"
                )
            return ProductResponse.model_validate(db_product)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )

    def delete(self, product_id: int) -> dict:
        """Elimina un producto"""
        product = self.repository.get_by_id(product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Producto con ID {product_id} no encontrado"
            )
        
        success = self.repository.delete(product_id)
        if success:
            return {"message": f"Producto {product_id} eliminado correctamente"}
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error al eliminar el producto"
            )