from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.database import Base, engine
from app.models.category_model import Category
from app.models.product_model import Product
from app.routers import product_router, category_router
from app.auth.auth_router import router as auth_router

# Crear las tablas en la BD si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Microservicio de Gestión de Productos y Categorías - POS",
    description="""
    Microservicio REST para la gestión de inventario del sistema POS.
    
    ## Características
    
    * Gestión completa de productos y categorías
    * Autenticación JWT con roles (admin/usuario)
    * Validaciones de integridad de datos
    * Integración con servicios de ventas
    
    ## Autenticación
    
    Usa el endpoint `/auth/login` para obtener un token JWT.
    Luego incluye el token en el header: `Authorization: Bearer <token>`
    
    **Usuarios de prueba:**
    - Admin: username=`admin`, password=`admin123`
    - Usuario: username=`user`, password=`user123`
    """,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS para permitir consumo desde Flutter y otros servicios
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar dominios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(auth_router)
app.include_router(category_router.router)
app.include_router(product_router.router)

@app.get("/", tags=["Raíz"])
def root():
    """Endpoint raíz del microservicio"""
    return {
        "message": "Microservicio de Gestión de Productos y Categorías - POS",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health", tags=["Salud"])
def health_check():
    """Endpoint de verificación de salud del servicio"""
    return {"status": "healthy", "service": "products-categories-service"}