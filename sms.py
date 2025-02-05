from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import DesiredCapabilities

def create_driver_with_capabilities():
    from selenium.webdriver.chrome.options import Options

    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
    chrome_options = Options()
    chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
    service = Service()
    return webdriver.Chrome(service=service, options=chrome_options)


def retrieve_phone_code(driver) -> str:
    """This code retrieves phone confirmation number and returns it as a string.
    Use it when application waits for the confirmation code to pass it into your tests.
    The phone confirmation code can only be obtained after it was requested in application."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No phone confirmation code found.\n"
                            "Please use retrieve_phone_code only after the code was requested in your application.")
        return code