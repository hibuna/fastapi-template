from typing import Union, Optional

from project.api.endpoints.config import EndpointConfig
from project.api.enums import HTTPMethod
from project.api.models.base import InputModel, OutputModel
from project.api.models.errors import HTTPError


class Endpoint:
    """
    Base class for all endpoints. Will be automatically resolved and documented if you add an
    endpoint to the `api.endpoints` module.

    Attributes
    ----------
    url : str
        The URL path to this endpoint.
    method : HTTPMethod
        The HTTP method for this endpoint.
    input_model : Optional[type[InputModel]]
        The input model for this request body. Can be `None` if you choose to omit a request body.
    response_model : Optional[Union[OutputModel, list[OutputModel]]]
        The output model for this endpoint. Can be `None` if you choose to omit a response body.
    config : EndpointConfig
        The configuration for this endpoint.
    error_models : list[type[HTTPError]]
        The list of HTTP errors that this endpoint can respond.
    """

    url: str
    method: HTTPMethod
    input_model: Optional[type[InputModel]]
    response_model: Union[OutputModel, list[OutputModel]]
    error_models: list[type[HTTPError]]
    config: EndpointConfig

    def __init__(self) -> None:
        if not hasattr(self, "config"):
            raise TypeError("Cannot instantiate abstract class Endpoint")

    def __post_init__(self) -> None:
        self.url = f"{self.config.endpoint_prefix}{self.url}"

    def execute(self, *args, **kwargs) -> OutputModel:
        """Execute on request. Override this method in your subclass."""
        raise NotImplementedError
