# Microservicio de Gestión de Productos y Categorías - POS

Microservicio REST desarrollado con FastAPI y PostgreSQL para la gestión de inventario del sistema POS (Punto de Venta).

## 🚀 Características

- ✅ Gestión completa de productos y categorías
- ✅ Autenticación JWT con roles (admin/usuario)
- ✅ Validaciones de integridad de datos (SKU único, stock no negativo, categoría existente)
- ✅ Arquitectura por capas (Routers → Services → Repositories → Models)
- ✅ Integridad referencial con ON DELETE SET NULL
- ✅ Documentación automática con OpenAPI/Swagger
- ✅ Carga masiva de 250+ productos
- ✅ CORS configurado para consumo desde Flutter y otros servicios

## 📋 Requisitos

- Python 3.11+
- PostgreSQL 12+
- pip

## 🔧 Instalación

1. Clonar el repositorio:
```bash
git clone <repository-url>
cd Api-SQL
```

2. Crear un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
cd app
pip install -r requirements.txt
```

4. Configurar la base de datos:
   
   **Opción A: Usar scripts SQL (Recomendado)**
   ```bash
   # Crear la base de datos
   createdb -U postgres tienda_pos
   
   # Ejecutar el esquema
   psql -U postgres -d tienda_pos -f database/schema.sql
   ```
   
   **Opción B: Script Python**
   ```bash
   python database/create_database.py
   ```
   
   **Opción C: Scripts automatizados**
   - Linux/Mac: `./database/create_database.sh`
   - Windows: `.\database\create_database.ps1`
   
   Ver `database/README.md` para más opciones y detalles.
   
   **Nota**: También puedes usar una base de datos existente (como Render, Railway, etc.)

5. Configurar variables de entorno:
```bash
# Copiar el archivo de ejemplo
cp .env.example .env
# O en Windows PowerShell:
Copy-Item .env.example .env

# Editar .env con tus configuraciones reales
# IMPORTANTE: Nunca subir el archivo .env al repositorio
```

6. Ejecutar el seeder para cargar datos iniciales:
```bash
python -m app.seeders.seed_data
```

## 🏃 Ejecución

### Desarrollo Local

```bash
cd app
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

La aplicación estará disponible en:
- API: http://localhost:8000
- Documentación Swagger: http://localhost:8000/docs
- Documentación ReDoc: http://localhost:8000/redoc

### Docker

```bash
docker build -t pos-products-service .
docker run -p 8000:8000 -e DATABASE_URL=postgresql://user:pass@host:5432/dbname pos-products-service
```

## 🔐 Autenticación

### Obtener Token JWT

```bash
POST /auth/login
Content-Type: application/json

{
  "username": "admin",
  "password": "admin123"
}
```

**Usuarios de prueba:**
- **Admin**: username=`admin`, password=`admin123` (permisos completos)
- **Usuario**: username=`user`, password=`user123` (solo lectura)

### Usar el Token

Incluir el token en el header de las peticiones:
```
Authorization: Bearer <token>
```

## 📚 Endpoints

### Autenticación

- `POST /auth/login` - Obtener token JWT

### Categorías

- `GET /categories/` - Listar todas las categorías (requiere autenticación)
- `GET /categories/{id}` - Obtener categoría por ID (requiere autenticación)
- `POST /categories/` - Crear categoría (requiere rol admin)
- `PUT /categories/{id}` - Actualizar categoría (requiere rol admin)
- `DELETE /categories/{id}` - Eliminar categoría (requiere rol admin)

### Productos

- `GET /products/` - Listar todos los productos (requiere autenticación)
- `GET /products/{id}` - Obtener producto por ID (requiere autenticación)
- `GET /products/search/query` - Buscar productos por nombre, SKU o categoría (requiere autenticación)
- `POST /products/` - Crear producto (requiere rol admin)
- `PUT /products/{id}` - Actualizar producto (requiere rol admin)
- `PATCH /products/{id}/stock` - Actualizar stock directamente (requiere rol admin)
- `POST /products/{id}/decrease-stock` - Descontar stock (usado por servicio de ventas)
- `DELETE /products/{id}` - Eliminar producto (requiere rol admin)

## 🗄️ Modelo de Datos

### Tabla `categories`
- `id` (PK, autoincremental)
- `name` (único, obligatorio)
- `description` (opcional)

### Tabla `products`
- `id` (PK, autoincremental)
- `name` (obligatorio)
- `short_description` (opcional)
- `sku` (único, obligatorio)
- `cost` (obligatorio)
- `sale_price` (obligatorio)
- `stock` (default: 0, no puede ser negativo)
- `unit` (opcional)
- `unit_of_measurement` (opcional)
- `provider_id` (opcional)
- `provider_name` (opcional)
- `image_path` (opcional)
- `category_id` (FK a categories.id, ON DELETE SET NULL)
- `created_at` (timestamp automático)
- `updated_at` (timestamp automático)

## ✅ Validaciones

- **SKU único**: No se permiten productos con el mismo SKU
- **Stock no negativo**: El stock nunca puede ser menor a 0
- **Categoría existente**: Toda categoría referenciada debe existir
- **Nombre de categoría único**: No se permiten categorías duplicadas

## 🏗️ Arquitectura

El proyecto sigue una arquitectura por capas:

```
app/
├── main.py                 # Punto de entrada de la aplicación
├── config/
│   └── database.py         # Configuración de base de datos
├── models/
│   ├── category_model.py   # Modelo SQLAlchemy de Category
│   └── product_model.py    # Modelo SQLAlchemy de Product
├── schemas/
│   ├── category_schema.py  # Schemas Pydantic para Category
│   └── product_schema.py   # Schemas Pydantic para Product
├── repositories/
│   ├── category_repository.py  # Lógica de acceso a datos de Category
│   └── product_repository.py   # Lógica de acceso a datos de Product
├── services/
│   ├── category_service.py     # Lógica de negocio de Category
│   └── product_service.py      # Lógica de negocio de Product
├── routers/
│   ├── auth_router.py      # Endpoints de autenticación
│   ├── category_router.py  # Endpoints de categorías
│   └── product_router.py   # Endpoints de productos
├── auth/
│   ├── jwt_handler.py      # Manejo de JWT
│   └── auth_router.py      # Router de autenticación
└── seeders/
    └── seed_data.py        # Script para cargar datos iniciales
```

## 🌐 Despliegue

### Render

1. Crear una nueva aplicación Web Service en Render
2. Conectar el repositorio
3. Configurar variables de entorno:
   - `DATABASE_URL`: URL de conexión a PostgreSQL
   - `ENVIRONMENT`: `production`
   - `SECRET_KEY`: Clave secreta para JWT
4. Build Command: `cd app && pip install -r requirements.txt`
5. Start Command: `cd app && uvicorn main:app --host 0.0.0.0 --port $PORT`

### Railway

1. Crear nuevo proyecto en Railway
2. Conectar repositorio
3. Agregar servicio PostgreSQL
4. Configurar variables de entorno
5. Deploy automático

### AWS / Heroku

Similar a Render, configurar variables de entorno y ejecutar el comando de inicio.

## 🔄 Integración con Servicio de Ventas

El microservicio expone un endpoint especial para descontar stock:

```bash
POST /products/{product_id}/decrease-stock
Authorization: Bearer <token>
Content-Type: application/json

{
  "quantity": 5
}
```

Este endpoint:
- Valida que el producto exista
- Verifica que haya stock suficiente
- Descuenta la cantidad solicitada
- Retorna error controlado si el stock es insuficiente

## 📝 Notas

- En producción, cambiar la clave secreta JWT en `app/auth/jwt_handler.py` o usar variable de entorno
- Configurar CORS con dominios específicos en producción
- Usar pool de conexiones en producción para mejor rendimiento
- Implementar rate limiting para prevenir abusos
- Considerar implementar caché para consultas frecuentes

## 📄 Licencia

Este proyecto es parte del sistema POS y está destinado para uso interno.

