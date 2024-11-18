from __future__ import annotations

from pydantic import Field

from locatieserver.schema.base import LocatieserverBaseModel
from locatieserver.schema.utils import Point  # noqa: TCH001


class LookupDoc(LocatieserverBaseModel):
    """Lookup service document"""

    bron: str | None
    woonplaatscode: str | None
    type: str | None
    woonplaatsnaam: str | None
    huis_nlt: str | None
    openbareruimtetype: str | None
    gemeentecode: str | None
    weergavenaam: str | None
    straatnaam_verkort: str | None
    id: str | None
    gemeentenaam: str | None
    identificatie: str | None
    openbareruimte_id: str | None
    provinciecode: str | None
    postcode: str | None
    provincienaam: str | None
    centroide_ll: Point | None
    nummeraanduiding_id: str | None
    adresseerbaarobject_id: str | None
    huisnummer: int | None
    huisnummertoevoeging: str | None = ""
    huisletter: str | None = ""
    provincieafkorting: str | None
    centroide_rd: Point | None
    straatnaam: str | None
    gekoppeld_perceel: list[str] | None


class LookupInlineResponse(LocatieserverBaseModel):
    num_found: int = Field(..., alias="numFound")
    start: int
    docs: list[LookupDoc]


class LookupResponse(LocatieserverBaseModel):
    """Response for the lookup service"""

    response: LookupInlineResponse
