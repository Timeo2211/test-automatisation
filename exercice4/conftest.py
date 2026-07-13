import os
import time
import uuid

import pytest
from dotenv import load_dotenv
from faker import Faker
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from app.inscription import supprimer_compte
from pages.login_page import LoginPage

load_dotenv(override=False)

COMPTE_VALIDE = {
    "email": os.getenv("SERVICE_EMAIL", "eleve.test@codeunmax.fr"),
    "mot_de_passe": os.getenv("SERVICE_PASSWORD", "Test1234!"),
}

FAKER_SEED = int(os.getenv("FAKER_SEED", "12345"))

NAVIGATEURS = [n.strip() for n in os.getenv("BROWSERS", "chrome,firefox").split(",") if n.strip()]
HEADLESS = os.getenv("HEADLESS", "1") != "0"


def _instancier(navigateur):
    if navigateur == "firefox":
        options = FirefoxOptions()
        if HEADLESS:
            options.add_argument("-headless")
        options.add_argument("--width=1280")
        options.add_argument("--height=900")
        return webdriver.Firefox(options=options)

    options = ChromeOptions()
    if HEADLESS:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,900")
    return webdriver.Chrome(options=options)


def _construire_driver(navigateur):
    # Selenium Manager peut etre tue par macOS (Gatekeeper) a son tout premier
    # lancement : on retente avec un court delai, le temps que l'OS valide le
    # binaire. Sans effet en CI Linux (driver preinstalle).
    derniere_erreur = None
    for _ in range(4):
        try:
            return _instancier(navigateur)
        except WebDriverException as erreur:
            derniere_erreur = erreur
            time.sleep(3)
    raise derniere_erreur


@pytest.fixture(scope="session")
def config():
    return {
        "base_url": os.getenv("BASE_URL", "http://localhost:8000"),
        "service": COMPTE_VALIDE,
    }


@pytest.fixture(scope="session")
def base_url(config):
    return config["base_url"]


@pytest.fixture(params=NAVIGATEURS)
def driver(request):
    navigateur = _construire_driver(request.param)
    yield navigateur
    navigateur.quit()


@pytest.fixture
def session_connectee(driver, base_url):
    dashboard = LoginPage(driver, base_url).open().login(
        COMPTE_VALIDE["email"], COMPTE_VALIDE["mot_de_passe"]
    )
    assert dashboard.est_affiche(), "Le login de la fixture a echoue"
    return dashboard


@pytest.fixture
def apprenant():
    faker = Faker("fr_FR")
    faker.seed_instance(FAKER_SEED)

    prenom = faker.first_name()
    nom = faker.last_name()
    unique = uuid.uuid4().hex[:8]
    donnees = {
        "nom": f"{prenom} {nom}",
        "email": f"{prenom.lower()}.{nom.lower()}.{unique}@codeunmax.fr",
        "mot_de_passe": faker.password(length=12),
    }

    yield donnees

    supprimer_compte(donnees["email"])
