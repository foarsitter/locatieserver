from pydantic import Field

from locatieserver.schema.base import LocatieserverBaseModel


class SuggestDoc(LocatieserverBaseModel):
    type: str
    weergavenaam: str
    id: str
    score: float


class SuggestInlineResponse(LocatieserverBaseModel):
    num_found: int = Field(..., alias="numFound")
    start: int
    max_score: float = Field(..., alias="maxScore")
    docs: list[SuggestDoc]


class Suggest(LocatieserverBaseModel):
    suggest: list[str]


class Suggestion(LocatieserverBaseModel):
    num_found: int = Field(..., alias="numFound")
    start_offset: int = Field(..., alias="startOffset")
    end_offset: int = Field(..., alias="endOffset")
    suggestion: list[str]


class Collation(LocatieserverBaseModel):
    collation_query: str = Field(..., alias="collationQuery")
    hits: int
    misspellings_and_corrections: list[str] = Field(
        ...,
        alias="misspellingsAndCorrections",
    )


class Spellcheck(LocatieserverBaseModel):
    suggestions: list[Suggestion]
    collations: list[Collation]


class SuggestResponse(LocatieserverBaseModel):
    """Response for the suggest service"""

    response: SuggestInlineResponse
    highlighting: dict[str, Suggest]
    spellcheck: Spellcheck
