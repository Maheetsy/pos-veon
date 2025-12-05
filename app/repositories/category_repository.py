from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.category_model import Category
from app.schemas.category_schema import CategoryCreate, CategoryUpdate
from typing import List, Optional

class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Category]:
        """Obtiene todas las categorías"""
        return self.db.query(Category).all()

    def get_by_id(self, category_id: int) -> Optional[Category]:
        """Obtiene una categoría por ID"""
        return self.db.query(Category).filter(Category.id == category_id).first()

    def get_by_name(self, name: str) -> Optional[Category]:
        """Obtiene una categoría por nombre"""
        return self.db.query(Category).filter(Category.name == name).first()

    def create(self, category: CategoryCreate) -> Category:
        """Crea una nueva categoría"""
        # Verificar si ya existe una categoría con el mismo nombre
        existing = self.get_by_name(category.name)
        if existing:
            raise ValueError(f"Ya existe una categoría con el nombre '{category.name}'")
        
        db_category = Category(**category.model_dump())
        self.db.add(db_category)
        try:
            self.db.commit()
            self.db.refresh(db_category)
            return db_category
        except IntegrityError:
            self.db.rollback()
            raise ValueError(f"Ya existe una categoría con el nombre '{category.name}'")

    def update(self, category_id: int, category: CategoryUpdate) -> Optional[Category]:
        """Actualiza una categoría"""
        db_category = self.get_by_id(category_id)
        if not db_category:
            return None
        
        update_data = category.model_dump(exclude_unset=True)
        
        # Verificar si el nuevo nombre ya existe
        if "name" in update_data:
            existing = self.get_by_name(update_data["name"])
            if existing and existing.id != category_id:
                raise ValueError(f"Ya existe una categoría con el nombre '{update_data['name']}'")
        
        for field, value in update_data.items():
            setattr(db_category, field, value)
        
        try:
            self.db.commit()
            self.db.refresh(db_category)
            return db_category
        except IntegrityError:
            self.db.rollback()
            raise ValueError(f"Ya existe una categoría con el nombre '{update_data.get('name', '')}'")

    def delete(self, category_id: int) -> bool:
        """Elimina una categoría"""
        db_category = self.get_by_id(category_id)
        if not db_category:
            return False
        
        self.db.delete(db_category)
        self.db.commit()
        return True

