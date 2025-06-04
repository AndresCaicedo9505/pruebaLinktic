# Microservicio: Inventoy

## Descripción


Este microservicio forma parte del sistema de gestión y se encarga de manejar las operaciones relacionadas con el inventario de productos. Permite registrar, consultar y actualizar las cantidades disponibles en stock, además de validar y procesar compras. Forma parte de un sistema desacoplado que incluye también el microservicio `products`, con el que se comunica mediante HTTP.

---

## Instalación

1. Clona el repositorio:
   ```bash
   git clone 
   cd inventory
   ```

2. Instala las dependencias:
   ```bash
   poetry install
   ```

3. Ejecuta las migraciones:
   ```bash
   alembic upgrade head
   ```

4. Levanta el servidor:
   ```bash
   poetry run uvicorn app.main:app --reload --port 8002
   ```

5. Accede a la documentación interactiva:
   - http://localhost:8002/docs

---

## Arquitectura y tecnologías

- **Lenguaje**: Python 3.11
- **Framework**: FastAPI
- **ORM**: SQLAlchemy
- **Migraciones**: Alembic
- **Gestión de dependencias**: Poetry
- **Base de datos**: SQLite
- **Testing**: Pytest + HTTPX
- **Validaciones y configuración**: Pydantic + pydantic-settings

Estructura basada en capas:

- `app/models`: definición de modelos SQLAlchemy
- `app/schemas`: Pydantic schemas para entrada/salida
- `app/api`: rutas y controladores
- `app/services`: lógica de negocio
- `app/core`: configuración y base de datos
- `app/clients`: comunicación https con otros microservicios

---

## Seguridad

Este microservicio puede validar solicitudes externas mediante un header `X-API-KEY`, si se implementa junto con sistemas externos como `products`.

---

## Endpoints principales

- `GET /inventory/{product_id}` → Trae el producto registrado en inventario y su cantidad
- `PUT /inventory/{product_id}` → Actualiza la cantidad de un producto por ID
- `POST /inventory/purchase` → Realiza compra de los productos

---

## Pruebas

1. Ejecuta pruebas unitarias:

```bash
poetry run pytest
```

2. Con cobertura de código:

```bash
poetry run pytest --cov=app --cov-report=term-missing
```

---

## Comunicación con otros microservicios

Este microservicio puede enviar solicitudes HTTP a `products`, por ejemplo:

```
GET /products/{product_id}
```

Usado para validar existencia y datos del producto antes de registrar una compra.

---

## Configuración con `.env`

Este proyecto puede usar variables de entorno definidas en un archivo `.env`:

```
DATABASE_URL=sqlite:///./products.db
API_KEY=supersecret
```

---

## Checklist

- [x] CRUD de productos funcional
- [x] Base de datos SQLite
- [x] Alembic configurado
- [x] Tests con cobertura
- [x] API Key opcional
- [x] Integración lista con `inventory`
- [x] Documentación Swagger (OpenAPI)
- [x] Poetry como gestor de entorno
