from typing import Optional, Any

from pydantic import BaseModel, ConfigDict

from project.api.types_ import serializable_type


class HTTPError(BaseModel):
    model_config = ConfigDict(extra="ignore")

    # internal attributes so pydantic ignores them
    _code: int = None
    _message: str = None

    @classmethod
    def as_dict(cls) -> dict[str, Any]:
        """Return the class defaults as a dictionary."""
        dict_ = {
            key: cls.model_json_schema()["properties"][key]["default"]
            for key in cls.model_json_schema()["properties"].keys()
        }
        return dict_


class NotFound(HTTPError):
    _code: int = 404
    _message: str = "Not Found"

    resource_cls: str = None
    resource_id: str = None

    # used for attribute typehints during instantiation
    def __init__(self, resource_cls: str, resource_id: str):
        super().__init__()
        self.resource_cls = resource_cls
        self.resource_id = resource_id


class UnprocessableContent(HTTPError):
    _code: int = 422
    _message: str = "Unprocessable Content"

    resource_cls: str = None
    field: str = None
    value: str = None

    resource_id: Optional[str] = None
    message: Optional[str] = None

    # used for attribute typehints during instantiation
    def __init__(
        self,
        resource_cls: str,
        field: str,
        value: serializable_type,
        resource_id: Optional[str] = None,
        message: Optional[str] = None,
    ):
        super().__init__()
        self.resource_cls = resource_cls
        self.resource_id = resource_id
        self.field = field
        self.value = value
        self.message = message


class InternalServerError(HTTPError):
    _code: int = 500
    _message: str = "Internal Server Error"
