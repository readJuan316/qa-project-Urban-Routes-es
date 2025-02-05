from driver import driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from locators import UrbanRoutesLocators
from selenium.webdriver.support import expected_conditions as EC
import data
from selenium import webdriver
from sms import create_driver_with_capabilities

class TestUrbanRoutes:

    driver = None
    routes_page = None

    @classmethod
    def setup_class(cls):
        cls.driver = create_driver_with_capabilities()
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesLocators(cls.driver)

    def test_set_route(self):
        """Prueba la seleccion de la ruta de origen y destino"""
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)

    def test_select_comfort_tariff(self):
        """Prueba la selección de la tarifa de confort."""
        self.driver.get(data.urban_routes_url)
        ## WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(UrbanRoutesLocators.comfort_tariff))
        routes_page = UrbanRoutesPage(self.driver)
        selected_tariff = self.driver.find_element(*UrbanRoutesLocators.comfort_tariff).get_attribute("class")
        ## assert "selected" in self.driver.find_element(*UrbanRoutesLocators.comfort_tariff).get_attribute("class")
        assert "active" in selected_tariff
