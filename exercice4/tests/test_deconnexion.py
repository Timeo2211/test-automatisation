import pytest

from pages.login_page import LoginPage


@pytest.mark.e2e
def test_deconnexion_ramene_a_la_page_de_login(session_connectee):
    dashboard = session_connectee
    login = dashboard.se_deconnecter()
    assert isinstance(login, LoginPage)
    assert login.est_present(LoginPage.SUBMIT), (
        "Le formulaire de login n'est pas revenu apres la deconnexion"
    )
    assert "Connexion" in login.titre(), (
        f"Titre inattendu apres deconnexion : {login.titre()!r}"
    )
