import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from new_pages.login_page1 import Login
from utilities.configpar import ConfigReader
import os


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

    download_dir = os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_dir, exist_ok=True)

    driver = None
    if browser == "chrome":
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--start-maximized")
        # options.add_argument("--headless=new")  # Headless mode
        prefs = {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        }

        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(options=options)
        # driver = webdriver.Remote(command_executor=hub_url, options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--start-maximized")
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.dir", download_dir)
        profile.set_preference(
            "browser.helperApps.neverAsk.saveToDisk",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        driver = webdriver.Firefox(options=options, firefox_profile=profile)
        # driver = webdriver.Remote(command_executor=hub_url, options=options)

    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        prefs = {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True
        }
        options.add_experimental_option("prefs", prefs)
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

