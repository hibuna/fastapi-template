from pydantic import BaseModel, ConfigDict


class InputModel(BaseModel):
    """
    Base class for all input models.

    To finetune the configuration for input models, you can subclass this class and override the
    `model_config` attribute.

    Attributes
    ----------
    model_config : ConfigDict
        The configuration for this model.

        Documentation:
        https://pydantic-docs.helpmanual.io/usage/model_config/
    """
    model_config = ConfigDict()


class OutputModel(BaseModel):
    """
    Base class for all output models.

    To finetune the configuration for output models, you can subclass this class and override the
    `model_config` attribute.

    Attributes
    ----------
    model_config : ConfigDict
        The configuration for this model.

        Passing `extra="ignore"` prevents raising an error on extra fields when casting the Base
        entity to the output model. This allows not exposing the password field for example.

        Documentation:
        https://pydantic-docs.helpmanual.io/usage/model_config/
    """
    model_config = ConfigDict(extra="ignore")
