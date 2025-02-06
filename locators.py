import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
#from urllib3.util.wait import select_wait_for_socket
#from utilities import retrieve_phone_code

class UrbanRoutesLocators:
    address_input = (By.ID, "address")
    request_taxi_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    mode_button = (By.CSS_SELECTOR, "modes-container")
    ask_taxi = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    tariff_picker = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]')
    #comfort_tariff_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
    comfort_tariff_button = (By.XPATH, "//div[contains(text(), 'Comfort')]")
    phone = (By.CLASS_NAME, "np-button")
    add_phone_number = (By.ID, 'phone')
    next_button = (By.CLASS_NAME, "button.full")
    add_code= (By.ID, 'code')
    confirmation_code = (By.CLASS_NAME, "button.full")
    payment_method = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]')
    card = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]')
    card_number = (By.XPATH, '//*[@id="number"]')
    card_code = (By.XPATH, '//*[@id="code"]')
    add_credit_card = (By.CLASS_NAME, "button.full")
    card_space = (By.CLASS_NAME, "plc")
    close_card_button = (By.CLASS_NAME, "close-button.section-close")
    driver_message = (By.ID, "comment")
    request_order = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[1]')
    blanket_tissues = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]')
    ice_cream_bucket = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]')
    close_button_payment_method = (
    By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')
    current_payment_method = (By.CLASS_NAME, 'pp-value-text')
    payment_method_select = (By.XPATH, '//div[@class="pp-button filled"]//div[contains(text(), "Payment method")]')


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_element(self, locator):
        """Espera a que un elemento esté visible en la página"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def set_from(self, from_address):
        """Configurar el campo 'Desde'"""
        from_field = self.wait.until(EC.visibility_of_element_located(self.from_field))
        from_field.clear()
        from_field.send_keys(from_address)

    def set_to(self, to_address):
        """Configurar el campo 'Hasta'"""
        to_field = self.wait.until(EC.visibility_of_element_located(self.to_field))
        to_field.clear()
        to_field.send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')


    def select_request_taxi(self):
        element = self.wait.until(EC.element_to_be_clickable(self.request_taxi_button))
        element.click()

    def select_comfort_tariff(self):
        element = self.wait.until(EC.element_to_be_clickable(self.comfort_tariff_button))
        element.click()

    def get_selected_tariff(self):
        element = self.driver.find_element(*self.comfort_tariff_button)
        return element.text

    def set_message_for_driver(self, message):
        "Agrega un mensaje para el conductor"
        driver_message = self.wait.until(EC.visibility_of_element_located(self.driver_message))
        driver_message.clear()
        driver_message.send_keys(message)

        return self.driver.find_element(*self.comfort_tariff).get_property('class')

    def set_add_phone_number(self, phone_number):
        "Configura el número de teléfono"
        phone_input = self.wait.until(EC.presence_of_element_located(self.add_phone_number))
        phone_input.clear()
        phone_input.send_keys(phone_number)
        self.wait_for_element(EC.element_to_be_clickable(self.next_button)).click()

    def get_add_phone_number(self):
        element = self.driver.find_element(*self.add_phone_number)
        return element.click

    def add_credit_card(self, card_number, card_code):
        "Agrega una tarjeta de crédito"
        card_number = self.wait.until(EC.visibility_of_element_located(self.card_number))
        card_number = self.wait.until(EC.visibility_of_element_located(self.card_code))
        card_number.clear()
        card_number.send_keys(card_number)
        card_number = self.wait.until(EC.visibility_of_element_located(self.card_number)).click()
        self.wait_for_element(EC.visibility_of_element_located(self.add_credit_card))

    def request_blanket_and_tissues(self, blanket_tissues):
        """Selecciona las opciones de manta y pañuelos"""
        blanket_and_tissues = self.wait.until(EC.visibility_of_element_located(self.blanket_tissues))
        self.wait_for_element(EC.visibility_of_element_located(self.blanket_tissues)).click()

    def request_ice_cream(self, quantity):
        """Solicita una cantidad específica de helado"""
        ice_cream_selector = self.wait.until(EC.visibility_of_element_located(self.ice_cream_bucket))
        ice_cream_selector.clear()
        ice_cream_selector.send_keys(str(quantity))

    def click_request_taxi(self):
        """Hace clic en el botón 'Pedir un taxi'"""
        request_button = self.wait.until(EC.visibility_of_element_located(self.request_taxi_button))
        request_button.click()

