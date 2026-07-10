import pytest

from pages.login_page import LoginPage

COMPTE_VALIDE = ("eleve.test@codeunmax.fr", "Test1234!")


@pytest.mark.e2e
def test_login_valide_mene_au_tableau_de_bord(driver, base_url):
    login = LoginPage(driver, base_url).open()
    dashboard = login.login(*COMPTE_VALIDE)
    assert dashboard.est_affiche(), "Le tableau de bord ne s'affiche pas apres un login valide"
    assert "Tableau de bord" in dashboard.titre(), (
        f"Titre inattendu apres login : {dashboard.titre()!r}"
    )


@pytest.mark.e2e
@pytest.mark.parametrize(
    "email, mot_de_passe, message_attendu",
    [
        ("eleve.test@codeunmax.fr", "mauvais-mdp", "incorrect"),
        ("inconnu@codeunmax.fr", "Test1234!", "incorrect"),
        ("", "Test1234!", "remplis"),
        ("eleve.test@codeunmax.fr", "", "remplis"),
    ],
)
def test_login_refuse_affiche_un_message(driver, base_url, email, mot_de_passe, message_attendu):
    login = LoginPage(driver, base_url).open()
    login.remplir_et_soumettre(email, mot_de_passe)
    message = login.message_erreur()
    assert message_attendu in message.lower(), (
        f"Message d'erreur inattendu pour ({email!r}, {mot_de_passe!r}) : {message!r}"
    )
