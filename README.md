# ZipAirlines

A basic application that implements a rest framework API that allows for calculation of airplane consumption and capacity

# About

## Requirements

### System requirements

- psycopg2 system requirements
- python 3.10


## Development

### Local environment

Setting up postgres for local development

```shell
docker run -e POSTGRES_PASSWORD=mypassword -e POSTGRES_USER=myuser \
  -v "$(pwd)/.postgres":/var/lib/postgresql/data -p 5433:5432 --name zipairpostgres -d postgres
```

After that to deploy an app on a local environment:

```shell
poetry install
cd zip_airlines && python3 manage.py runserver
```

### Running tests

```shell
cd zip_airlines
pytest tests -vvv
```




