# Microservicio Backend: Productos e Inventario

## Descripción
Este sistema está compuesto por dos microservicios independientes:

- `products`: CRUD de productos
- `inventory`: gestión de inventario y flujo de compras

Ambos se comunican vía HTTP siguiendo el estándar [JSON:API](https://jsonapi.org/).

---

## Instalación

1. Clonar el repositorio
2. Ejecutar `docker-compose up --build`
3. Acceder a la documentación interactiva:
   - Productos: http://localhost:8001/docs
   - Inventario: http://localhost:8002/docs

---

## Arquitectura y tecnologías

- Lenguaje: Python 3.11
- Framework: FastAPI
- BD: SQLite con Alembic para migraciones
- Contenedores: Docker + Docker Compose
- Comunicación: HTTP + JSON:API + API Key
- Dependencias: Poetry
- Testing: Pytest + HTTPX

Estructura hexagonal con capas:
- `domain`: modelos y esquemas
- `repository`: acceso a datos
- `services`: lógica de negocio
- `api`: rutas y controladores
- `clients`: comunicación entre servicios

---

## Seguridad y Autenticación

Cada request entre servicios incluye una API Key en el header `X-API-KEY`. Esta clave se valida antes de hacer la solicitud.

---

## Flujo de Compra

1. Cliente envía `POST /inventory/purchase` con `product_id` y `quantity`
2. Inventory consulta vía HTTP al microservicio `products`
3. Verifica existencia y stock
4. Descuenta cantidad
5. Devuelve la confirmación de compra

---

## 🧪 Pruebas

```bash
cd products
poetry run pytest

cd ../inventory
poetry run pytest
```


## Checklist de requisitos

- [x] Microservicios desacoplados
- [x] Comunicación HTTP con autenticación
- [x] Docker + Compose
- [x] Alembic + SQLite
- [x] Tests unitarios e integración
- [x] JSON:API cumplido
- [x] README y diagramas

---

## 🔄 Flujo de compra
```
POST /inventory/purchase
    ├─> GET /products/{id}    (validación existencia)
    ├─> validar stock
    └─> actualizar inventario y responder
```

