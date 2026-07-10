from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CataloguePage(BasePage):
    URL_PATH = "/catalogue"

    CARTE = (By.CLASS_NAME, "cours-card")
    TITRE = (By.CLASS_NAME, "cours-titre")

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self.base_url = base_url

    def open(self):
        self.ouvrir(self.base_url + self.URL_PATH)
        return self

    def nombre_de_cours(self):
        return self.compter(self.CARTE)

    def titres_des_cours(self):
        return [e.text for e in self.driver.find_elements(*self.TITRE)]

    def s_inscrire_au_cours(self, nom):
        from pages.inscription_page import InscriptionPage
        lien = (
            By.XPATH,
            "//div[contains(@class,'cours-card')]"
            f"[.//*[normalize-space(text())='{nom}']]//a",
        )
        self.cliquer(lien)
        return InscriptionPage(self.driver, self.base_url)
