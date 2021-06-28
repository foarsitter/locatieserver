from __future__ import annotations

from typing import List, Optional

from pydantic import Field

from locatieserver.schema.base import LocatieserverBaseModel


class LookupDoc(LocatieserverBaseModel):
    """Lookup service document"""

    bron: str
    woonplaatscode: str
    type: str
    woonplaatsnaam: str
    huis_nlt: str
    openbareruimtetype: str
    gemeentecode: str
    weergavenaam: str
    straatnaam_verkort: str
    id: str
    gemeentenaam: str
    identificatie: str
    openbareruimte_id: str
    provinciecode: str
    postcode: str
    provincienaam: str
    centroide_ll: str
    nummeraanduiding_id: str
    adresseerbaarobject_id: str
    huisnummer: int
    huisnummertoevoeging: Optional[str] = ""
    huisletter: Optional[str] = ""
    provincieafkorting: str
    centroide_rd: str
    straatnaam: str
    gekoppeld_perceel: List[str]


class LookupInlineResponse(LocatieserverBaseModel):
    num_found: int = Field(..., alias="numFound")
    start: int
    docs: List[LookupDoc]


class LookupResponse(LocatieserverBaseModel):
    """Response for the lookup service"""

    response: LookupInlineResponse
