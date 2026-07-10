from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InscriptionPage(BasePage):
    NOM = (By.ID, "nom")
    MOTIVATION = (By.ID, "motivation")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    CONFIRMATION = (By.CSS_SELECTOR, ".alert-success")

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self.base_url = base_url

    def s_inscrire(self, nom, motivation):
        self.saisir(self.NOM, nom)
        self.saisir(self.MOTIVATION, motivation)
        self.cliquer(self.SUBMIT)
        return self

    def message_confirmation(self):
        return self.lire_texte(self.CONFIRMATION)
