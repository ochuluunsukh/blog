## Tools

```
FastApi
JWT
PostgresSQL
SQLAlchemy
Alembic
```

## RUN

```
fastapi dev app/main.py
```

## Docker

```
docker-compose down
docker-compose up -d
docker-compose -f docker-compose-dev.yml up -d

docker-compose build
docker exec -it blog-api-1 bash
```

## Test

```
# a file name matters, prefix `test_*.py`
# https://docs.pytest.org/en/stable/explanation/goodpractices.html#test-discovery
# v - verbose
# x - stop first failed test
pytest
pytest -v
pytest -s
pytest --disable-warnings
pytest --disable-warnings -v
pytest --disable-warnings -v -x
```

## Data migration

```
alembic init alembic
```
