# Scalable FastAPI Template (REST)

## Use case

This template is intended to be used as a starting point for a new project that uses FastAPI and 
has a database. It is designed to be scalable and easy to use. The current implementation makes use 
of SQLAlchemy, but it can be easily replaced with any other ORM.

## Requirements

- Python 3.11
- pipenv


## Features

- Standalone FastAPI app
- Dynamic endpoints based on Pydantic (v2) models
- Automatic field validation
- Scalable project structure
- Sample endpoints to get started
- Customizable HTTP errors
- Generated API documentation


## Setup

1. Clone this repo
2. Install pipenv with `pip install pipenv`
3. Run `pipenv install` to install dependencies
4. Run `uvicorn main:app --reload` to start the app for development


## How to use

To start development you can use the sample endpoints in `project/api/endpoints/user.py` as a starting
point. Some basic RESTful endpoints are defined here.

This repo revolves around `Endpoint` classes. These classes are defined in `project/api/endpoints/base.py`.
They are used to define endpoints for entities. The `Endpoint` class takes an `InputModel` and an `OutputModel`

### Endpoints for the user entity

To add an endpoint for the user entity, copy a similar endpoint and define the in- and output as needed. 
Models inherit from Pydantic `BaseModel`; this adds automatic field validation. 
To tweak or turn off validation, you can modify the `InputModel` and `OutputModel` base classes.
To tweak endpoint behaviour, change or subclass `EndpointConfig` and pass them to the `Endpoint` classes as you see fit.

### Endpoints for new entities

To add endpoints for new entities, you can simply follow the same pattern as used for the user entity. 
This means copying all `project/api/*/user.py` files and refactoring the copies to fit the new entity.


## API Documentation

Run the app and go to http://localhost:8000/docs.


## Documentation

Documentation on FastAPI can be found [here](https://fastapi.tiangolo.com/).\
Documentation on Pydantic can be found [here](https://docs.pydantic.dev/dev-v2/).