from typing import TypeAlias, Union, TypeVar

from pydantic import BaseModel

from project.api.models.base import OutputModel


serializable_type: TypeAlias = Union[
    str, int, float, list, tuple, bool, dict, None, BaseModel
]

output_model_type: TypeAlias = TypeVar("output_model_type", bound=OutputModel)
