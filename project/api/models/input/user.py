from typing import Optional

from pydantic import EmailStr, Field, field_validator

from project.api.models.base import InputModel
from project.api.models.errors import UnprocessableContent
from project.api.responses import raise_
from project.api.validators import validate_email


class CreateUserInput(InputModel):
    email: EmailStr = Field(max_length=255)
    password: str = Field(min_length=8, max_length=255)
    name_first: str = Field(min_length=2, max_length=255)
    name_last: str = Field(min_length=2, max_length=255)

    name_middle: Optional[str] = Field(min_length=2, max_length=255, default=None)

    @field_validator("email")
    @classmethod
    def email_validator(cls, value: str):
        if validate_email(value):
            return value

        error = UnprocessableContent(
            resource_cls="User",
            field="email",
            value=value,
            message="Email is reserved.",
        )
        raise_(error)


class UpdateUserInput(InputModel):
    email: Optional[EmailStr] = Field(max_length=255, default=None)
    password: Optional[str] = Field(min_length=8, max_length=255, default=None)
    name_first: Optional[str] = Field(min_length=2, max_length=255, default=None)
    name_last: Optional[str] = Field(min_length=2, max_length=255, default=None)
    name_middle: Optional[str] = Field(min_length=2, max_length=255, default=None)

    @field_validator("email")
    @classmethod
    def email_validator(cls, value: str):
        if validate_email(value):
            return value

        error = UnprocessableContent(
            resource_cls="User",
            field="email",
            value=value,
            message="Email is reserved.",
        )
        raise_(error)
