import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from utilities.configpar import ConfigReader


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="staging")
    parser.addoption("--browsers", action="store", default="chrome")
    parser.addoption("--hub", action="store", default="http://localhost:4444/wd/hub")  # Hub URL


@pytest.fixture()
def setup(request):
    env = request.config.getoption("--env")
    browser = request.config.getoption("--browsers")
    # hub_url = request.config.getoption("--hub")

    # --------- Environment Config ---------
    if env == "staging":
        base_url = "https://app-staging.m5wtech.com/login"
        username = ConfigReader.read_config("staging-creds", "username")
        password = ConfigReader.read_config("staging-creds", "password")
    elif env == "test":
        base_url = "https://app-test-staging.wealthfy.com/"
        username = ConfigReader.read_config("Test-creds", "username")
        password = ConfigReader.read_config("Test-creds", "password")
    elif env == "dev":
        base_url = "https://app-dev-staging.wealthfy.com/login"
        username = ConfigReader.read_config("Dev-creds", "username")
        password = ConfigReader.read_config("Dev-creds", "password")
    else:
        base_url = "https://app-staging.m5wtech.com/login"

    # --------- Browser Options ---------
    driver = None
    if browser == "chrome":
        options = Options()
        # options.add_argument("--headless")
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
        # driver = webdriver.Remote(command_executor=hub_url, options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Firefox(options=options)
        # driver = webdriver.Remote(command_executor=hub_url, options=options)

    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Edge(options=options)
        # driver = webdriver.Remote(command_executor=hub_url, options=options)

    # --------- Common Setup ---------
    driver.get(base_url)
    driver.implicitly_wait(20)

    # Credentials assign kar
    request.cls.username = username
    request.cls.password = password

    yield driver
    driver.quit()
