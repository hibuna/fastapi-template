from typing import Annotated

from pydantic import Field, UUID4, EmailStr

from project.api.models.base import OutputModel


class UserModel(OutputModel):
    uuid: UUID4 = Field(alias="id")
    email: Annotated[EmailStr, str]
    name_first: str
    name_last: str
    name_middle: str | None
