from pydantic import BaseModel
from pydantic import ConfigDict


class LocatieserverBaseModel(BaseModel):
    """
    BaseModel replacement for sharing the configuration across the different schemas.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)
