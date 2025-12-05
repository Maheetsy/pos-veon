# Scripts de Base de Datos

Este directorio contiene scripts para crear y configurar la base de datos PostgreSQL para el microservicio.

## 📁 Archivos

- **`schema.sql`**: Script SQL principal que crea todas las tablas, índices, constraints y triggers
- **`create_database.sql`**: Script para crear la base de datos (instrucciones)
- **`create_database.sh`**: Script bash para Linux/Mac
- **`create_database.ps1`**: Script PowerShell para Windows
- **`create_database.py`**: Script Python multiplataforma

## 🚀 Uso

### Opción 1: Script SQL Manual (Recomendado)

1. **Crear la base de datos:**
   ```bash
   # Linux/Mac
   createdb -U postgres tienda_pos
   
   # Windows (desde PowerShell)
   createdb -U postgres tienda_pos
   ```

2. **Ejecutar el esquema:**
   ```bash
   # Linux/Mac
   psql -U postgres -d tienda_pos -f database/schema.sql
   
   # Windows
   psql -U postgres -d tienda_pos -f database\schema.sql
   ```

### Opción 2: Script Bash (Linux/Mac)

```bash
chmod +x database/create_database.sh
./database/create_database.sh
```

### Opción 3: Script PowerShell (Windows)

```powershell
.\database\create_database.ps1
```

### Opción 4: Script Python (Multiplataforma)

```bash
# Instalar dependencia si es necesario
pip install psycopg2-binary

# Ejecutar el script
python database/create_database.py
```

O con variables de entorno:

```bash
export DB_USER=postgres
export DB_PASSWORD=tu_contraseña
export DB_NAME=tienda_pos
python database/create_database.py
```

## 📋 Requisitos

- PostgreSQL 12 o superior
- Usuario con permisos para crear bases de datos (normalmente `postgres`)
- Acceso a la base de datos PostgreSQL

## 🔧 Configuración

### Variables de Entorno (Opcional)

Puedes configurar estas variables antes de ejecutar los scripts:

```bash
# Linux/Mac
export DB_HOST=localhost
export DB_PORT=5432
export DB_USER=postgres
export DB_PASSWORD=tu_contraseña
export DB_NAME=tienda_pos

# Windows PowerShell
$env:DB_HOST="localhost"
$env:DB_PORT="5432"
$env:DB_USER="postgres"
$env:DB_PASSWORD="tu_contraseña"
$env:DB_NAME="tienda_pos"
```

## 📊 Estructura Creada

El script `schema.sql` crea:

1. **Tabla `categories`**:
   - `id` (SERIAL PRIMARY KEY)
   - `name` (VARCHAR(100), UNIQUE, NOT NULL)
   - `description` (TEXT, opcional)

2. **Tabla `products`**:
   - `id` (SERIAL PRIMARY KEY)
   - `name` (VARCHAR(255), NOT NULL)
   - `short_description` (TEXT)
   - `sku` (VARCHAR(50), UNIQUE, NOT NULL)
   - `cost` (DOUBLE PRECISION, NOT NULL, > 0)
   - `sale_price` (DOUBLE PRECISION, NOT NULL, > 0)
   - `stock` (INTEGER, NOT NULL, DEFAULT 0, >= 0)
   - `unit` (VARCHAR(50))
   - `unit_of_measurement` (VARCHAR(50))
   - `provider_id` (VARCHAR(100))
   - `provider_name` (VARCHAR(255))
   - `image_path` (VARCHAR(500))
   - `category_id` (INTEGER, FK a categories.id, ON DELETE SET NULL)
   - `created_at` (TIMESTAMP WITH TIME ZONE, DEFAULT NOW())
   - `updated_at` (TIMESTAMP WITH TIME ZONE, DEFAULT NOW())

3. **Índices**:
   - Índices en campos frecuentemente consultados
   - Índice único en `categories.name`
   - Índice único en `products.sku`

4. **Constraints**:
   - Stock no negativo
   - Precios positivos
   - SKU único
   - Nombre de categoría único

5. **Triggers**:
   - Actualización automática de `updated_at` en productos

## ✅ Verificación

Después de ejecutar el script, puedes verificar que todo se creó correctamente:

```sql
-- Conectarse a la base de datos
\c tienda_pos

-- Ver tablas creadas
\dt

-- Ver estructura de una tabla
\d categories
\d products

-- Verificar índices
\di

-- Verificar constraints
SELECT 
    conname AS constraint_name,
    contype AS constraint_type,
    pg_get_constraintdef(oid) AS constraint_definition
FROM pg_constraint
WHERE conrelid IN (
    'categories'::regclass,
    'products'::regclass
);
```

## 🔄 Recrear la Base de Datos

Si necesitas recrear la base de datos desde cero:

```sql
-- ⚠️ ADVERTENCIA: Esto eliminará todos los datos
DROP DATABASE IF EXISTS tienda_pos;
CREATE DATABASE tienda_pos;
\c tienda_pos
\i database/schema.sql
```

O usando el script:

```bash
dropdb -U postgres tienda_pos
createdb -U postgres tienda_pos
psql -U postgres -d tienda_pos -f database/schema.sql
```

## 🐛 Solución de Problemas

### Error: "database already exists"
La base de datos ya existe. Puedes:
- Usarla tal como está
- Eliminarla y recrearla: `dropdb -U postgres tienda_pos`

### Error: "permission denied"
Necesitas permisos de superusuario. Usa el usuario `postgres` o un usuario con permisos.

### Error: "psql: command not found"
PostgreSQL no está instalado o no está en el PATH. Instala PostgreSQL y agrega `bin` al PATH.

### Error de conexión
Verifica que PostgreSQL esté corriendo:
```bash
# Linux/Mac
sudo service postgresql status

# Windows
# Verificar en Services si PostgreSQL está corriendo
```

## 📝 Notas

- El script es idempotente: puedes ejecutarlo múltiples veces sin problemas
- Los índices mejoran el rendimiento de las consultas
- Los triggers mantienen `updated_at` actualizado automáticamente
- Las constraints garantizan la integridad de los datos

