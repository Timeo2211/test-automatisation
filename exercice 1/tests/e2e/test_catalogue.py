import pytest
from selenium.webdriver.common.by import By


@pytest.mark.e2e
def test_le_catalogue_affiche_au_moins_un_cours(driver, base_url):
    driver.get(f"{base_url}/catalogue")
    cartes = driver.find_elements(By.CLASS_NAME, "cours-card")
    assert len(cartes) >= 1
    titres = driver.find_elements(By.CLASS_NAME, "cours-titre")
    assert len(titres) >= 1
    assert titres[0].text.strip() != ""
