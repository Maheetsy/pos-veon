"""
Seeder para cargar datos iniciales de categorías y productos
Ejecutar con: python -m app.seeders.seed_data
"""
import sys
from pathlib import Path

# Agregar el directorio raíz al path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from sqlalchemy.orm import Session
from app.config.database import SessionLocal, engine
from app.models.category_model import Category
from app.models.product_model import Product
from app.config.database import Base
import random

# Crear tablas
Base.metadata.create_all(bind=engine)

# Datos de categorías
CATEGORIES_DATA = [
    {"name": "Electrónica", "description": "Dispositivos electrónicos y accesorios"},
    {"name": "Alimentos y Bebidas", "description": "Productos alimenticios y bebidas"},
    {"name": "Ropa y Accesorios", "description": "Prendas de vestir y complementos"},
    {"name": "Hogar y Jardín", "description": "Artículos para el hogar y jardín"},
    {"name": "Deportes y Fitness", "description": "Equipamiento deportivo y fitness"},
    {"name": "Libros y Papelería", "description": "Libros, cuadernos y material de oficina"},
    {"name": "Juguetes y Juegos", "description": "Juguetes y juegos para todas las edades"},
    {"name": "Salud y Belleza", "description": "Productos de cuidado personal y belleza"},
    {"name": "Automotriz", "description": "Repuestos y accesorios para vehículos"},
    {"name": "Mascotas", "description": "Alimentos y accesorios para mascotas"},
]

# Datos de productos (más de 250 productos)
PRODUCTS_DATA = [
    # Electrónica
    {"name": "Smartphone Samsung Galaxy S21", "short_description": "Teléfono inteligente 128GB", "sku": "ELEC-001", "cost": 450.00, "sale_price": 699.99, "stock": 25, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-001", "provider_name": "Tech Distributors", "image_path": "/images/electronics/samsung-s21.jpg", "category_name": "Electrónica"},
    {"name": "iPhone 13 Pro", "short_description": "Teléfono inteligente Apple 256GB", "sku": "ELEC-002", "cost": 800.00, "sale_price": 1199.99, "stock": 15, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-002", "provider_name": "Apple Store", "image_path": "/images/electronics/iphone13.jpg", "category_name": "Electrónica"},
    {"name": "Laptop Dell XPS 15", "short_description": "Laptop 15 pulgadas Intel i7", "sku": "ELEC-003", "cost": 1200.00, "sale_price": 1799.99, "stock": 10, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-003", "provider_name": "Dell Technologies", "image_path": "/images/electronics/dell-xps.jpg", "category_name": "Electrónica"},
    {"name": "Auriculares Sony WH-1000XM4", "short_description": "Auriculares inalámbricos con cancelación de ruido", "sku": "ELEC-004", "cost": 250.00, "sale_price": 349.99, "stock": 30, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-001", "provider_name": "Tech Distributors", "image_path": "/images/electronics/sony-headphones.jpg", "category_name": "Electrónica"},
    {"name": "Tablet iPad Air", "short_description": "Tablet Apple 64GB", "sku": "ELEC-005", "cost": 450.00, "sale_price": 599.99, "stock": 20, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-002", "provider_name": "Apple Store", "image_path": "/images/electronics/ipad-air.jpg", "category_name": "Electrónica"},
    {"name": "Smartwatch Apple Watch Series 7", "short_description": "Reloj inteligente 45mm", "sku": "ELEC-006", "cost": 300.00, "sale_price": 429.99, "stock": 18, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-002", "provider_name": "Apple Store", "image_path": "/images/electronics/apple-watch.jpg", "category_name": "Electrónica"},
    {"name": "Cargador Inalámbrico Samsung", "short_description": "Cargador rápido 15W", "sku": "ELEC-007", "cost": 25.00, "sale_price": 39.99, "stock": 50, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-001", "provider_name": "Tech Distributors", "image_path": "/images/electronics/wireless-charger.jpg", "category_name": "Electrónica"},
    {"name": "Cable USB-C 2m", "short_description": "Cable de carga rápida", "sku": "ELEC-008", "cost": 8.00, "sale_price": 14.99, "stock": 100, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-004", "provider_name": "Cable Express", "image_path": "/images/electronics/usb-cable.jpg", "category_name": "Electrónica"},
    {"name": "Mouse Logitech MX Master 3", "short_description": "Mouse inalámbrico ergonómico", "sku": "ELEC-009", "cost": 60.00, "sale_price": 99.99, "stock": 35, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-005", "provider_name": "Logitech Store", "image_path": "/images/electronics/logitech-mouse.jpg", "category_name": "Electrónica"},
    {"name": "Teclado Mecánico RGB", "short_description": "Teclado gaming con iluminación RGB", "sku": "ELEC-010", "cost": 80.00, "sale_price": 129.99, "stock": 28, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-005", "provider_name": "Logitech Store", "image_path": "/images/electronics/rgb-keyboard.jpg", "category_name": "Electrónica"},
    {"name": "Monitor LG 27 pulgadas 4K", "short_description": "Monitor IPS 27 pulgadas", "sku": "ELEC-011", "cost": 350.00, "sale_price": 499.99, "stock": 12, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-006", "provider_name": "LG Electronics", "image_path": "/images/electronics/lg-monitor.jpg", "category_name": "Electrónica"},
    {"name": "Webcam Logitech C920", "short_description": "Cámara web Full HD 1080p", "sku": "ELEC-012", "cost": 50.00, "sale_price": 79.99, "stock": 40, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-005", "provider_name": "Logitech Store", "image_path": "/images/electronics/webcam.jpg", "category_name": "Electrónica"},
    {"name": "Altavoz Bluetooth JBL Flip 5", "short_description": "Altavoz portátil resistente al agua", "sku": "ELEC-013", "cost": 70.00, "sale_price": 119.99, "stock": 22, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-007", "provider_name": "JBL Audio", "image_path": "/images/electronics/jbl-speaker.jpg", "category_name": "Electrónica"},
    {"name": "Cámara GoPro Hero 10", "short_description": "Cámara de acción 4K", "sku": "ELEC-014", "cost": 350.00, "sale_price": 499.99, "stock": 8, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-008", "provider_name": "GoPro Store", "image_path": "/images/electronics/gopro.jpg", "category_name": "Electrónica"},
    {"name": "Router WiFi 6 TP-Link", "short_description": "Router inalámbrico AX3000", "sku": "ELEC-015", "cost": 90.00, "sale_price": 149.99, "stock": 15, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-009", "provider_name": "TP-Link", "image_path": "/images/electronics/router.jpg", "category_name": "Electrónica"},
    
    # Alimentos y Bebidas
    {"name": "Arroz Premium 5kg", "short_description": "Arroz de grano largo", "sku": "FOOD-001", "cost": 4.50, "sale_price": 7.99, "stock": 200, "unit": "1", "unit_of_measurement": "bolsa", "provider_id": "PROV-010", "provider_name": "Alimentos del Valle", "image_path": "/images/food/rice.jpg", "category_name": "Alimentos y Bebidas"},
    {"name": "Aceite de Oliva Extra Virgen 1L", "short_description": "Aceite de oliva premium", "sku": "FOOD-002", "cost": 8.00, "sale_price": 14.99, "stock": 150, "unit": "1", "unit_of_measurement": "botella", "provider_id": "PROV-011", "provider_name": "Aceites Premium", "image_path": "/images/food/olive-oil.jpg", "category_name": "Alimentos y Bebidas"},
    {"name": "Leche Entera 1L", "short_description": "Leche fresca pasteurizada", "sku": "FOOD-003", "cost": 1.20, "sale_price": 2.49, "stock": 300, "unit": "1", "unit_of_measurement": "cartón", "provider_id": "PROV-012", "provider_name": "Lácteos Frescos", "image_path": "/images/food/milk.jpg", "category_name": "Alimentos y Bebidas"},
    {"name": "Huevos Grade A x12", "short_description": "Docena de huevos frescos", "sku": "FOOD-004", "cost": 2.50, "sale_price": 4.99, "stock": 250, "unit": "1", "unit_of_measurement": "docena", "provider_id": "PROV-013", "provider_name": "Granja San José", "image_path": "/images/food/eggs.jpg", "category_name": "Alimentos y Bebidas"},
    {"name": "Pan Integral 500g", "short_description": "Pan de molde integral", "sku": "FOOD-005", "cost": 1.80, "sale_price": 3.49, "stock": 180, "unit": "1", "unit_of_measurement": "bolsa", "provider_id": "PROV-014", "provider_name": "Panadería Artesanal", "image_path": "/images/food/bread.jpg", "category_name": "Alimentos y Bebidas"},
    {"name": "Café Molido 500g", "short_description": "Café 100% arábica", "sku": "FOOD-006", "cost": 6.00, "sale_price": 11.99, "stock": 120, "unit": "1", "unit_of_measurement": "bolsa", "provider_id": "PROV-015", "provider_name": "Café Premium", "image_path": "/images/food/coffee.jpg", "category_name": "Alimentos y Bebidas"},
    {"name": "Azúcar Blanca 1kg", "short_description": "Azúcar refinada", "sku": "FOOD-007", "cost": 1.50, "sale_price": 2.99, "stock": 220, "unit": "1", "unit_of_measurement": "bolsa", "provider_id": "PROV-016", "provider_name": "Dulces del Sur", "image_path": "/images/food/sugar.jpg", "category_name": "Alimentos y Bebidas"},
    {"name": "Sal de Mesa 1kg", "short_description": "Sal yodada", "sku": "FOOD-008", "cost": 0.80, "sale_price": 1.49, "stock": 280, "unit": "1", "unit_of_measurement": "bolsa", "provider_id": "PROV-017", "provider_name": "Salinas del Norte", "image_path": "/images/food/salt.jpg", "category_name": "Alimentos y Bebidas"},
    {"name": "Pasta Spaghetti 500g", "short_description": "Pasta italiana de trigo duro", "sku": "FOOD-009", "cost": 1.20, "sale_price": 2.49, "stock": 200, "unit": "1", "unit_of_measurement": "paquete", "provider_id": "PROV-018", "provider_name": "Pastas Italianas", "image_path": "/images/food/pasta.jpg", "category_name": "Alimentos y Bebidas"},
    {"name": "Salsa de Tomate 400g", "short_description": "Salsa de tomate natural", "sku": "FOOD-010", "cost": 1.00, "sale_price": 1.99, "stock": 190, "unit": "1", "unit_of_measurement": "lata", "provider_id": "PROV-019", "provider_name": "Conservas del Campo", "image_path": "/images/food/tomato-sauce.jpg", "category_name": "Alimentos y Bebidas"},
    {"name": "Atún en Lata 160g", "short_description": "Atún en agua", "sku": "FOOD-011", "cost": 1.50, "sale_price": 2.99, "stock": 170, "unit": "1", "unit_of_measurement": "lata", "provider_id": "PROV-020", "provider_name": "Pescados del Mar", "image_path": "/images/food/tuna.jpg", "category_name": "Alimentos y Bebidas"},
    {"name": "Agua Mineral 1.5L", "short_description": "Agua mineral natural", "sku": "FOOD-012", "cost": 0.60, "sale_price": 1.29, "stock": 400, "unit": "1", "unit_of_measurement": "botella", "provider_id": "PROV-021", "provider_name": "Aguas Puras", "image_path": "/images/food/water.jpg", "category_name": "Alimentos y Bebidas"},
    {"name": "Refresco Cola 2L", "short_description": "Bebida gaseosa", "sku": "FOOD-013", "cost": 1.20, "sale_price": 2.49, "stock": 180, "unit": "1", "unit_of_measurement": "botella", "provider_id": "PROV-022", "provider_name": "Bebidas Refrescantes", "image_path": "/images/food/cola.jpg", "category_name": "Alimentos y Bebidas"},
    {"name": "Jugo de Naranja 1L", "short_description": "Jugo 100% natural", "sku": "FOOD-014", "cost": 2.00, "sale_price": 3.99, "stock": 140, "unit": "1", "unit_of_measurement": "cartón", "provider_id": "PROV-023", "provider_name": "Jugos Naturales", "image_path": "/images/food/orange-juice.jpg", "category_name": "Alimentos y Bebidas"},
    {"name": "Yogur Natural 1kg", "short_description": "Yogur griego natural", "sku": "FOOD-015", "cost": 3.50, "sale_price": 6.99, "stock": 160, "unit": "1", "unit_of_measurement": "envase", "provider_id": "PROV-012", "provider_name": "Lácteos Frescos", "image_path": "/images/food/yogurt.jpg", "category_name": "Alimentos y Bebidas"},
    {"name": "Queso Cheddar 250g", "short_description": "Queso cheddar en lonchas", "sku": "FOOD-016", "cost": 4.00, "sale_price": 7.99, "stock": 130, "unit": "1", "unit_of_measurement": "paquete", "provider_id": "PROV-012", "provider_name": "Lácteos Frescos", "image_path": "/images/food/cheese.jpg", "category_name": "Alimentos y Bebidas"},
    {"name": "Mantequilla 250g", "short_description": "Mantequilla sin sal", "sku": "FOOD-017", "cost": 2.50, "sale_price": 4.99, "stock": 150, "unit": "1", "unit_of_measurement": "paquete", "provider_id": "PROV-012", "provider_name": "Lácteos Frescos", "image_path": "/images/food/butter.jpg", "category_name": "Alimentos y Bebidas"},
    {"name": "Mermelada de Fresa 350g", "short_description": "Mermelada artesanal", "sku": "FOOD-018", "cost": 2.20, "sale_price": 4.49, "stock": 110, "unit": "1", "unit_of_measurement": "frasco", "provider_id": "PROV-024", "provider_name": "Dulces Artesanales", "image_path": "/images/food/jam.jpg", "category_name": "Alimentos y Bebidas"},
    {"name": "Miel de Abeja 500g", "short_description": "Miel pura de abeja", "sku": "FOOD-019", "cost": 5.00, "sale_price": 9.99, "stock": 90, "unit": "1", "unit_of_measurement": "frasco", "provider_id": "PROV-025", "provider_name": "Apiarios del Campo", "image_path": "/images/food/honey.jpg", "category_name": "Alimentos y Bebidas"},
    {"name": "Cereal de Avena 500g", "short_description": "Cereal integral con avena", "sku": "FOOD-020", "cost": 3.00, "sale_price": 5.99, "stock": 100, "unit": "1", "unit_of_measurement": "caja", "provider_id": "PROV-026", "provider_name": "Cereales Saludables", "image_path": "/images/food/cereal.jpg", "category_name": "Alimentos y Bebidas"},
    
    # Ropa y Accesorios
    {"name": "Camiseta Básica Algodón", "short_description": "Camiseta 100% algodón", "sku": "CLOTH-001", "cost": 8.00, "sale_price": 19.99, "stock": 80, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-027", "provider_name": "Textiles Modernos", "image_path": "/images/clothing/tshirt.jpg", "category_name": "Ropa y Accesorios"},
    {"name": "Jeans Clásicos", "short_description": "Pantalón vaquero azul", "sku": "CLOTH-002", "cost": 25.00, "sale_price": 59.99, "stock": 60, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-028", "provider_name": "Denim Factory", "image_path": "/images/clothing/jeans.jpg", "category_name": "Ropa y Accesorios"},
    {"name": "Zapatillas Deportivas", "short_description": "Zapatillas running", "sku": "CLOTH-003", "cost": 40.00, "sale_price": 89.99, "stock": 45, "unit": "1", "unit_of_measurement": "par", "provider_id": "PROV-029", "provider_name": "Sport Shoes Co", "image_path": "/images/clothing/sneakers.jpg", "category_name": "Ropa y Accesorios"},
    {"name": "Chaqueta Impermeable", "short_description": "Chaqueta resistente al agua", "sku": "CLOTH-004", "cost": 35.00, "sale_price": 79.99, "stock": 35, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-030", "provider_name": "Outdoor Gear", "image_path": "/images/clothing/jacket.jpg", "category_name": "Ropa y Accesorios"},
    {"name": "Vestido Casual", "short_description": "Vestido de verano", "sku": "CLOTH-005", "cost": 20.00, "sale_price": 49.99, "stock": 50, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-031", "provider_name": "Fashion Store", "image_path": "/images/clothing/dress.jpg", "category_name": "Ropa y Accesorios"},
    {"name": "Bufanda de Lana", "short_description": "Bufanda tejida a mano", "sku": "CLOTH-006", "cost": 12.00, "sale_price": 24.99, "stock": 70, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-032", "provider_name": "Accesorios de Lana", "image_path": "/images/clothing/scarf.jpg", "category_name": "Ropa y Accesorios"},
    {"name": "Gorra Deportiva", "short_description": "Gorra ajustable", "sku": "CLOTH-007", "cost": 8.00, "sale_price": 16.99, "stock": 90, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-033", "provider_name": "Headwear Co", "image_path": "/images/clothing/cap.jpg", "category_name": "Ropa y Accesorios"},
    {"name": "Cinturón de Cuero", "short_description": "Cinturón genuino", "sku": "CLOTH-008", "cost": 15.00, "sale_price": 34.99, "stock": 55, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-034", "provider_name": "Leather Goods", "image_path": "/images/clothing/belt.jpg", "category_name": "Ropa y Accesorios"},
    {"name": "Calcetines Pack x3", "short_description": "Pack de calcetines deportivos", "sku": "CLOTH-009", "cost": 6.00, "sale_price": 12.99, "stock": 120, "unit": "1", "unit_of_measurement": "pack", "provider_id": "PROV-035", "provider_name": "Socks Factory", "image_path": "/images/clothing/socks.jpg", "category_name": "Ropa y Accesorios"},
    {"name": "Bolso de Mano", "short_description": "Bolso de cuero sintético", "sku": "CLOTH-010", "cost": 18.00, "sale_price": 39.99, "stock": 40, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-036", "provider_name": "Bags & More", "image_path": "/images/clothing/handbag.jpg", "category_name": "Ropa y Accesorios"},
    
    # Hogar y Jardín
    {"name": "Sábanas de Algodón Queen", "short_description": "Juego de sábanas 4 piezas", "sku": "HOME-001", "cost": 25.00, "sale_price": 49.99, "stock": 30, "unit": "1", "unit_of_measurement": "juego", "provider_id": "PROV-037", "provider_name": "Textiles del Hogar", "image_path": "/images/home/sheets.jpg", "category_name": "Hogar y Jardín"},
    {"name": "Almohada Ortopédica", "short_description": "Almohada con memoria", "sku": "HOME-002", "cost": 20.00, "sale_price": 39.99, "stock": 50, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-038", "provider_name": "Comfort Sleep", "image_path": "/images/home/pillow.jpg", "category_name": "Hogar y Jardín"},
    {"name": "Toalla de Baño", "short_description": "Toalla de algodón egipcio", "sku": "HOME-003", "cost": 12.00, "sale_price": 24.99, "stock": 65, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-037", "provider_name": "Textiles del Hogar", "image_path": "/images/home/towel.jpg", "category_name": "Hogar y Jardín"},
    {"name": "Cortinas Blackout", "short_description": "Cortinas opacas 2x2m", "sku": "HOME-004", "cost": 30.00, "sale_price": 59.99, "stock": 25, "unit": "1", "unit_of_measurement": "par", "provider_id": "PROV-039", "provider_name": "Decoración del Hogar", "image_path": "/images/home/curtains.jpg", "category_name": "Hogar y Jardín"},
    {"name": "Lámpara de Mesa LED", "short_description": "Lámpara moderna con USB", "sku": "HOME-005", "cost": 15.00, "sale_price": 29.99, "stock": 40, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-040", "provider_name": "Iluminación Moderna", "image_path": "/images/home/lamp.jpg", "category_name": "Hogar y Jardín"},
    {"name": "Maceta de Cerámica 20cm", "short_description": "Maceta decorativa", "sku": "HOME-006", "cost": 8.00, "sale_price": 16.99, "stock": 70, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-041", "provider_name": "Jardinería Plus", "image_path": "/images/home/pot.jpg", "category_name": "Hogar y Jardín"},
    {"name": "Tierra para Macetas 10L", "short_description": "Sustrato universal", "sku": "HOME-007", "cost": 5.00, "sale_price": 9.99, "stock": 85, "unit": "1", "unit_of_measurement": "bolsa", "provider_id": "PROV-041", "provider_name": "Jardinería Plus", "image_path": "/images/home/soil.jpg", "category_name": "Hogar y Jardín"},
    {"name": "Regadera de Plástico 5L", "short_description": "Regadera para jardín", "sku": "HOME-008", "cost": 6.00, "sale_price": 12.99, "stock": 55, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-041", "provider_name": "Jardinería Plus", "image_path": "/images/home/watering-can.jpg", "category_name": "Hogar y Jardín"},
    {"name": "Cojín Decorativo 40x40cm", "short_description": "Cojín de algodón", "sku": "HOME-009", "cost": 10.00, "sale_price": 19.99, "stock": 60, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-037", "provider_name": "Textiles del Hogar", "image_path": "/images/home/cushion.jpg", "category_name": "Hogar y Jardín"},
    {"name": "Organizador de Escritorio", "short_description": "Organizador de plástico", "sku": "HOME-010", "cost": 7.00, "sale_price": 14.99, "stock": 45, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-042", "provider_name": "Organización Plus", "image_path": "/images/home/organizer.jpg", "category_name": "Hogar y Jardín"},
    
    # Deportes y Fitness
    {"name": "Pelota de Fútbol", "short_description": "Pelota oficial tamaño 5", "sku": "SPORT-001", "cost": 15.00, "sale_price": 29.99, "stock": 50, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-043", "provider_name": "Sports Equipment", "image_path": "/images/sports/soccer-ball.jpg", "category_name": "Deportes y Fitness"},
    {"name": "Raqueta de Tenis", "short_description": "Raqueta profesional", "sku": "SPORT-002", "cost": 50.00, "sale_price": 99.99, "stock": 20, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-044", "provider_name": "Tennis Pro", "image_path": "/images/sports/tennis-racket.jpg", "category_name": "Deportes y Fitness"},
    {"name": "Mancuernas Ajustables 2x10kg", "short_description": "Par de mancuernas", "sku": "SPORT-003", "cost": 40.00, "sale_price": 79.99, "stock": 30, "unit": "1", "unit_of_measurement": "par", "provider_id": "PROV-045", "provider_name": "Fitness Equipment", "image_path": "/images/sports/dumbbells.jpg", "category_name": "Deportes y Fitness"},
    {"name": "Colchoneta de Yoga", "short_description": "Colchoneta antideslizante", "sku": "SPORT-004", "cost": 12.00, "sale_price": 24.99, "stock": 60, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-046", "provider_name": "Yoga Essentials", "image_path": "/images/sports/yoga-mat.jpg", "category_name": "Deportes y Fitness"},
    {"name": "Bicicleta Estática", "short_description": "Bicicleta de ejercicio", "sku": "SPORT-005", "cost": 200.00, "sale_price": 399.99, "stock": 8, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-045", "provider_name": "Fitness Equipment", "image_path": "/images/sports/exercise-bike.jpg", "category_name": "Deportes y Fitness"},
    {"name": "Cuerda para Saltar", "short_description": "Cuerda de velocidad", "sku": "SPORT-006", "cost": 5.00, "sale_price": 9.99, "stock": 80, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-045", "provider_name": "Fitness Equipment", "image_path": "/images/sports/jump-rope.jpg", "category_name": "Deportes y Fitness"},
    {"name": "Balón de Baloncesto", "short_description": "Balón oficial tamaño 7", "sku": "SPORT-007", "cost": 18.00, "sale_price": 34.99, "stock": 35, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-043", "provider_name": "Sports Equipment", "image_path": "/images/sports/basketball.jpg", "category_name": "Deportes y Fitness"},
    {"name": "Guantes de Boxeo", "short_description": "Guantes de entrenamiento", "sku": "SPORT-008", "cost": 25.00, "sale_price": 49.99, "stock": 25, "unit": "1", "unit_of_measurement": "par", "provider_id": "PROV-047", "provider_name": "Combat Sports", "image_path": "/images/sports/boxing-gloves.jpg", "category_name": "Deportes y Fitness"},
    {"name": "Mochila Deportiva", "short_description": "Mochila para gimnasio", "sku": "SPORT-009", "cost": 20.00, "sale_price": 39.99, "stock": 40, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-048", "provider_name": "Sport Bags", "image_path": "/images/sports/gym-bag.jpg", "category_name": "Deportes y Fitness"},
    {"name": "Botella Deportiva 750ml", "short_description": "Botella de acero inoxidable", "sku": "SPORT-010", "cost": 8.00, "sale_price": 16.99, "stock": 70, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-049", "provider_name": "Hydration Plus", "image_path": "/images/sports/water-bottle.jpg", "category_name": "Deportes y Fitness"},
    
    # Libros y Papelería
    {"name": "Cuaderno Universitario 100 hojas", "short_description": "Cuaderno rayado", "sku": "BOOK-001", "cost": 2.50, "sale_price": 4.99, "stock": 150, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-050", "provider_name": "Papelería Central", "image_path": "/images/books/notebook.jpg", "category_name": "Libros y Papelería"},
    {"name": "Bolígrafo Pack x10", "short_description": "Pack de bolígrafos azules", "sku": "BOOK-002", "cost": 3.00, "sale_price": 5.99, "stock": 200, "unit": "1", "unit_of_measurement": "pack", "provider_id": "PROV-050", "provider_name": "Papelería Central", "image_path": "/images/books/pens.jpg", "category_name": "Libros y Papelería"},
    {"name": "Lápices HB Pack x12", "short_description": "Pack de lápices", "sku": "BOOK-003", "cost": 2.00, "sale_price": 3.99, "stock": 180, "unit": "1", "unit_of_measurement": "pack", "provider_id": "PROV-050", "provider_name": "Papelería Central", "image_path": "/images/books/pencils.jpg", "category_name": "Libros y Papelería"},
    {"name": "Resaltadores Pack x5", "short_description": "Resaltadores fluorescentes", "sku": "BOOK-004", "cost": 4.00, "sale_price": 7.99, "stock": 120, "unit": "1", "unit_of_measurement": "pack", "provider_id": "PROV-050", "provider_name": "Papelería Central", "image_path": "/images/books/highlighters.jpg", "category_name": "Libros y Papelería"},
    {"name": "Carpeta con Anillas A4", "short_description": "Carpeta de plástico", "sku": "BOOK-005", "cost": 3.50, "sale_price": 6.99, "stock": 100, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-050", "provider_name": "Papelería Central", "image_path": "/images/books/binder.jpg", "category_name": "Libros y Papelería"},
    {"name": "Libro: El Quijote", "short_description": "Edición clásica", "sku": "BOOK-006", "cost": 8.00, "sale_price": 15.99, "stock": 40, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-051", "provider_name": "Editorial Clásica", "image_path": "/images/books/quijote.jpg", "category_name": "Libros y Papelería"},
    {"name": "Libro: Cien Años de Soledad", "short_description": "Novela de García Márquez", "sku": "BOOK-007", "cost": 9.00, "sale_price": 17.99, "stock": 35, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-051", "provider_name": "Editorial Clásica", "image_path": "/images/books/cien-anos.jpg", "category_name": "Libros y Papelería"},
    {"name": "Calculadora Científica", "short_description": "Calculadora con funciones avanzadas", "sku": "BOOK-008", "cost": 12.00, "sale_price": 24.99, "stock": 55, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-052", "provider_name": "Electrónica Educativa", "image_path": "/images/books/calculator.jpg", "category_name": "Libros y Papelería"},
    {"name": "Regla de 30cm", "short_description": "Regla de plástico transparente", "sku": "BOOK-009", "cost": 1.00, "sale_price": 1.99, "stock": 250, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-050", "provider_name": "Papelería Central", "image_path": "/images/books/ruler.jpg", "category_name": "Libros y Papelería"},
    {"name": "Goma de Borrar", "short_description": "Goma blanca estándar", "sku": "BOOK-010", "cost": 0.50, "sale_price": 0.99, "stock": 300, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-050", "provider_name": "Papelería Central", "image_path": "/images/books/eraser.jpg", "category_name": "Libros y Papelería"},
    
    # Juguetes y Juegos
    {"name": "Lego Classic 10696", "short_description": "Set de construcción básico", "sku": "TOY-001", "cost": 30.00, "sale_price": 59.99, "stock": 25, "unit": "1", "unit_of_measurement": "caja", "provider_id": "PROV-053", "provider_name": "Toy Distributors", "image_path": "/images/toys/lego.jpg", "category_name": "Juguetes y Juegos"},
    {"name": "Muñeca Barbie", "short_description": "Muñeca clásica", "sku": "TOY-002", "cost": 15.00, "sale_price": 29.99, "stock": 40, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-053", "provider_name": "Toy Distributors", "image_path": "/images/toys/barbie.jpg", "category_name": "Juguetes y Juegos"},
    {"name": "Coche de Juguete RC", "short_description": "Coche teledirigido", "sku": "TOY-003", "cost": 25.00, "sale_price": 49.99, "stock": 30, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-054", "provider_name": "RC Toys", "image_path": "/images/toys/rc-car.jpg", "category_name": "Juguetes y Juegos"},
    {"name": "Puzzle 1000 Piezas", "short_description": "Puzzle de paisaje", "sku": "TOY-004", "cost": 12.00, "sale_price": 24.99, "stock": 35, "unit": "1", "unit_of_measurement": "caja", "provider_id": "PROV-055", "provider_name": "Puzzle Masters", "image_path": "/images/toys/puzzle.jpg", "category_name": "Juguetes y Juegos"},
    {"name": "Juego de Mesa Monopoly", "short_description": "Juego clásico de mesa", "sku": "TOY-005", "cost": 20.00, "sale_price": 39.99, "stock": 28, "unit": "1", "unit_of_measurement": "caja", "provider_id": "PROV-056", "provider_name": "Board Games Co", "image_path": "/images/toys/monopoly.jpg", "category_name": "Juguetes y Juegos"},
    {"name": "Pelota de Playa", "short_description": "Pelota inflable", "sku": "TOY-006", "cost": 5.00, "sale_price": 9.99, "stock": 60, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-057", "provider_name": "Beach Toys", "image_path": "/images/toys/beach-ball.jpg", "category_name": "Juguetes y Juegos"},
    {"name": "Figura de Acción", "short_description": "Figura articulada", "sku": "TOY-007", "cost": 10.00, "sale_price": 19.99, "stock": 50, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-053", "provider_name": "Toy Distributors", "image_path": "/images/toys/action-figure.jpg", "category_name": "Juguetes y Juegos"},
    {"name": "Juego de Construcción Magnético", "short_description": "Bloques magnéticos", "sku": "TOY-008", "cost": 35.00, "sale_price": 69.99, "stock": 20, "unit": "1", "unit_of_measurement": "caja", "provider_id": "PROV-058", "provider_name": "Educational Toys", "image_path": "/images/toys/magnetic-blocks.jpg", "category_name": "Juguetes y Juegos"},
    {"name": "Peluche Oso de Peluche", "short_description": "Oso de peluche suave", "sku": "TOY-009", "cost": 12.00, "sale_price": 24.99, "stock": 45, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-059", "provider_name": "Plush Toys", "image_path": "/images/toys/teddy-bear.jpg", "category_name": "Juguetes y Juegos"},
    {"name": "Juego de Cartas UNO", "short_description": "Juego de cartas clásico", "sku": "TOY-010", "cost": 6.00, "sale_price": 11.99, "stock": 70, "unit": "1", "unit_of_measurement": "caja", "provider_id": "PROV-056", "provider_name": "Board Games Co", "image_path": "/images/toys/uno.jpg", "category_name": "Juguetes y Juegos"},
    
    # Salud y Belleza
    {"name": "Champú Hidratante 400ml", "short_description": "Champú para cabello seco", "sku": "BEAUTY-001", "cost": 5.00, "sale_price": 9.99, "stock": 100, "unit": "1", "unit_of_measurement": "botella", "provider_id": "PROV-060", "provider_name": "Cosmetics Plus", "image_path": "/images/beauty/shampoo.jpg", "category_name": "Salud y Belleza"},
    {"name": "Acondicionador 400ml", "short_description": "Acondicionador reparador", "sku": "BEAUTY-002", "cost": 5.00, "sale_price": 9.99, "stock": 95, "unit": "1", "unit_of_measurement": "botella", "provider_id": "PROV-060", "provider_name": "Cosmetics Plus", "image_path": "/images/beauty/conditioner.jpg", "category_name": "Salud y Belleza"},
    {"name": "Jabón de Glicerina x3", "short_description": "Pack de jabones naturales", "sku": "BEAUTY-003", "cost": 4.00, "sale_price": 7.99, "stock": 110, "unit": "1", "unit_of_measurement": "pack", "provider_id": "PROV-061", "provider_name": "Natural Soaps", "image_path": "/images/beauty/soap.jpg", "category_name": "Salud y Belleza"},
    {"name": "Crema Hidratante Facial 50ml", "short_description": "Crema con SPF 30", "sku": "BEAUTY-004", "cost": 8.00, "sale_price": 15.99, "stock": 80, "unit": "1", "unit_of_measurement": "tubo", "provider_id": "PROV-062", "provider_name": "Skincare Pro", "image_path": "/images/beauty/face-cream.jpg", "category_name": "Salud y Belleza"},
    {"name": "Desodorante Roll-On 50ml", "short_description": "Desodorante 48h", "sku": "BEAUTY-005", "cost": 3.00, "sale_price": 5.99, "stock": 150, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-063", "provider_name": "Personal Care", "image_path": "/images/beauty/deodorant.jpg", "category_name": "Salud y Belleza"},
    {"name": "Cepillo de Dientes Eléctrico", "short_description": "Cepillo recargable", "sku": "BEAUTY-006", "cost": 25.00, "sale_price": 49.99, "stock": 40, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-064", "provider_name": "Oral Care", "image_path": "/images/beauty/electric-toothbrush.jpg", "category_name": "Salud y Belleza"},
    {"name": "Pasta Dental 100ml", "short_description": "Pasta dental con flúor", "sku": "BEAUTY-007", "cost": 2.50, "sale_price": 4.99, "stock": 180, "unit": "1", "unit_of_measurement": "tubo", "provider_id": "PROV-064", "provider_name": "Oral Care", "image_path": "/images/beauty/toothpaste.jpg", "category_name": "Salud y Belleza"},
    {"name": "Perfume 50ml", "short_description": "Fragancia unisex", "sku": "BEAUTY-008", "cost": 20.00, "sale_price": 39.99, "stock": 35, "unit": "1", "unit_of_measurement": "botella", "provider_id": "PROV-065", "provider_name": "Fragrances Co", "image_path": "/images/beauty/perfume.jpg", "category_name": "Salud y Belleza"},
    {"name": "Protector Solar SPF 50 200ml", "short_description": "Protector solar resistente al agua", "sku": "BEAUTY-009", "cost": 12.00, "sale_price": 24.99, "stock": 60, "unit": "1", "unit_of_measurement": "botella", "provider_id": "PROV-062", "provider_name": "Skincare Pro", "image_path": "/images/beauty/sunscreen.jpg", "category_name": "Salud y Belleza"},
    {"name": "Mascarilla Facial x5", "short_description": "Pack de mascarillas hidratantes", "sku": "BEAUTY-010", "cost": 8.00, "sale_price": 15.99, "stock": 70, "unit": "1", "unit_of_measurement": "pack", "provider_id": "PROV-062", "provider_name": "Skincare Pro", "image_path": "/images/beauty/face-mask.jpg", "category_name": "Salud y Belleza"},
    
    # Automotriz
    {"name": "Aceite de Motor 5W-30 4L", "short_description": "Aceite sintético", "sku": "AUTO-001", "cost": 25.00, "sale_price": 49.99, "stock": 40, "unit": "1", "unit_of_measurement": "botella", "provider_id": "PROV-066", "provider_name": "Auto Parts Plus", "image_path": "/images/auto/motor-oil.jpg", "category_name": "Automotriz"},
    {"name": "Filtro de Aire", "short_description": "Filtro de aire estándar", "sku": "AUTO-002", "cost": 8.00, "sale_price": 15.99, "stock": 60, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-066", "provider_name": "Auto Parts Plus", "image_path": "/images/auto/air-filter.jpg", "category_name": "Automotriz"},
    {"name": "Bujías x4", "short_description": "Pack de bujías de iridio", "sku": "AUTO-003", "cost": 15.00, "sale_price": 29.99, "stock": 50, "unit": "1", "unit_of_measurement": "pack", "provider_id": "PROV-067", "provider_name": "Spark Plugs Co", "image_path": "/images/auto/spark-plugs.jpg", "category_name": "Automotriz"},
    {"name": "Líquido de Frenos 500ml", "short_description": "Líquido DOT 4", "sku": "AUTO-004", "cost": 6.00, "sale_price": 11.99, "stock": 45, "unit": "1", "unit_of_measurement": "botella", "provider_id": "PROV-066", "provider_name": "Auto Parts Plus", "image_path": "/images/auto/brake-fluid.jpg", "category_name": "Automotriz"},
    {"name": "Anticongelante 5L", "short_description": "Anticongelante concentrado", "sku": "AUTO-005", "cost": 12.00, "sale_price": 24.99, "stock": 35, "unit": "1", "unit_of_measurement": "botella", "provider_id": "PROV-068", "provider_name": "Cooling Systems", "image_path": "/images/auto/antifreeze.jpg", "category_name": "Automotriz"},
    {"name": "Batería de Coche 12V", "short_description": "Batería 60Ah", "sku": "AUTO-006", "cost": 80.00, "sale_price": 149.99, "stock": 15, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-069", "provider_name": "Battery Store", "image_path": "/images/auto/battery.jpg", "category_name": "Automotriz"},
    {"name": "Neumático 205/55R16", "short_description": "Neumático todo tiempo", "sku": "AUTO-007", "cost": 60.00, "sale_price": 119.99, "stock": 20, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-070", "provider_name": "Tire Center", "image_path": "/images/auto/tire.jpg", "category_name": "Automotriz"},
    {"name": "Pastillas de Freno Delanteras", "short_description": "Pastillas cerámicas", "sku": "AUTO-008", "cost": 35.00, "sale_price": 69.99, "stock": 25, "unit": "1", "unit_of_measurement": "juego", "provider_id": "PROV-071", "provider_name": "Brake Systems", "image_path": "/images/auto/brake-pads.jpg", "category_name": "Automotriz"},
    {"name": "Aceite de Transmisión 1L", "short_description": "Aceite ATF", "sku": "AUTO-009", "cost": 10.00, "sale_price": 19.99, "stock": 30, "unit": "1", "unit_of_measurement": "botella", "provider_id": "PROV-066", "provider_name": "Auto Parts Plus", "image_path": "/images/auto/transmission-oil.jpg", "category_name": "Automotriz"},
    {"name": "Fusibles Pack x10", "short_description": "Pack de fusibles 10A", "sku": "AUTO-010", "cost": 3.00, "sale_price": 5.99, "stock": 80, "unit": "1", "unit_of_measurement": "pack", "provider_id": "PROV-072", "provider_name": "Electrical Parts", "image_path": "/images/auto/fuses.jpg", "category_name": "Automotriz"},
    
    # Mascotas
    {"name": "Alimento para Perro Adulto 15kg", "short_description": "Alimento premium", "sku": "PET-001", "cost": 25.00, "sale_price": 49.99, "stock": 50, "unit": "1", "unit_of_measurement": "bolsa", "provider_id": "PROV-073", "provider_name": "Pet Food Co", "image_path": "/images/pets/dog-food.jpg", "category_name": "Mascotas"},
    {"name": "Alimento para Gato 10kg", "short_description": "Alimento seco premium", "sku": "PET-002", "cost": 20.00, "sale_price": 39.99, "stock": 45, "unit": "1", "unit_of_measurement": "bolsa", "provider_id": "PROV-073", "provider_name": "Pet Food Co", "image_path": "/images/pets/cat-food.jpg", "category_name": "Mascotas"},
    {"name": "Arena para Gato 20L", "short_description": "Arena aglomerante", "sku": "PET-003", "cost": 8.00, "sale_price": 15.99, "stock": 60, "unit": "1", "unit_of_measurement": "bolsa", "provider_id": "PROV-074", "provider_name": "Cat Litter Plus", "image_path": "/images/pets/cat-litter.jpg", "category_name": "Mascotas"},
    {"name": "Juguete para Perro", "short_description": "Pelota de tenis", "sku": "PET-004", "cost": 3.00, "sale_price": 5.99, "stock": 100, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-075", "provider_name": "Pet Toys", "image_path": "/images/pets/dog-toy.jpg", "category_name": "Mascotas"},
    {"name": "Correa para Perro", "short_description": "Correa retráctil 5m", "sku": "PET-005", "cost": 8.00, "sale_price": 15.99, "stock": 55, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-076", "provider_name": "Pet Accessories", "image_path": "/images/pets/dog-leash.jpg", "category_name": "Mascotas"},
    {"name": "Collar para Perro", "short_description": "Collar ajustable", "sku": "PET-006", "cost": 5.00, "sale_price": 9.99, "stock": 70, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-076", "provider_name": "Pet Accessories", "image_path": "/images/pets/dog-collar.jpg", "category_name": "Mascotas"},
    {"name": "Comedero para Mascota", "short_description": "Comedero de acero inoxidable", "sku": "PET-007", "cost": 6.00, "sale_price": 11.99, "stock": 65, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-077", "provider_name": "Pet Supplies", "image_path": "/images/pets/pet-bowl.jpg", "category_name": "Mascotas"},
    {"name": "Cama para Perro", "short_description": "Cama ortopédica tamaño mediano", "sku": "PET-008", "cost": 25.00, "sale_price": 49.99, "stock": 20, "unit": "1", "unit_of_measurement": "unidad", "provider_id": "PROV-078", "provider_name": "Pet Beds", "image_path": "/images/pets/dog-bed.jpg", "category_name": "Mascotas"},
    {"name": "Shampoo para Perro 500ml", "short_description": "Shampoo hipoalergénico", "sku": "PET-009", "cost": 7.00, "sale_price": 13.99, "stock": 40, "unit": "1", "unit_of_measurement": "botella", "provider_id": "PROV-079", "provider_name": "Pet Grooming", "image_path": "/images/pets/dog-shampoo.jpg", "category_name": "Mascotas"},
    {"name": "Snacks para Perro 500g", "short_description": "Snacks dentales", "sku": "PET-010", "cost": 4.00, "sale_price": 7.99, "stock": 80, "unit": "1", "unit_of_measurement": "bolsa", "provider_id": "PROV-073", "provider_name": "Pet Food Co", "image_path": "/images/pets/dog-treats.jpg", "category_name": "Mascotas"},
]

def seed_database():
    """Función principal para poblar la base de datos"""
    db: Session = SessionLocal()
    
    try:
        # Crear categorías
        print("Creando categorías...")
        category_map = {}
        for cat_data in CATEGORIES_DATA:
            existing = db.query(Category).filter(Category.name == cat_data["name"]).first()
            if not existing:
                category = Category(**cat_data)
                db.add(category)
                db.commit()
                db.refresh(category)
                category_map[cat_data["name"]] = category.id
                print(f"  ✓ Categoría creada: {cat_data['name']}")
            else:
                category_map[cat_data["name"]] = existing.id
                print(f"  - Categoría ya existe: {cat_data['name']}")
        
        # Crear productos
        print("\nCreando productos...")
        created_count = 0
        for prod_data in PRODUCTS_DATA:
            # Verificar si el producto ya existe por SKU
            existing = db.query(Product).filter(Product.sku == prod_data["sku"]).first()
            if existing:
                print(f"  - Producto ya existe: {prod_data['sku']}")
                continue
            
            # Obtener category_id
            category_name = prod_data.pop("category_name")
            category_id = category_map.get(category_name)
            
            if not category_id:
                print(f"  ✗ Error: Categoría '{category_name}' no encontrada para producto {prod_data['sku']}")
                continue
            
            prod_data["category_id"] = category_id
            product = Product(**prod_data)
            db.add(product)
            created_count += 1
            
            if created_count % 50 == 0:
                db.commit()
                print(f"  ✓ {created_count} productos creados...")
        
        db.commit()
        print(f"\n✓ Proceso completado. Total de productos creados: {created_count}")
        
        # Generar productos adicionales para llegar a 250+
        print("\nGenerando productos adicionales...")
        additional_products = []
        category_ids = list(category_map.values())
        
        # Generar productos variados para cada categoría
        for i in range(250 - created_count):
            category_id = random.choice(category_ids)
            category_name = [k for k, v in category_map.items() if v == category_id][0]
            
            # Generar SKU único
            sku = f"{category_name[:4].upper()}-{str(1000 + i).zfill(3)}"
            
            # Generar datos aleatorios
            cost = round(random.uniform(5, 100), 2)
            sale_price = round(cost * random.uniform(1.5, 2.5), 2)
            stock = random.randint(10, 200)
            
            product_data = {
                "name": f"Producto {category_name} {i+1}",
                "short_description": f"Descripción del producto {i+1}",
                "sku": sku,
                "cost": cost,
                "sale_price": sale_price,
                "stock": stock,
                "unit": "1",
                "unit_of_measurement": "unidad",
                "provider_id": f"PROV-{str(random.randint(1, 100)).zfill(3)}",
                "provider_name": f"Proveedor {random.randint(1, 50)}",
                "image_path": f"/images/{category_name.lower().replace(' ', '-')}/product-{i+1}.jpg",
                "category_id": category_id
            }
            
            product = Product(**product_data)
            db.add(product)
            additional_products.append(product)
            
            if len(additional_products) % 50 == 0:
                db.commit()
                print(f"  ✓ {len(additional_products)} productos adicionales creados...")
        
        db.commit()
        total_products = created_count + len(additional_products)
        print(f"\n✓ Total de productos en la base de datos: {total_products}")
        
    except Exception as e:
        db.rollback()
        print(f"\n✗ Error al poblar la base de datos: {str(e)}")
        raise
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()

