FROM python:3.13

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-root

COPY . .

# crear carpeta si se usa subdirectorio
RUN mkdir -p /app

RUN chmod +x entrypoint.sh

EXPOSE 8002

CMD ["sh", "./entrypoint.sh"]
