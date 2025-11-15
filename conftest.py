import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utilities.config_reader import read_config

@pytest.fixture(scope="class")
def setup(request):
    browser = read_config("DEFAULT", "browser").lower()
    if browser == "chrome":
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("Unsupported browser!")

    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver
    driver.quit()
