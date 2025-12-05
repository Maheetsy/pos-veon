#!/bin/bash

# ============================================
# Script para crear la base de datos en PostgreSQL
# ============================================

# Colores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Variables de configuración
DB_NAME="tienda_pos"
DB_USER="postgres"
DB_HOST="localhost"
DB_PORT="5432"

echo -e "${YELLOW}========================================${NC}"
echo -e "${YELLOW}Creando base de datos PostgreSQL${NC}"
echo -e "${YELLOW}========================================${NC}"

# Verificar si PostgreSQL está instalado
if ! command -v psql &> /dev/null; then
    echo -e "${RED}Error: PostgreSQL no está instalado o no está en el PATH${NC}"
    exit 1
fi

# Crear la base de datos
echo -e "${GREEN}Creando base de datos: ${DB_NAME}...${NC}"
createdb -U ${DB_USER} -h ${DB_HOST} -p ${DB_PORT} ${DB_NAME} 2>/dev/null

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Base de datos '${DB_NAME}' creada exitosamente${NC}"
elif [ $? -eq 1 ]; then
    echo -e "${YELLOW}⚠ La base de datos '${DB_NAME}' ya existe${NC}"
else
    echo -e "${RED}✗ Error al crear la base de datos${NC}"
    exit 1
fi

# Ejecutar el script de esquema
echo -e "${GREEN}Ejecutando script de esquema...${NC}"
psql -U ${DB_USER} -h ${DB_HOST} -p ${DB_PORT} -d ${DB_NAME} -f database/schema.sql

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Esquema creado exitosamente${NC}"
    echo -e "${GREEN}========================================${NC}"
    echo -e "${GREEN}Base de datos lista para usar${NC}"
    echo -e "${GREEN}========================================${NC}"
else
    echo -e "${RED}✗ Error al ejecutar el script de esquema${NC}"
    exit 1
fi


