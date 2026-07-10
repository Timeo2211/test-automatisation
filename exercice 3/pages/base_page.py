from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.TIMEOUT)

    def ouvrir(self, url):
        self.driver.get(url)
        return self

    def saisir(self, locator, texte):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(texte)

    def cliquer(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def lire_texte(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def est_present(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def compter(self, locator):
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return len(self.driver.find_elements(*locator))

    def titre(self):
        return self.driver.title
