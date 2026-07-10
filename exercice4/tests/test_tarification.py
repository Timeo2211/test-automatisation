import pytest

from app.tarification import prix_inscription


@pytest.mark.unit
@pytest.mark.parametrize(
    "nb_cours, prix_attendu",
    [
        (1, 40.0),
        (2, 80.0),
        (3, 102.0),
        (4, 136.0),
        (5, 170.0),
    ],
)
def test_prix_inscription_applique_la_remise_des_le_3e_cours(nb_cours, prix_attendu):
    assert prix_inscription(nb_cours) == prix_attendu, (
        f"{nb_cours} cours devraient couter {prix_attendu}"
    )
