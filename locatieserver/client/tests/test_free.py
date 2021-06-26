from locatieserver.client import free


def test_free():

    response = free("Bolstraat and Utrecht and type:adres")

    assert response.response.numFound == 165
