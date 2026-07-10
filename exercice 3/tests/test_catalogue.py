import pytest

from pages.catalogue_page import CataloguePage


@pytest.mark.e2e
@pytest.mark.parametrize("cours_attendu", ["Python avance", "Selenium pour les nuls"])
def test_le_catalogue_affiche_le_cours_attendu(driver, base_url, cours_attendu):
    catalogue = CataloguePage(driver, base_url).open()
    titres = catalogue.titres_des_cours()
    assert catalogue.nombre_de_cours() >= 1, "Le catalogue ne contient aucun cours"
    assert cours_attendu in titres, (
        f"Cours {cours_attendu!r} absent du catalogue. Trouves : {titres}"
    )
