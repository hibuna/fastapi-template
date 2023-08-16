from typing import Optional

from fastapi import FastAPI

from project.api.endpoints.base import Endpoint
from project.api.endpoints.user import CreateUser, GetUser, ListUser, UpdateUser
from project.api.enums import HTTPMethod
from project.api.responses import format_error_responses
from project.api.util import pascal_to_capital


class CustomApi(FastAPI):
    """
    API class that automatically resolves and documents endpoints from the `api.endpoints` module
    if they are listed in this class or passed during instantiation.
    """
    endpoints = [
        CreateUser(),
        GetUser(),
        ListUser(),
        UpdateUser(),
    ]

    def __init__(self, endpoints: Optional[list[Endpoint]] = None) -> None:
        super().__init__()
        for endpoint in endpoints or self.endpoints:
            method = self.http_method_map[endpoint.method]
            name = pascal_to_capital(type(endpoint).__name__)
            method(
                name=name,
                path=endpoint.url,
                response_model=endpoint.response_model,
                responses=format_error_responses(endpoint.error_models),
            )(endpoint.execute)

    @property
    def http_method_map(self):
        return {
            HTTPMethod.GET: self.get,
            HTTPMethod.POST: self.post,
            HTTPMethod.PUT: self.put,
            HTTPMethod.DELETE: self.delete,
            HTTPMethod.PATCH: self.patch,
        }
