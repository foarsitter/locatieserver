from __future__ import annotations

from locatieserver.client.utils import filter_defaults
from locatieserver.client.utils import http_get
from locatieserver.schema.suggest import SuggestResponse


PATH = "suggest"


def suggest(  # noqa: PLR0913
    q: str | None = "*:*",
    fl: str | None = "id,weergavenaam,type,score",
    sort: str | None = "score desc, sortering asc, weergavenaam asc",
    qf: str | None = "score desc, sortering asc, weergavenaam asc",
    bq: str
    | None = "type:provincie^1.5 type:gemeente^1.5 type:woonplaats^1.5 type:weg^1.5 type:postcode^0.5 type:adres^1",  # noqa: E501
    rows: int | None = 10,
    start: int | None = 0,
    wt: str | None = "json",
    indent: bool | None = True,  # noqa: FBT002
    lat: float | None = None,
    lon: float | None = None,
    fq: str | None = "type:(gemeente OR woonplaats OR weg OR postcode OR adres)",
) -> SuggestResponse:
    """Suggest service.

    For detailed description: https://github.com/PDOK/locatieserver/wiki/API-Locatieserver#3suggest-service

    :param q: Hiermee worden de zoektermen opgegeven. De Solr-syntax voor zoektermen kan hier worden toegepast,
        bijv. combineren met `and`, en het gebruik van dubbele quotes voor opeenvolgende zoektermen.
        Zoektermen mogen incompleet zijn. Ook wordt er gebruik gemaakt van synoniemen.
    :param fl: Hiermee worden de velden opgegeven die teruggegeven dienen te worden.
    :param sort: Hiermee kan worden opgegeven hoe de sortering plaatsvindt.
        De defaultwaarde is `score desc, sortering asc, weergavenaam asc`.
        Door voor deze string `typesortering asc` toe te voegen, kan de oude sortering worden gebruikt.
    :type sort: str
    :param qf: Met behulp van deze parameter kan aan bepaalde *velden* een extra boost worden meegegeven.
        Hiermee kan de scoreberekening worden aangepast.
        De defaultwaarde is exacte_match^1 suggest^0.5 huisnummer^0.5 huisletter^0.5 huisnummertoevoeging^0.5.
        Om alleen van het suggest-veld gebruik te maken, kan qf=suggest worden meegegeven.
    :param bq: Met behulp van deze parameter kan aan bepaalde veldwaarden een extra boost worden meegegeven.
        Ook hiermee kan de scoreberekening worden aangepast. Dit gebeurt alleen o.b.v. de inhoud van het veld `type`.
        De overige typen (nog niet aanwezig) hebben geen boost.
        Voor elke boost query moet een aparte bq=<boost> worden gebruikt.
        Bijvoorbeeld `bq=type:gemeente^1.5&bq=type:woonplaats^1.5`.
    :param rows: Hiermee wordt opgegeven wat het maximale aantal rijen (ofwel resultaten)
        is dat teruggegeven moet worden op deze bevraging.
    :param start: Hiermee wordt opgegeven wat de index is van het eerste resultaat dat teruggegeven wordt.
        Dit is zero-based. In combinatie met de rows-parameter kunnen deze services gepagineerd worden bevraagd.
    :param wt: Hiermee wordt opgegeven wat het outputformaat is van de bevraging.
    :param indent: Hiermee kan worden opgegeven of de teruggegeven JSON ingesprongen (geïndenteerd) moet worden.
    :param lat: Werkt alleen in combinatie met `lon`.
        Hiermee kan een coördinaat (in lat/lon, ofwel WGS84) worden opgegeven.
        Met behulp van deze parameters worden de gevonden zoekresultaten gesorteerd op afstand van het meegegeven punt.
        Wanneer de locatie van de gebruiker bekend is, kan op deze manier effectiever worden gezocht.
        Het meegeven van een coördinaat is met name nuttig voor de suggest- en vrije geocoder-services.
        Hier worden meestal meerdere resultaten teruggegeven.
        Als decimaal scheidingsteken moet een punt worden opgegeven i.p.v. een komma.
    :param lon: Werkt alleen in combinatie met `lat`.
        Hiermee kan een coördinaat (in lat/lon, ofwel WGS84) worden opgegeven.
        Met behulp van deze parameters worden de gevonden zoekresultaten gesorteerd op afstand van het meegegeven punt.
        Wanneer de locatie van de gebruiker bekend is, kan op deze manier effectiever worden gezocht.
        Het meegeven van een coördinaat is met name nuttig voor de suggest- en vrije geocoder-services.
        Hier worden meestal meerdere resultaten teruggegeven.
        Als decimaal scheidingsteken moet een punt worden opgegeven i.p.v. een komma.
    :param fq: Hiermee kan een filter query worden opgegeven, bijv. `fq=bron:BAG`.
        Met `fq=*` kan de default filter query worden opgeheven.
    :return: SuggestResponse schema
    :rtype: SuggestResponse
    """  # noqa: E501
    params = filter_defaults(
        suggest,
        q=q,
        fl=fl,
        sort=sort,
        qf=qf,
        bq=bq,
        rows=rows,
        start=start,
        wt=wt,
        indent=indent,
        lat=lat,
        lon=lon,
        fq=fq,
    )

    response = http_get(PATH, params=params)

    return SuggestResponse.parse_raw(response.content)
