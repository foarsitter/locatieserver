from typing import Any

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
        headers = {"content-type": "application/json"}  # noqa: RUF012

        def json(self) -> dict[str, Any]:
            return {"code": 400, "metadata": [], "msg": "Missing required parameter: q"}

    monkeypatch.setattr(httpx, "get", lambda *_, **__: ErrorResponse())

    with pytest.raises(LocatieserverResponseError):
        free("123456789")
