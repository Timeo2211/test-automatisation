from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DashboardPage(BasePage):
    URL_PATH = "/dashboard"

    DASHBOARD = (By.ID, "dashboard")
    TITRE = (By.CSS_SELECTOR, "h1.dashboard-title")
    LIEN_CATALOGUE = (By.LINK_TEXT, "Catalogue")
    LOGOUT = (By.ID, "logout")

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self.base_url = base_url

    def est_affiche(self):
        return self.est_present(self.DASHBOARD)

    def titre_tableau(self):
        return self.lire_texte(self.TITRE)

    def ouvrir_catalogue(self):
        from pages.catalogue_page import CataloguePage
        self.cliquer(self.LIEN_CATALOGUE)
        return CataloguePage(self.driver, self.base_url)

    def se_deconnecter(self):
        from pages.login_page import LoginPage
        self.cliquer(self.LOGOUT)
        return LoginPage(self.driver, self.base_url)
