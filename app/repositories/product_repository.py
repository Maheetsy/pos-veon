from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import or_
from app.models.product_model import Product
from app.schemas.product_schema import ProductCreate, ProductUpdate, StockUpdate
from typing import List, Optional

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Product]:
        """Obtiene todos los productos"""
        return self.db.query(Product).all()

    def get_by_id(self, product_id: int) -> Optional[Product]:
        """Obtiene un producto por ID"""
        return self.db.query(Product).filter(Product.id == product_id).first()

    def get_by_sku(self, sku: str) -> Optional[Product]:
        """Obtiene un producto por SKU"""
        return self.db.query(Product).filter(Product.sku == sku).first()

    def search(self, name: Optional[str] = None, sku: Optional[str] = None, category_id: Optional[int] = None) -> List[Product]:
        """Busca productos por nombre, SKU o categoría"""
        query = self.db.query(Product)
        
        if name:
            query = query.filter(Product.name.ilike(f"%{name}%"))
        if sku:
            query = query.filter(Product.sku.ilike(f"%{sku}%"))
        if category_id:
            query = query.filter(Product.category_id == category_id)
        
        return query.all()

    def create(self, product: ProductCreate) -> Product:
        """Crea un nuevo producto"""
        # Verificar si ya existe un producto con el mismo SKU
        existing = self.get_by_sku(product.sku)
        if existing:
            raise ValueError(f"Ya existe un producto con el SKU '{product.sku}'")
        
        db_product = Product(**product.model_dump())
        self.db.add(db_product)
        try:
            self.db.commit()
            self.db.refresh(db_product)
            return db_product
        except IntegrityError:
            self.db.rollback()
            raise ValueError(f"Ya existe un producto con el SKU '{product.sku}'")

    def update(self, product_id: int, product: ProductUpdate) -> Optional[Product]:
        """Actualiza un producto"""
        db_product = self.get_by_id(product_id)
        if not db_product:
            return None
        
        update_data = product.model_dump(exclude_unset=True)
        
        # Verificar si el nuevo SKU ya existe
        if "sku" in update_data:
            existing = self.get_by_sku(update_data["sku"])
            if existing and existing.id != product_id:
                raise ValueError(f"Ya existe un producto con el SKU '{update_data['sku']}'")
        
        for field, value in update_data.items():
            setattr(db_product, field, value)
        
        try:
            self.db.commit()
            self.db.refresh(db_product)
            return db_product
        except IntegrityError:
            self.db.rollback()
            raise ValueError(f"Error al actualizar el producto")

    def update_stock(self, product_id: int, stock: int) -> Optional[Product]:
        """Actualiza el stock de un producto directamente"""
        db_product = self.get_by_id(product_id)
        if not db_product:
            return None
        
        if stock < 0:
            raise ValueError("El stock no puede ser negativo")
        
        db_product.stock = stock
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def decrease_stock(self, product_id: int, quantity: int) -> Optional[Product]:
        """Descuenta stock de un producto (usado por el servicio de ventas)"""
        db_product = self.get_by_id(product_id)
        if not db_product:
            return None
        
        if db_product.stock < quantity:
            raise ValueError(f"Stock insuficiente. Disponible: {db_product.stock}, Solicitado: {quantity}")
        
        db_product.stock -= quantity
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def delete(self, product_id: int) -> bool:
        """Elimina un producto"""
        db_product = self.get_by_id(product_id)
        if not db_product:
            return False
        
        self.db.delete(db_product)
        self.db.commit()
        return True