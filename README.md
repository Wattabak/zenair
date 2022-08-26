# Grenzeit | Borders in time

A backend of the Grenzeit project

## Requirements

### System requirements

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




