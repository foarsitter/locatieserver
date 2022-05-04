from locatieserver.client import free
from locatieserver.client.utils import safe_result


@safe_result
def test_free():

    result = free("Bolstraat and Utrecht and type:adres")

    assert result.response.num_found == 165

    return result
