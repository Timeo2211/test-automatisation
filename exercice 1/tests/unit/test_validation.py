"""TEST-1 : premier test unitaire sur la logique metier.

On teste la fonction pure `email_valide` (aucun reseau, aucun navigateur),
avec au moins un cas valide et un cas invalide.
"""

import pytest

from app.validation import email_valide


@pytest.mark.unit
@pytest.mark.parametrize(
    "adresse",
    [
        "eleve.test@codeunmax.fr",
        "apprenant@codeunmax.fr",
        "a@b.co",
    ],
)
def test_email_valide_accepte_les_adresses_bien_formees(adresse):
    assert email_valide(adresse) is True


@pytest.mark.unit
@pytest.mark.parametrize(
    "adresse",
    [
        "",                      # vide
        "eleve.test",            # pas de @
        "@codeunmax.fr",         # partie locale vide
        "eleve@",                # domaine vide
        "eleve@codeunmax",       # domaine sans point
    ],
)
def test_email_valide_rejette_les_adresses_mal_formees(adresse):
    assert email_valide(adresse) is False
