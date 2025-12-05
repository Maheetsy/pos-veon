"""
Script para ejecutar el seeder de datos
Ejecutar con: python run_seeder.py
"""
import sys
from pathlib import Path

# Agregar el directorio app al path
sys.path.insert(0, str(Path(__file__).parent / "app"))

from app.seeders.seed_data import seed_database

if __name__ == "__main__":
    print("=" * 50)
    print("Ejecutando seeder de datos...")
    print("=" * 50)
    try:
        seed_database()
        print("\n✓ Seeder ejecutado exitosamente!")
    except Exception as e:
        print(f"\n✗ Error al ejecutar el seeder: {str(e)}")
        sys.exit(1)

