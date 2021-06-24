import httpx

from locatieserver.client.config import BASE_URL
from locatieserver.schema import SuggestResponse

PATH = "/suggest"


def suggest(q: str) -> SuggestResponse:
    """/lookup/v3/suggest."""
    response = httpx.get(BASE_URL + PATH, params=dict(q=q))

    return SuggestResponse.parse_raw(response.content)
