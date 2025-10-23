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

docker-compose -f docker-compose-prod.yml pull
docker-compose -f docker-compose-prod.yml up -d

# copy
scp -i ~/amazon/my-ec2-key.pem docker-compose-prod.yml ec2-user@54.221.190.240:/home/ec2-user/projects/blog-api

# install docker-compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose


# remove all of containers, images
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -a -q)

docker-compose -f docker-compose-prod.yml down
docker-compose -f docker-compose-prod.yml down -v

docker exec api_id alembic upgrade head
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
