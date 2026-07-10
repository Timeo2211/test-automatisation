import pytest

from pages.catalogue_page import CataloguePage


@pytest.mark.e2e
def test_inscription_a_un_cours_affiche_la_confirmation(driver, base_url):
    catalogue = CataloguePage(driver, base_url).open()
    inscription = catalogue.s_inscrire_au_cours("Python avance")
    inscription.s_inscrire(nom="Ada Lovelace", motivation="Je veux progresser en Python.")
    message = inscription.message_confirmation()
    assert "confirmee" in message.lower(), (
        f"Message de confirmation inattendu : {message!r}"
    )
