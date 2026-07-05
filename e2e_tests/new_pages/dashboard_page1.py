import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from uihelper.helper_file import UI_Helper


class DashboardList(UI_Helper):
    HUMBERGER_MENU_XPATH = (By.XPATH, "//*[contains(@class,'lucide lucide-menu')]")
    SELECT_DASHBOARD_LIST_XPATH = (By.XPATH, "//*[contains(text(), 'Dashboards List')]")
    CLICK_ON_THE_PLUS_BUTTON = (By.XPATH, "//*[contains(@class, '10 w-10')]")
    SEND_DASHBOARD_NAME_ID = (By.ID, "dashboard-name")
    SEND_DASHBOARD_DESCRIPTION_ID = (By.ID, "dashboard-description")
    CREATE_DASHBOARD_BUTTON_XPATH = (By.XPATH, "//*[text()='Create Dashboard']")
    ASSERT_ON_SUCCESFUL_CREATION_DASHBOARD_XPATH = (By.XPATH, "//*[text()='Dashboard created successfully']")
    ASSERT_FOR_NAME_TEXT_BOX_XPATH = (By.XPATH, "//*[text()='Name can not be empty']")
    ASSERT_FOR_DESCRIPTION_TEXT_BOX_XPATH = (By.XPATH, "//*[text()='Description can not be empty']")
    CLICK_DESCRIPTION_XPATH = (By.XPATH, "//*[text()='Description']")

    #activity logs
    HUMBERGER_MENU_ACTIVITY_LOG_XPATH = (By.XPATH, "//*[contains(@class, 'hamburger')]")
    CLICK_ON_ACTIVITY_LOG_XPATH = (By.XPATH, "//*[contains(text(), 'Activity Logs')]")
    CREATE_DASHBOARD_LOG_XPATH = (By.XPATH, "(//td[12])[2]")
    VISITED_DASHBOARD_LOG_XPATH = (By.XPATH, "(//td[12])[1]")
    DELETE_DASHBOARD_XPATH = (By.XPATH, "//*[text()='Piyush27471']/parent::div/parent::td/parent::tr/td[7]/div/button[4]")
    CLICK_ON_YES_XPATH = (By.XPATH, "//*[text()='Yes']")
    CLICK_ON_PLUS_ICON_XPATH = (By.XPATH, "//button[contains(@class, 'h-10 w-10')]")
    SELECT_ALL_WIDGET_CLICK_XPATH = (By.XPATH, "//*[contains(text(),'Select All')]")
    CLICK_ON_APPLY_BUTTON_XPATH = (By.XPATH, "(//*[contains(text(),'Apply')])[2]")
    CLICK_ON_SAVE_BUTTON_XPATH = (By.XPATH, "(//*[contains(@class,'[40px] h-10')])[2]")
    CLICK_ON_THE_VIEW_MODE_XPATH = (By.XPATH, "(//*[contains(@class,'[40px] h-10')])[4]")
    ADD_WIDGET_LOGS_XPATH = (By.XPATH, "(//td[11])[2]")
    DASHBOARD_SAVE_LOGS_XPATH = (By.XPATH, "(//td[11])[1]")
    SCROLL_DOWN_TO_CLIENT_LIST_XPATH = (By.XPATH, "//h3[text()='Clients List']")
    ASSERT_FOR_NAVIGATE_TO_CLIENT_DASH_XPATH = (By.XPATH, "(//td[12])[1]")
    #Dashboard elements
    SCROLL_DOWN_TO_GROUP_LIST_XPATH = (By.XPATH, "//h3[text()='Groups List']")
    EDIT_BUTTON_DASHBOARD_XPATH = (By.XPATH, "(//*[contains(@class,'[40px] h-10')])[1]")
    NEW_DASHBOARD_NAME_ID = (By.ID, "name")
    VERIFY_NEW_DASHBOARD_NAME_ID = (By.ID, "dashboard-title")
    CLICK_ON_CURRENCY_DROP_DOWN_CSS = (By.CSS_SELECTOR,'button.flex.items-center.justify-between.rounded-md:nth-of-type(2)')
    CHANGE_CURRENCY_XPATH = (By.XPATH, "//*[text()='INR - Indian Rupee']")
    CLICK_ON_NEW_APPLY_BUTTON_XPATH = (By.XPATH, "//*[contains(text(),'Apply')]")
    TOGGLE_BUTTON_CSS = (By.CSS_SELECTOR, "button.peer")
    CLICK_ON_DATE_CSS = (By.CSS_SELECTOR, "button.inline-flex.transition-all.duration-200")
    SEND_FROM_DATE_IN_CALENDER_XPATH = (By.XPATH, "//input[@placeholder='Start date']")
    SEND_TO_DATE_IN_CALENDER_XPATH = (By.XPATH, "//input[@placeholder='End date']")
    VERIFY_DATE_PERIOD_CSS = (By.CSS_SELECTOR, "div.flex.items-center.bg-transparent")

    #theme
    CLICK_ON_THEME_CSS = (By.CSS_SELECTOR, "div.w-6.h-6.rounded-lg")
    FOREST_THEME_SELECTION_XPATH = (By.XPATH, "//*[text()='Forest']")
    VERIFY_THEME_XPATH = (By.XPATH, "//*[@fill='#2D6A4F']")



    def __init__(self,driver):
        self.driver = driver

    def dashboard_creation(self,dashboard_name,dashboard_description):
        # self.driver.refresh()
        self.do_click(self.HUMBERGER_MENU_XPATH)
        time.sleep(2)
        self.js_click(self.SELECT_DASHBOARD_LIST_XPATH)
        # self.do_click(self.SELECT_DASHBOARD_LIST_XPATH)
        self.do_click(self.CLICK_ON_THE_PLUS_BUTTON)
        self.send_key(self.SEND_DASHBOARD_NAME_ID,dashboard_name)
        self.send_key(self.SEND_DASHBOARD_DESCRIPTION_ID, dashboard_description)
        self.do_click(self.CREATE_DASHBOARD_BUTTON_XPATH)

    def dashboard_creation_without_input(self, dashboard_name, dashboard_description):
        self.do_click(self.HUMBERGER_MENU_XPATH)
        time.sleep(2)
        self.do_click(self.SELECT_DASHBOARD_LIST_XPATH)
        self.do_click(self.CLICK_ON_THE_PLUS_BUTTON)
        self.send_key(self.SEND_DASHBOARD_NAME_ID, dashboard_name)
        self.send_key(self.SEND_DASHBOARD_DESCRIPTION_ID, dashboard_description)
        # self.do_click(self.CLICK_DESCRIPTION_XPATH)

    def after_create_dashboard_log_generate_check(self):
        time.sleep(3)
        self.do_click(self.HUMBERGER_MENU_XPATH)
        time.sleep(2)
        self.do_click(self.CLICK_ON_ACTIVITY_LOG_XPATH)
        self.dasboard_creation_log = self.get_text(self.CREATE_DASHBOARD_LOG_XPATH)
        self.dasboard_visited_log  = self.get_text(self.VISITED_DASHBOARD_LOG_XPATH)
        print(self.dasboard_creation_log, self.dasboard_visited_log)

    def delete_dashboard(self,name):
        time.sleep(2)
        # if self.is_element_present(self.HUMBERGER_MENU_XPATH):
        #     self.do_click(self.HUMBERGER_MENU_XPATH)
        # elif self.is_element_present(self.HUMBERGER_MENU_ACTIVITY_LOG_XPATH):
        #      self.do_click(self.HUMBERGER_MENU_ACTIVITY_LOG_XPATH)
        # else:
        #     time.sleep(1)
        self.js_click(self.HUMBERGER_MENU_XPATH)
        time.sleep(2)
        # self.do_click(self.SELECT_DASHBOARD_LIST_XPATH)
        self.js_click(self.SELECT_DASHBOARD_LIST_XPATH)
        time.sleep(4)
        self.driver.find_element(By.XPATH,
                                 f"//*[contains(text(),'{name}')]/parent::div/parent::td/parent::tr/td[7]/div/button[4]").click()
        self.do_click(self.CLICK_ON_YES_XPATH)

    def delete_dashboard_part_2(self,name):
        time.sleep(2)
        try:
            if self.driver.find_element(By.CSS_SELECTOR, "svg.lucide.lucide-menu").is_displayed():
                self.driver.find_element(By.CSS_SELECTOR, "svg.lucide.lucide-menu").click()
                self.js_click(self.SELECT_DASHBOARD_LIST_XPATH)
                time.sleep(4)
                self.driver.find_element(By.XPATH,
                                         f"//*[contains(text(),'{name}')]/parent::div/parent::td/parent::tr/td[7]/div/button[4]").click()
                self.do_click(self.CLICK_ON_YES_XPATH)
            else:
                self.js_click(self.HUMBERGER_MENU_ACTIVITY_LOG_XPATH)
                self.js_click(self.SELECT_DASHBOARD_LIST_XPATH)
                time.sleep(4)
                self.driver.find_element(By.XPATH,
                                         f"//*[contains(text(),'{name}')]/parent::div/parent::td/parent::tr/td[7]/div/button[4]").click()
                self.do_click(self.CLICK_ON_YES_XPATH)

        except Exception as E:
            print(E)
        time.sleep(5)


    def add_all_widget_and_save_navigate_acitvitylog(self):
        time.sleep(2)
        self.do_click(self.CLICK_ON_PLUS_ICON_XPATH)
        self.do_click(self.SELECT_ALL_WIDGET_CLICK_XPATH)
        self.do_click(self.CLICK_ON_APPLY_BUTTON_XPATH)
        self.do_click(self.CLICK_ON_SAVE_BUTTON_XPATH)
        time.sleep(3)
        self.do_click(self.HUMBERGER_MENU_XPATH)
        time.sleep(2)
        self.do_click(self.CLICK_ON_ACTIVITY_LOG_XPATH)
        self.do_click(self.CLICK_ON_THE_VIEW_MODE_XPATH)
        self.widget_update = self.get_text(self.ADD_WIDGET_LOGS_XPATH)
        self.saved_dashboard = self.get_text(self.DASHBOARD_SAVE_LOGS_XPATH)

    def add_all_widget_and_save(self):
        time.sleep(2)
        self.do_click(self.CLICK_ON_PLUS_ICON_XPATH)
        self.do_click(self.SELECT_ALL_WIDGET_CLICK_XPATH)
        self.js_click(self.CLICK_ON_APPLY_BUTTON_XPATH)
        self.js_click(self.CLICK_ON_SAVE_BUTTON_XPATH)
        self.js_click(self.CLICK_ON_THE_VIEW_MODE_XPATH)

    def edit_dashboard_name(self,newDashboard_name):
        self.do_click(self.EDIT_BUTTON_DASHBOARD_XPATH)
        self.send_key(self.NEW_DASHBOARD_NAME_ID, newDashboard_name)
        self.do_click(self.CLICK_ON_SAVE_BUTTON_XPATH)
        time.sleep(2)

    def set_currency(self):
        self.js_click(self.CLICK_ON_CURRENCY_DROP_DOWN_CSS)
        self.js_click(self.CHANGE_CURRENCY_XPATH)
        self.do_click(self.CLICK_ON_NEW_APPLY_BUTTON_XPATH)

    def handle_the_toggle(self):
        self.js_click(self.TOGGLE_BUTTON_CSS)
        self.toggle = self.get_attribute(self.TOGGLE_BUTTON_CSS, "aria-checked")

    def enter_date_in_calender(self,from_date, to_date):
        time.sleep(2)
        self.do_click(self.CLICK_ON_DATE_CSS)
        try:
            self.send_key(self.SEND_FROM_DATE_IN_CALENDER_XPATH, from_date)
            self.send_key(self.SEND_FROM_DATE_IN_CALENDER_XPATH,Keys.ENTER)
            self.clear_text(self.SEND_TO_DATE_IN_CALENDER_XPATH)
            self.send_key(self.SEND_TO_DATE_IN_CALENDER_XPATH, to_date)
            self.send_key(self.SEND_TO_DATE_IN_CALENDER_XPATH, Keys.ENTER)
            self.do_click(self.CLICK_ON_NEW_APPLY_BUTTON_XPATH)
            time.sleep(3)
        except:
            None



    def navigate_to_RM_dashboard_from_client_list(self, clinet_name):
        self.scroll_down_toElement(self.SCROLL_DOWN_TO_CLIENT_LIST_XPATH)
        self.driver.find_element(By.XPATH, f"//*[text()='{clinet_name}']").click()
        time.sleep(3)


    def validate_the_log_for_navigation_to_client_dashboard(self):
        time.sleep(2)
        self.do_click(self.HUMBERGER_MENU_XPATH)
        self.do_click(self.CLICK_ON_ACTIVITY_LOG_XPATH)
        self.client_navigation = self.get_text(self.ASSERT_FOR_NAVIGATE_TO_CLIENT_DASH_XPATH)


    def navigate_the_log_form_group_list_to_client_dashboard(self,group_name):
        self.scroll_down_toElement(self.SCROLL_DOWN_TO_GROUP_LIST_XPATH)
        self.driver.find_element(By.XPATH, f"//*[text()='{group_name}']").click()
        time.sleep(3)

    def change_the_theme(self):
        self.do_click(self.CLICK_ON_THEME_CSS)
        self.do_click(self.FOREST_THEME_SELECTION_XPATH)
        time.sleep(3)





















