import pytest

from app.validation import email_valide


@pytest.mark.unit
@pytest.mark.parametrize(
    "adresse",
    ["eleve.test@codeunmax.fr", "apprenant@codeunmax.fr", "a@b.co"],
)
def test_email_valide_accepte_les_adresses_bien_formees(adresse):
    assert email_valide(adresse) is True


@pytest.mark.unit
@pytest.mark.parametrize(
    "adresse",
    ["", "eleve.test", "@codeunmax.fr", "eleve@", "eleve@codeunmax"],
)
def test_email_valide_rejette_les_adresses_mal_formees(adresse):
    assert email_valide(adresse) is False
