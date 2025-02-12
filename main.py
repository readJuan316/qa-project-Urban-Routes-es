import data

from page import UrbanRoutesPage
from sms import create_driver_with_capabilities

class TestUrbanRoutes:

    driver = None
    routes_page = None

    @classmethod
    def setup_class(cls):
        cls.driver = create_driver_with_capabilities()
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)

    def test_request_taxi(self):
        """Prueba la seleccion de la ruta de origen y destino"""
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)

        self.routes_page.select_request_taxi()

    def test_select_comfort_tariff(self):
        """Prueba la selección de la tarifa de confort."""
        self.routes_page.select_comfort_tariff()
        selected_tariff = self.routes_page.get_selected_tariff()
        assert selected_tariff == "Comfort"

    def test_request_phone_number(self):
        self.routes_page.selected_phone_number_button()
        self.routes_page.get_enter_phone_number(data.phone_number)
        phone_number_test = '+1 123 123 12 12'
        display_phone_number = self.routes_page.get_display_phone_number()
        assert display_phone_number == phone_number_test

    def test_request_card_number(self):
        self.routes_page.selected_card_number_button()
        self.routes_page.get_card_number(data.card_number, data.card_code)
        display_card_number = self.routes_page.is_card_add()
        assert display_card_number

    def test_driver_comment(self):
        self.routes_page.set_driver_comment(data.message_for_driver)
        display_driver_comment = self.routes_page.get_display_driver_comment()
        #self.routes_page.set_route(driver_comment)
        assert display_driver_comment

    def test_blanket_and_tissues(self):
        self.routes_page.toggle_blanket()
        blanket_switch = self.routes_page.is_blanket_select()
        assert blanket_switch

    def test_ice_cream(self):
        self.routes_page.add_two_ice_cream()
        ice_count = self.routes_page.get_ice_cream_count()
        assert ice_count == 2

    def test_ask_taxi(self):
        self.routes_page.click_ask_taxi()
        search_true = self.routes_page.is_search()
        assert search_true

    def test_display_modal_taxi(self):
        self.routes_page.selected_modal_taxi()
        display_true = self.routes_page.is_display_modal_taxi()
        assert display_true

    @classmethod
    def close_class(cls):
        cls.driver.quit()
