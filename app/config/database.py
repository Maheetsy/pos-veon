import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import NullPool

# URL de conexion desde variable de entorno
# IMPORTANTE: Nunca hardcodear credenciales en el codigo
# Configurar DATABASE_URL en el archivo .env o en las variables de entorno del sistema
# En Render: Configurar DATABASE_URL en el dashboard (Environment Variables)
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError(
        "DATABASE_URL no esta configurada. "
        "Por favor, configura la variable de entorno DATABASE_URL en tu archivo .env o en el sistema. "
        "Ejemplo: postgresql://usuario:contraseña@host:puerto/nombre_bd"
    )

# Configuracion del engine para produccion
# En produccion, usar pool de conexiones
if os.getenv("ENVIRONMENT") == "production":
    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True,
        pool_size=10,
        max_overflow=20
    )
else:
    engine = create_engine(DATABASE_URL, poolclass=NullPool)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependencia para obtener la DB en cada peticion (Dependency Injection)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
