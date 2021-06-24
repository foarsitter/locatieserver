from __future__ import annotations

from typing import Dict, List, Union

from pydantic import BaseModel, Field


class Doc(BaseModel):
    type: str
    weergavenaam: str
    id: str
    score: float


class Response(BaseModel):
    num_found: int = Field(..., alias="numFound")
    start: int
    max_score: float = Field(..., alias="maxScore")
    docs: List[Doc]


class Suggest(BaseModel):
    suggest: List[str]


class Suggestion(BaseModel):
    num_found: int = Field(..., alias="numFound")
    start_offset: int = Field(..., alias="startOffset")
    end_offset: int = Field(..., alias="endOffset")
    suggestion: List[str]


class Collation(BaseModel):
    collation_query: str = Field(..., alias="collationQuery")
    hits: int
    misspellings_and_corrections: List[str] = Field(..., alias="misspellingsAndCorrections")


class Spellcheck(BaseModel):
    suggestions: List[Union[str, Suggestion]]
    collations: List[Union[str, Collation]]


class SuggestResponse(BaseModel):
    response: Response
    highlighting: Dict[str, Suggest]
    spellcheck: Spellcheck
