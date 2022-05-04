from locatieserver.client import lookup
from locatieserver.client.utils import safe_result


@safe_result
def test_lookup():

    result = lookup("adr-bf54db721969487ed33ba84d9973c702")

    assert result.response.num_found == 1

    return result
