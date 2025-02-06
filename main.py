#from driver import driver
#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.support.wait import WebDriverWait
#from data import phone_number
from locators import UrbanRoutesLocators
#from selenium.webdriver.support import expected_conditions as EC
import data
#from selenium import webdriver
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

    def test_request_taxi(self):
        self.routes_page.select_request_taxi()

    def test_select_comfort_tariff(self):
        """Prueba la selección de la tarifa de confort."""
        self.routes_page.select_comfort_tariff()
        selected_tariff = self.routes_page.get_selected_tariff()
        assert selected_tariff == "Comfort"

    def test_add_phone_number(self):
        """Prueba la introducción del número de teléfono."""
        self.routes_page.add_phone_number(data.phone_number)
        selected_phone_number = self.routes_page.get_add_phone_number()
        assert selected_phone_number == "phone"

