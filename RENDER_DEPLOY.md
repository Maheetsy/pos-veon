# Guía de Despliegue en Render

Esta guía te ayudará a desplegar el microservicio de Productos y Categorías en Render.

## 📋 Requisitos Previos

1. Cuenta en [Render](https://render.com)
2. Repositorio Git (GitHub, GitLab, o Bitbucket)

## 🚀 Pasos para Desplegar

### 1. Crear Base de Datos PostgreSQL en Render

1. Ve a tu dashboard de Render
2. Click en "New +" → "PostgreSQL"
3. Configura:
   - **Name**: `pos-database` (o el nombre que prefieras)
   - **Database**: `pos_veon` (o el nombre que prefieras)
   - **User**: Se genera automáticamente
   - **Region**: Elige la más cercana (Oregon, etc.)
   - **PostgreSQL Version**: La más reciente
   - **Plan**: Free (para desarrollo) o Paid (para producción)

4. Una vez creada, ve a la sección "Connections"
5. **IMPORTANTE**: Copia la **"Internal Database URL"** (para servicios dentro de Render)
   - Formato: `postgresql://usuario:contraseña@host.oregon-postgres.render.com/nombre_bd`

### 2. Crear Web Service en Render

1. Ve a tu dashboard de Render
2. Click en "New +" → "Web Service"
3. Conecta tu repositorio Git
4. Configura el servicio:
   - **Name**: `pos-products-service` (o el nombre que prefieras)
   - **Environment**: `Python 3`
   - **Build Command**: 
     ```bash
     cd app && pip install -r requirements.txt
     ```
   - **Start Command**: 
     ```bash
     cd app && uvicorn main:app --host 0.0.0.0 --port $PORT
     ```
   - **Plan**: Free (para desarrollo) o Paid (para producción)

### 3. Configurar Variables de Entorno

En el dashboard de tu Web Service, ve a la sección **"Environment"** y agrega las siguientes variables:

#### Variables Requeridas:

```bash
# Base de Datos (copiar desde tu PostgreSQL Database)
DATABASE_URL=postgresql://usuario:contraseña@host.oregon-postgres.render.com/nombre_bd

# Entorno
ENVIRONMENT=production

# JWT - Generar una clave segura
SECRET_KEY=tu-clave-secreta-aqui-generar-con-openssl-rand-hex-32

# JWT - Configuración
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

#### Variables Opcionales:

```bash
# CORS (si necesitas restringir orígenes)
CORS_ORIGINS=https://tudominio.com,https://app.tudominio.com

# Puerto (Render lo proporciona automáticamente, pero puedes especificarlo)
PORT=10000
```

### 4. Generar Clave Secreta para JWT

Para generar una clave secreta segura, ejecuta en tu terminal:

```bash
# Linux/Mac
openssl rand -hex 32

# Windows PowerShell
-join ((48..57) + (65..90) + (97..122) | Get-Random -Count 64 | % {[char]$_})
```

O usa un generador online: https://randomkeygen.com/

### 5. Desplegar

1. Guarda todas las variables de entorno
2. Render comenzará automáticamente a construir y desplegar tu servicio
3. Puedes ver el progreso en la sección "Logs"
4. Una vez completado, tu servicio estará disponible en: `https://tu-servicio.onrender.com`

### 6. Ejecutar Seeder (Cargar Datos Iniciales)

Para cargar los 250+ productos iniciales, tienes dos opciones:

#### Opción A: Desde tu máquina local

1. Configura tu `.env` local con la **"External Database URL"** de Render
2. Ejecuta:
   ```bash
   python run_seeder.py
   ```

#### Opción B: Desde Render (SSH)

1. En el dashboard de Render, ve a tu servicio
2. Click en "Shell" (si está disponible en tu plan)
3. Ejecuta:
   ```bash
   cd app
   python -m app.seeders.seed_data
   ```

## 🔒 Seguridad

### ✅ Buenas Prácticas:

- ✅ **NUNCA** hardcodear credenciales en el código
- ✅ Usar variables de entorno para toda la configuración sensible
- ✅ La `DATABASE_URL` debe estar solo en variables de entorno
- ✅ Generar `SECRET_KEY` única y segura para producción
- ✅ Usar `ENVIRONMENT=production` en Render
- ✅ Configurar CORS con dominios específicos en producción

### ❌ Evitar:

- ❌ Subir archivos `.env` al repositorio
- ❌ Compartir credenciales en código o documentación pública
- ❌ Usar claves de desarrollo en producción

## 📝 Verificación Post-Despliegue

1. **Health Check**: 
   ```
   GET https://tu-servicio.onrender.com/health
   ```
   Debe retornar: `{"status": "healthy", "service": "products-categories-service"}`

2. **Documentación**:
   ```
   https://tu-servicio.onrender.com/docs
   ```

3. **Autenticación**:
   ```bash
   POST https://tu-servicio.onrender.com/auth/login
   Content-Type: application/json
   
   {
     "username": "admin",
     "password": "admin123"
   }
   ```

4. **Listar Productos** (requiere token):
   ```bash
   GET https://tu-servicio.onrender.com/products/
   Authorization: Bearer <tu-token>
   ```

## 🔧 Solución de Problemas

### Error: "DATABASE_URL no está configurada"

- Verifica que la variable `DATABASE_URL` esté configurada en Render
- Asegúrate de usar la "Internal Database URL" para servicios dentro de Render

### Error de Conexión a la Base de Datos

- Verifica que la base de datos esté activa en Render
- Revisa que la URL sea correcta (sin espacios al inicio/final)
- Asegúrate de usar la URL "Internal" si el servicio está en Render

### Error al Ejecutar Migraciones

- Las tablas se crean automáticamente al iniciar la aplicación
- Si hay problemas, ejecuta el seeder manualmente

## 📚 Recursos Adicionales

- [Documentación de Render](https://render.com/docs)
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)
- [PostgreSQL en Render](https://render.com/docs/databases)

## 🎉 ¡Listo!

Tu microservicio debería estar funcionando en Render. Recuerda:

1. ✅ Configurar todas las variables de entorno
2. ✅ Ejecutar el seeder para cargar datos iniciales
3. ✅ Probar los endpoints desde la documentación Swagger
4. ✅ Configurar CORS para tu aplicación Flutter

