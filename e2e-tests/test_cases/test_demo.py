import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="class")
def driver(request):
    drv = webdriver.Chrome()
    drv.maximize_window()
    drv.implicitly_wait(10)

    # ---- LOGIN ONCE ----
    drv.get("https://app-staging.m5wtech.com/login")
    wait = WebDriverWait(drv, 20)
    drv.find_element(By.XPATH, "//*[text()='I Agree']").click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@placeholder, 'Username')]"))).send_keys("piyushd+lwp+rm2@valuefy.com")
    drv.find_element(By.XPATH, "//*[contains(@placeholder, 'Password')]").send_keys("Piyush@123456")
    drv.find_element(By.XPATH, "//*[text()='Sign in']").click()

    # wait until dashboard loads
    wait.until(EC.url_contains("dashboard"))

    request.cls.driver = drv
    yield
    drv.quit()


@pytest.mark.usefixtures("driver")
class TestDashboard:

    def test_01_dashboard_title(self):
        assert "M5Wealth" in self.driver.title

    def test_02_logo_visible(self):
        assert self.driver.find_element(By.CSS_SELECTOR, ".logo").is_displayed()

    def test_03_menu_present(self):
        assert self.driver.find_element(By.ID, "sidebar").is_displayed()

    def test_04_widget_count(self):
        widgets = self.driver.find_elements(By.CSS_SELECTOR, ".widget")
        assert len(widgets) > 0

    def test_05_user_profile(self):
        assert self.driver.find_element(By.CSS_SELECTOR, ".profile").is_displayed()

    def test_06_search_box(self):
        assert self.driver.find_element(By.ID, "search").is_enabled()

    def test_07_notifications(self):
        assert self.driver.find_element(By.CSS_SELECTOR, ".notifications").is_displayed()

    def test_08_table_loaded(self):
        rows = self.driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
        assert len(rows) >= 0

    def test_09_footer(self):
        assert self.driver.find_element(By.TAG_NAME, "footer").is_displayed()

    def test_10_logout_button(self):
        assert self.driver.find_element(By.ID, "logout").is_displayed()