from random import randint
from typing import NoReturn
from uuid import uuid4

from pydantic import UUID4

from project.entities import User
from project.api.endpoints.base import Endpoint
from project.api.endpoints.config import EndpointConfig
from project.api.enums import HTTPMethod
from project.api.models.errors import (
    InternalServerError,
    UnprocessableContent,
    NotFound,
)
from project.api.models.input.user import CreateUserInput, UpdateUserInput
from project.api.models.output.user import UserModel
from project.api.responses import respond_model, raise_, respond_models
from project.api.types_ import output_model_type


class CreateUser(Endpoint):
    url = "/user"
    method = HTTPMethod.POST
    input_model = CreateUserInput
    response_model = UserModel
    error_models = [InternalServerError, UnprocessableContent]
    config = EndpointConfig()

    def execute(self, input_: CreateUserInput) -> output_model_type:
        # MOCKED LOGIC - REPLACE WITH YOUR OWN
        entity = User(
            id=randint(1, 999_999), uuid=str(uuid4()), **input_.model_dump()
        )
        return respond_model(model=self.response_model, entity=entity)
        # END MOCKED LOGIC


class GetUser(Endpoint):
    url = "/user/{user_id}"
    method = HTTPMethod.GET
    input_model = None  # GET doesn't have request body
    response_model = UserModel
    error_models = [NotFound, InternalServerError]
    config = EndpointConfig()

    def execute(self, user_id: UUID4) -> NoReturn:  # type: ignore
        # MOCKED LOGIC - REPLACE WITH YOUR OWN
        error = NotFound(resource_cls="User", resource_id=str(user_id))
        raise_(error)
        # END MOCKED LOGIC


class ListUser(Endpoint):
    url = "/user"
    method = HTTPMethod.GET
    input_model = None  # GET doesn't have request body
    response_model = list[UserModel]
    error_models = [InternalServerError]
    config = EndpointConfig()

    def execute(self) -> list[output_model_type]:
        # MOCKED LOGIC - REPLACE WITH YOUR OWN
        first_names = ("John", "Jane", "Jack")
        last_names = ("Doe", "Smith", "Johnson")
        users = [
            User(
                id=randint(1, 999_999),
                uuid=str(uuid4()),
                name_first=first_names[i],
                name_last=last_names[i],
                name_middle=None,
                email=f"{first_names[i]}.{last_names[i]}@example.com",
                password="some_hashed_password",
            )
            for i in range(3)
        ]
        return respond_models(self.response_model, users)
        # END MOCKED LOGIC


class UpdateUser(Endpoint):
    url = "/user/{user_id}"
    method = HTTPMethod.PUT
    input_model = UpdateUserInput
    response_model = UserModel
    error_models = [NotFound, InternalServerError, UnprocessableContent]
    config = EndpointConfig()

    def execute(self, user_id: UUID4, input_: UpdateUserInput) -> output_model_type:
        # MOCKED LOGIC - REPLACE WITH YOUR OWN
        def find_user(uuid: str) -> User:
            return User(
                id=randint(1, 999_999),
                uuid=uuid,
                name_first="John",
                name_last="Doe",
                name_middle=None,
                email=f"John.Doe@example.com",
                password="some_hashed_password",
            )

        user = find_user(uuid=str(user_id))
        for k, v in input_.model_dump(exclude_unset=True).items():
            setattr(user, k, v)
        return respond_model(model=self.response_model, entity=user)
        # END MOCKED LOGIC
