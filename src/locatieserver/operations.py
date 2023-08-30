from typing import Optional

from pydantic import Field


class Operation:
    """Base class for API operations."""


class Free(Operation):
    """Free API operation."""
    url = '/free'
    method = 'get'

    q: Optional[str] = Field(..., description="""Hiermee worden de zoektermen opgegeven. De Solr-syntax voor zoektermen kan hier
worden toegepast, bijv. combineren met "and", en het gebruik van dubbele quotes
voor opeenvolgende zoektermen. Zoektermen mogen incompleet zijn. Ook wordt er
gebruik gemaakt van synoniemen.

Voorbeelden:
`q=Utrecht`: geeft resultaten terug met de zoekterm Utrecht, bijv. adressen in
de stad Utrecht, woonplaatsen en gemeenten in de provincie Utrecht.

`q="De Bilt"`: geeft resultaten terug met de zoekterm De Bilt, bijv. de
woonplaats en gemeente De Bilt, of adressen in deze woonplaats. Let op
dat bij het daadwerkelijk verzenden van het request onder water de
URL-encodingregels toegepast worden, dus een spatie wordt verzonden als
een plusteken.

`q="Sint Jacob" Utre`: geeft o.a. adressen terug waarvan er delen
achtereenvolgens beginnen met "Sint" en "Jacob", of met "St"
(synoniem) en "Jacob", en waar ook een deel met "Utre" begint. Een
voorbeeld is het adres St.-Jacobsstraat 200 (officiële schrijfwijze)
in Utrecht."""
                   )
