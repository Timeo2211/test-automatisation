import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage

COMPTE_VALIDE = {
    "email": "eleve.test@codeunmax.fr",
    "mot_de_passe": "Test1234!",
}


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "http://localhost:8000")


@pytest.fixture
def driver():
    options = Options()
    if os.getenv("HEADLESS", "1") != "0":
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,900")

    navigateur = webdriver.Chrome(options=options)
    yield navigateur
    navigateur.quit()


@pytest.fixture
def session_connectee(driver, base_url):
    dashboard = LoginPage(driver, base_url).open().login(
        COMPTE_VALIDE["email"], COMPTE_VALIDE["mot_de_passe"]
    )
    assert dashboard.est_affiche(), "Le login de la fixture a echoue"
    return dashboard
