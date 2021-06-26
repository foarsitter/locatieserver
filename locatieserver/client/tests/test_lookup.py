from locatieserver.client import lookup


def test_lookkup():

    x = lookup("adr-bf54db721969487ed33ba84d9973c702")

    assert x.response.numFound == 1
