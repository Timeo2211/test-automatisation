import os
import sys

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

RACINE_PROJET = os.path.dirname(os.path.abspath(__file__))
RACINE_PROJET = os.path.dirname(RACINE_PROJET)
if RACINE_PROJET not in sys.path:
    sys.path.insert(0, RACINE_PROJET)


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
    navigateur.implicitly_wait(5)
    try:
        yield navigateur
    finally:
        navigateur.quit()
