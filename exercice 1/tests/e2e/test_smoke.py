import pytest


@pytest.mark.e2e
def test_le_driver_ouvre_la_plateforme(driver, base_url):
    driver.get(f"{base_url}/login")
    assert "Code un max" in driver.title
