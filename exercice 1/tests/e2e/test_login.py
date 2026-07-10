import pytest
from selenium.webdriver.common.by import By


@pytest.mark.e2e
def test_la_page_de_login_s_affiche(driver, base_url):
    driver.get(f"{base_url}/login")
    assert "Connexion" in driver.title
    assert driver.find_element(By.ID, "email").is_displayed()
    assert driver.find_element(By.ID, "password").is_displayed()
    assert driver.find_element(By.ID, "submit").is_displayed()
