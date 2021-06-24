import httpx

from locatieserver.client.config import BASE_URL
from locatieserver.schema import SuggestResponse

PATH = "/suggest"


FL_DEFAULT = ""

defaults = {
    "fl": "id,weergavenaam,type,score",
    "sort": "score desc, sortering asc, weergavenaam asc",
    "qf": "score desc, sortering asc, weergavenaam asc",
    "bq": "type:provincie^1.5 type:gemeente^1.5 type:woonplaats^1.5 type:weg^1.5 type:postcode^0.5 type:adres^1",
    "rows": 10,
    "start": 0,
    "wt": "json",
    "indent": True,
    "lat": None,
    "lon": None,
    "fq": "type:(gemeente OR woonplaats OR weg OR postcode OR adres)",
}


def suggest(
    q: str,
    fl: str = defaults["fl"],
    sort: str = defaults["sort"],
    qf: str = defaults["qf"],
    bq: str = defaults["bq"],
    rows: int = defaults["rows"],
    start: int = defaults["start"],
    wt: str = defaults["wt"],
    indent: bool = defaults["indent"],
    lat: float = defaults["lat"],
    lon: float = defaults["lon"],
    fq: str = defaults["fq"],
) -> SuggestResponse:

    params = filter_defaults(
        fl=fl, sort=sort, qf=qf, bq=bq, rows=rows, start=start, wt=wt, indent=indent, lat=lat, lon=lon, fq=fq
    )

    params["q"] = q

    response = httpx.get(BASE_URL + PATH, params=params)

    return SuggestResponse.parse_raw(response.content)


def filter_defaults(**kwargs):
    non_default_values = {}

    for key, value in kwargs.items():
        if value != defaults[key]:
            non_default_values[key] = value

    return non_default_values
