# Microservicio: Products

## Descripción

Este microservicio se encarga de la gestión de productos: creación, consulta, actualización y eliminación (CRUD). Forma parte de un sistema desacoplado que incluye también el microservicio `inventory`, con el que se comunica mediante HTTP.

---

## Instalación

1. Clona el repositorio:
   ```bash
   git clone 
   cd products
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
   poetry run uvicorn app.main:app --reload --port 8001
   ```

5. Accede a la documentación interactiva:
   - http://localhost:8001/docs

---

## ⚙️ Arquitectura y tecnologías

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

---

## Seguridad

Este microservicio puede validar solicitudes externas mediante un header `X-API-KEY`, si se implementa junto con sistemas externos como `inventory`.

---

## Endpoints principales

- `GET /products/` → listar productos
- `GET /products/{id}` → obtener un producto por ID
- `POST /products/` → crear producto
- `PUT /products/{id}` → actualizar producto
- `DELETE /products/{id}` → eliminar producto

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

Este microservicio puede responder a solicitudes HTTP desde `inventory`, por ejemplo:

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
