from sqlalchemy.orm import Session
from app.repositories.category_repository import CategoryRepository
from app.repositories.product_repository import ProductRepository
from app.schemas.category_schema import CategoryCreate, CategoryUpdate, CategoryResponse
from typing import List
from fastapi import HTTPException, status

class CategoryService:
    def __init__(self, db: Session):
        self.repository = CategoryRepository(db)
        self.product_repository = ProductRepository(db)

    def get_all(self) -> List[CategoryResponse]:
        """Obtiene todas las categorías"""
        categories = self.repository.get_all()
        return [CategoryResponse.model_validate(cat) for cat in categories]

    def get_by_id(self, category_id: int) -> CategoryResponse:
        """Obtiene una categoría por ID"""
        category = self.repository.get_by_id(category_id)
        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Categoría con ID {category_id} no encontrada"
            )
        return CategoryResponse.model_validate(category)

    def create(self, category: CategoryCreate) -> CategoryResponse:
        """Crea una nueva categoría"""
        try:
            db_category = self.repository.create(category)
            return CategoryResponse.model_validate(db_category)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )

    def update(self, category_id: int, category: CategoryUpdate) -> CategoryResponse:
        """Actualiza una categoría"""
        try:
            db_category = self.repository.update(category_id, category)
            if not db_category:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Categoría con ID {category_id} no encontrada"
                )
            return CategoryResponse.model_validate(db_category)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )

    def delete(self, category_id: int) -> dict:
        """Elimina una categoría"""
        # Verificar que la categoría existe
        category = self.repository.get_by_id(category_id)
        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Categoría con ID {category_id} no encontrada"
            )
        
        # La eliminación es lógica (ON DELETE SET NULL), así que los productos no se eliminan
        success = self.repository.delete(category_id)
        if success:
            return {"message": f"Categoría {category_id} eliminada correctamente"}
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error al eliminar la categoría"
            )

