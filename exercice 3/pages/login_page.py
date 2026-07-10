from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage


class LoginPage(BasePage):
    URL_PATH = "/login"

    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "submit")
    ERREUR = (By.CSS_SELECTOR, ".alert-error")

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self.base_url = base_url

    def open(self):
        self.ouvrir(self.base_url + self.URL_PATH)
        return self

    def remplir_et_soumettre(self, email, mot_de_passe):
        self.saisir(self.EMAIL, email)
        self.saisir(self.PASSWORD, mot_de_passe)
        self.cliquer(self.SUBMIT)

    def login(self, email, mot_de_passe):
        self.remplir_et_soumettre(email, mot_de_passe)
        return DashboardPage(self.driver, self.base_url)

    def message_erreur(self):
        return self.lire_texte(self.ERREUR)
