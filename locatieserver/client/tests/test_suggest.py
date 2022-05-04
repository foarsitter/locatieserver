import locatieserver.client.suggest
from locatieserver.client.utils import safe_result


@safe_result
def test_suggest():

    result = locatieserver.client.suggest("Westerein")

    assert result
    assert result.response.num_found == 140

    return result
