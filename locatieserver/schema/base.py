from pydantic import BaseModel


class LocatieserverBaseModel(BaseModel):
    """BaseModel replacement for sharing the configuration across the different schemas."""


class SuggestResponse(LocatieserverBaseModel):
    """Response schema for suggest()."""


class LookupResponse(LocatieserverBaseModel):
    """Response schema for lookup()."""


class FreeResponse(LocatieserverBaseModel):
    """Response schema for free()."""
