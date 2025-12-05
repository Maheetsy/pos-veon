# ============================================
# Script PowerShell para crear la base de datos en PostgreSQL
# ============================================

# Variables de configuración
$DB_NAME = "tienda_pos"
$DB_USER = "postgres"
$DB_HOST = "localhost"
$DB_PORT = "5432"

Write-Host "========================================" -ForegroundColor Yellow
Write-Host "Creando base de datos PostgreSQL" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Yellow

# Verificar si psql está disponible
try {
    $null = Get-Command psql -ErrorAction Stop
} catch {
    Write-Host "Error: PostgreSQL no está instalado o no está en el PATH" -ForegroundColor Red
    Write-Host "Asegúrate de tener PostgreSQL instalado y agregado al PATH" -ForegroundColor Yellow
    exit 1
}

# Crear la base de datos
Write-Host "Creando base de datos: $DB_NAME..." -ForegroundColor Green

$env:PGPASSWORD = Read-Host "Ingresa la contraseña de PostgreSQL para el usuario $DB_USER" -AsSecureString | ConvertFrom-SecureString -AsPlainText

$createDbCommand = "createdb -U $DB_USER -h $DB_HOST -p $DB_PORT $DB_NAME 2>&1"
$result = Invoke-Expression $createDbCommand

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Base de datos '$DB_NAME' creada exitosamente" -ForegroundColor Green
} elseif ($result -match "already exists") {
    Write-Host "⚠ La base de datos '$DB_NAME' ya existe" -ForegroundColor Yellow
} else {
    Write-Host "✗ Error al crear la base de datos: $result" -ForegroundColor Red
    exit 1
}

# Ejecutar el script de esquema
Write-Host "Ejecutando script de esquema..." -ForegroundColor Green

$schemaScript = Join-Path $PSScriptRoot "schema.sql"
if (-not (Test-Path $schemaScript)) {
    Write-Host "✗ No se encontró el archivo schema.sql en: $schemaScript" -ForegroundColor Red
    exit 1
}

$env:PGPASSWORD = Read-Host "Ingresa nuevamente la contraseña de PostgreSQL" -AsSecureString | ConvertFrom-SecureString -AsPlainText

$runSchemaCommand = "psql -U $DB_USER -h $DB_HOST -p $DB_PORT -d $DB_NAME -f `"$schemaScript`" 2>&1"
$schemaResult = Invoke-Expression $runSchemaCommand

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Esquema creado exitosamente" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "Base de datos lista para usar" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
} else {
    Write-Host "✗ Error al ejecutar el script de esquema: $schemaResult" -ForegroundColor Red
    exit 1
}

# Limpiar variable de entorno
Remove-Item Env:\PGPASSWORD -ErrorAction SilentlyContinue

