"""
Script Python para crear la base de datos y esquema en PostgreSQL
Ejecutar con: python database/create_database.py
"""
import os
import sys
from pathlib import Path
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Agregar el directorio raíz al path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Configuración de la base de datos
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": "postgres"  # Conectarse a postgres para crear la nueva BD
}

DB_NAME = os.getenv("DB_NAME", "tienda_pos")

def create_database():
    """Crea la base de datos si no existe"""
    try:
        print("=" * 50)
        print("Creando base de datos PostgreSQL")
        print("=" * 50)
        
        # Conectar a PostgreSQL (base de datos por defecto)
        conn = psycopg2.connect(**DB_CONFIG)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        
        # Verificar si la base de datos ya existe
        cursor.execute(
            "SELECT 1 FROM pg_database WHERE datname = %s",
            (DB_NAME,)
        )
        exists = cursor.fetchone()
        
        if exists:
            print(f"⚠ La base de datos '{DB_NAME}' ya existe")
        else:
            # Crear la base de datos
            cursor.execute(f'CREATE DATABASE {DB_NAME}')
            print(f"✓ Base de datos '{DB_NAME}' creada exitosamente")
        
        cursor.close()
        conn.close()
        return True
        
    except psycopg2.Error as e:
        print(f"✗ Error al crear la base de datos: {e}")
        return False

def create_schema():
    """Crea el esquema de la base de datos"""
    try:
        print("\nEjecutando script de esquema...")
        
        # Leer el archivo schema.sql
        schema_file = Path(__file__).parent / "schema.sql"
        if not schema_file.exists():
            print(f"✗ No se encontró el archivo schema.sql en: {schema_file}")
            return False
        
        with open(schema_file, 'r', encoding='utf-8') as f:
            schema_sql = f.read()
        
        # Conectar a la nueva base de datos
        db_config = DB_CONFIG.copy()
        db_config["database"] = DB_NAME
        
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()
        
        # Ejecutar el script SQL
        cursor.execute(schema_sql)
        conn.commit()
        
        print("✓ Esquema creado exitosamente")
        
        # Verificar tablas creadas
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_type = 'BASE TABLE'
            ORDER BY table_name
        """)
        tables = cursor.fetchall()
        
        print(f"\n✓ Tablas creadas: {', '.join([t[0] for t in tables])}")
        
        cursor.close()
        conn.close()
        
        print("\n" + "=" * 50)
        print("Base de datos lista para usar")
        print("=" * 50)
        return True
        
    except psycopg2.Error as e:
        print(f"✗ Error al ejecutar el script de esquema: {e}")
        return False

def main():
    """Función principal"""
    # Verificar si psycopg2 está instalado
    try:
        import psycopg2
    except ImportError:
        print("✗ Error: psycopg2 no está instalado")
        print("Instala con: pip install psycopg2-binary")
        sys.exit(1)
    
    # Solicitar contraseña si no está en variables de entorno
    if not DB_CONFIG["password"]:
        import getpass
        DB_CONFIG["password"] = getpass.getpass(
            f"Ingresa la contraseña de PostgreSQL para el usuario {DB_CONFIG['user']}: "
        )
    
    # Crear base de datos
    if not create_database():
        sys.exit(1)
    
    # Crear esquema
    if not create_schema():
        sys.exit(1)
    
    print("\n✓ Proceso completado exitosamente!")

if __name__ == "__main__":
    main()


