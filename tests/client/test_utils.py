from typing import Any
from typing import Dict

import httpx
import pytest
from _pytest.monkeypatch import MonkeyPatch

from locatieserver.client import free
from locatieserver.client.utils import LocatieserverResponseError
from locatieserver.client.utils import http_get


def test_http_get_400() -> None:
    with pytest.raises(LocatieserverResponseError):
        http_get("lookup", {"misssing": "123456789", "wt": "json", "q": "test"})


def test_error_response_json(monkeypatch: MonkeyPatch) -> None:
    class ErrorResponse:
        status_code = 400
        headers = {"content-type": "application/json"}

        def json(self) -> Dict[str, Any]:
            return {"code": 400, "metadata": [], "msg": "Missing required parameter: q"}

    monkeypatch.setattr(httpx, "get", lambda *args, **kwargs: ErrorResponse())

    with pytest.raises(LocatieserverResponseError):
        free("123456789", wt="json")
