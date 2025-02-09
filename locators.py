import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from sms import retrieve_phone_code

class UrbanRoutesLocators:
    address_input = (By.ID, "address")
    request_taxi_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    mode_button = (By.CSS_SELECTOR, "modes-container")
    ask_taxi = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    tariff_picker = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]')

    comfort_tariff_button = (By.XPATH, "//div[contains(text(), 'Comfort')]")
    phone_number_button = (By.CLASS_NAME, "np-button")
    phone_input = (By.ID, 'phone')
    phone_submit_button = (By.XPATH, "//button[contains(text(),'Siguiente')]")
    next_button = (By.CLASS_NAME, "button.full")
    add_code= (By.ID, 'code')
    confirmation_code = (By.CLASS_NAME, "button.full")

    metodo_pago_button = (By.CLASS_NAME, 'pp-button')
    add_card_button = (By.XPATH, "//div[contains(text(), 'Agregar tarjeta')]")
    confirm_card_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    close_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    card_number_input = (By.ID, 'number')
    card_code_input = (By.XPATH, "//input[@id='code' and @placeholder='12']")

    card = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]')
    card_number_button = (By.CLASS_NAME, 'card_number_input')
    card_submit_button = (By.XPATH, "//button[contains(text(),'Agregar')]")
    card_code = (By.ID, 'code')
    card_space = (By.CLASS_NAME, "plc")
    close_card_button = (By.CLASS_NAME, "close-button.section-close")

    message_div = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[3]/div')
    driver_comment = (By.ID, "comment")
    comment_input = (By.XPATH, '//*[@id="comment"]')
    request_order = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[1]')
    blanket_tissues = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]')

    ice_cream_bucket = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    ice_cream_count = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]')

    ask_taxi_button = (By.XPATH, "//span[contains(text(),'Pedir un taxi')]")
    modal_taxi = (By.XPATH, '//*[@id="root"]/div/div[5]/div[2]/div[1]/div/div[1]')

    driver_information = (By.XPATH, '//*[@id="root"]/div/div[5]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

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

    def selected_phone_number_button(self):
        element = self.wait.until(EC.element_to_be_clickable(self.phone_number_button))
        element.click()

    def get_enter_phone_number(self, phone_number):
        phone_field = self.wait.until(EC.element_to_be_clickable(self.phone_input))
        phone_field.clear()
        phone_field.send_keys(phone_number)
        self.driver.find_element(*self.phone_submit_button).click()

        "Esperar que aparezca la ventana emergente"
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Introduce el código')]"))
        )

        "Obtener el código"
        code = retrieve_phone_code(self.driver)

        "Ingresar el código"
        code_input = self.driver.find_element(By.ID,'code')
        code_input.clear()
        code_input.send_keys(code)

        "Hacer clic"
        confirm = self.driver.find_element(By.XPATH, "//button[contains(text(),'Confirmar')]")
        confirm.click()

    def get_display_phone_number(self):
        element = self.driver.find_element(*self.phone_input)
        return element.get_attribute('value')

    def selected_card_number_button(self):
        element = self.wait.until(EC.element_to_be_clickable(self.metodo_pago_button))
        element.click()

    def get_card_number(self, card_number, card_code):
        "Agregar número de tarjeta"
        add_card_element = self.wait.until(EC.element_to_be_clickable(self.add_card_button))
        add_card_element.click()

        card_number_field = self.wait.until(EC.visibility_of_element_located(self.card_number_input))
        card_number_field.clear()
        card_number_field.send_keys(card_number)

        "Agregar código de tarjeta"
        card_code_field = self.wait.until(EC.visibility_of_element_located(self.card_code_input))
        card_code_field.clear()
        card_code_field.send_keys(card_code)

        "Hacer clic en cualquier parte de la pantalla"
        self.driver.find_element(By.TAG_NAME,'body').click()

        "Hacer clic al botón agregar"
        confirm_button = self.wait.until(EC.element_to_be_clickable(self.confirm_card_button))
        confirm_button.click()

        "Cerrar el popup"
        close_button = self.wait.until(EC.element_to_be_clickable(self.close_button))
        close_button.click()

    def is_card_add(self):
        self.driver.find_element(*self.close_button)
        return True

    def set_driver_comment(self, comment):
        "Escribir mensaje al conductor"
        message_div_element = self.wait.until(EC.element_to_be_clickable(self.message_div))
        message_div_element.click()
        driver_comment = self.wait.until(EC.visibility_of_element_located(self.driver_comment))
        driver_comment.clear()
        driver_comment.send_keys(comment)

    def get_display_driver_comment(self):
        element = self.driver.find_element(*self.comment_input)
        return element.get_attribute('value')

    def open_section(self):
        reqs_section = self.driver.find_element(By.CLASS_NAME, 'reqs')
        class_reqs_open = reqs_section.get_attribute('class')
        if 'open' not in class_reqs_open:
            header = reqs_section.find_element(By.CLASS_NAME, 'reqs-header')
            header.click()
            WebDriverWait(self.driver,10).until(
                lambda driver: 'open' in reqs_section.get_attribute('class')
            )

    def toggle_blanket(self):
        self.open_section()
        blanket_button = self.wait.until(EC.element_to_be_clickable(self.blanket_tissues))
        blanket_button.click()

    def is_blanket_select(self):
        self.open_section()
        blanket_switch = self.driver.find_element(*self.blanket_tissues)
        class_reqs_open = blanket_switch.get_attribute('class')
        return class_reqs_open

    def add_two_ice_cream(self):
        self.open_section()
        ice_plus = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ice_cream_bucket)
        )
        for _ in range(2):
            ice_plus.click()
            time.sleep(0.5)

    def get_ice_cream_count(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.ice_cream_count)
        )
        count_text = element.text
        return int(count_text)

    def click_ask_taxi(self):
        request_button = self.wait.until(EC.element_to_be_clickable(self.ask_taxi_button))
        request_button.click()

    def is_search(self):
        "Esperar que aparezca la ventana emergente modal"
        self.wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, 'order-header-title'),'Buscar automóvil')
        )
        return True

    def selected_modal_taxi(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.driver_information))
        time.sleep(5)

    def is_display_modal_taxi(self):
        self.wait.until(EC.visibility_of_element_located(self.driver_information))
        return True