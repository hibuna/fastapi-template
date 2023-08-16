from typing import get_args as typing_get_args, NoReturn

from fastapi import HTTPException

from project.entities import Base
from project.api.endpoints.config import EndpointConfig
from project.api.models.base import OutputModel
from project.api.models.errors import HTTPError


def format_error_responses(errors: list[type[HTTPError]]) -> dict[int, dict[str, HTTPError]]:
    """Format a list of {HTTP code : ErrorModel} pairs into a dict."""
    return {error._code.default: {"model": error} for error in errors}  # type: ignore


def raise_(error: HTTPError) -> NoReturn:
    details = error.as_dict()
    details.update(vars(error))  # overwrite class defaults with instance values
    raise HTTPException(status_code=error._code, detail=details)


def respond_model(
    model: type(OutputModel), entity: Base, config: EndpointConfig = EndpointConfig()
) -> OutputModel:
    data = vars(entity)

    if config.map_uuid_to_id:
        data["id"] = data["uuid"]

    model = model.model_validate(data)
    return model


def respond_models(
    model: type(list[type(OutputModel)]),
    entities: list[Base],
    config: EndpointConfig = EndpointConfig(),
) -> list[OutputModel]:
    model = typing_get_args(model)[0]
    return [respond_model(model, entity, config) for entity in entities]
