# generated by datamodel-codegen:
#   timestamp: 2021-06-26T19:10:08+00:00
from __future__ import annotations

from pydantic import Field

from locatieserver.schema.base import LocatieserverBaseModel


class ErrorResponse(LocatieserverBaseModel):
    metadata: list[str] = Field(default_factory=list)
    msg: str
    code: int
