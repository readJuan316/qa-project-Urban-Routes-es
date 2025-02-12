from selenium.webdriver.common.by import By

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
    phone_code_input = (By.XPATH, "//div[contains(text(),'Introduce el código')]")
    code_input = (By.ID,'code')
    confirm_button = (By.XPATH, "//button[contains(text(),'Confirmar')]")

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
    body_submit = (By.TAG_NAME,'body')

    message_div = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[3]/div')
    driver_comment = (By.ID, "comment")
    comment_input = (By.XPATH, '//*[@id="comment"]')
    request_order = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[1]')
    blanket_tissues = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]')

    open_reqs = (By.CLASS_NAME, 'reqs')
    open_reqs_header = (By.CLASS_NAME, 'reqs-header')

    ice_cream_bucket = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    ice_cream_count = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]')

    ask_taxi_button = (By.XPATH, "//span[contains(text(),'Pedir un taxi')]")
    modal_taxi = (By.XPATH, '//*[@id="root"]/div/div[5]/div[2]/div[1]/div/div[1]')
    search_car = (By.CLASS_NAME, 'order-header-title')

    driver_information = (By.XPATH, '//*[@id="root"]/div/div[5]')

