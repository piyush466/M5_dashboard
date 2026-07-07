from datetime import datetime
import time
import os
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from uihelper.helper_file import UI_Helper


class ClinetNeedAttentionWidget(UI_Helper):

    GET_ALL_COLUMNS_NAME_XPATH = (By.XPATH,
                                  "//*[@data-widget-id='Client Needs Attention']/div/div/div[2]/div[2]/div/table/thead/tr")

    CLICK_ON_DROP_DOWN_XPATH = (
        By.XPATH, '(//*[@data-widget-id="Client Needs Attention"]/div/div/div[2]/div/div/button/span)[1]'
    )

    GET_ALL_DROPDOWN_VALUES_XPATH = (By.XPATH,
                                     "//span[contains(@id,'radix-')]"
    )

    GET_DAYS_DRODPDOWN_VALUES_XPATH = (By.XPATH,
                                       "//button[contains(@class,'flex w-full items-center gap-2')]/span")

    CLICK_ON_DAYS_DROPDOWN_XPATH = (By.XPATH,
                                    '//div[@class="flex items-center gap-2"]/button[2]')

    HOVER_ON_I_ICON_XPATH = (By.XPATH,
                             "//*[text()='Client Needs Attention']//parent::div[1]/button")

    CLICK_ON_EXCEL_DOWNLOAD_XPATH = (By.XPATH,
                                     "//button[@title='Export']")

    HOVER_ON_BELL_ICON_XPATH = (By.XPATH,
                                "//button[@title='Export Status']")

    CLICK_ON_DOWNLOAD_BUTTON_XPATH = (By.XPATH,
                                      '//div[@data-widget-id="Client Needs Attention"]//button[text()=" Download"]')

    GET_FIRST_NAME_XPATH = (By.XPATH,
                            "(//span[@class='cursor-default'])[1]")

    SEND_USER_NAME_IN_SEARCH_XPATH = (By.XPATH,
                            '//div[@data-widget-id="Client Needs Attention"]//input')

    GET_EXPIRY_DATE_XPATH = (By.XPATH,
                             '(//div[@data-widget-id="Client Needs Attention"]//table/tbody/tr/td[3])[1]')

    GET_USER_STATUS_XPATH = (By.XPATH,
                             '(//div[@data-widget-id="Client Needs Attention"]//table/tbody/tr/td[2])[1]')

    PAGINATION_TEXT_DISPLAYED_XPATH = (By.XPATH,
                                       "//span[@class='flex-1 whitespace-nowrap px-2 text-sm text-muted-foreground']")

    CLICK_ON_TAKE_ACTION_BUTTON_XPATH = (By.XPATH,
                                         "(//button[text()='Take Action'])[1]")


    GET_TEXT_FROM_ONBOARDING_ACCOUNT_XPATH = (By.XPATH,
                                     "//h2[contains(@class,'capitalize text-ellipsis')]")

    GET_ALL_USERS_NAME_XPATH = (By.XPATH,
                                '//div[@data-widget-id="Client Needs Attention"]//tbody/tr/td/div')

    CLICK_ON_IRPQ_NEXT_REVIEW_DATE_XPATH = (By.XPATH,
                                            "//*[text()='IRPQ Next Review']")

    CLICK_OM_RISK_ANALYSIS_FORM_XPATH = (By.XPATH,
                                         "//*[text()='Risk Analysis']")

    CLICK_ON_VIEW_RISK_PROFILE_BUTTON_XPATH = (By.XPATH,
                                               "//*[text()='View Risk Profile']")

    GET_IRPQ_DATE_FROM_RISK_ANALYSIS_FORM_XPATH = (By.XPATH,
                                                   "//h3[text()='Next Review Date']//parent::div/p")


    def __init__(self,driver):
        self.driver = driver

    def navigate_to_client_need_attention_widget(self):
        self.scroll_down_toElement(self.GET_ALL_COLUMNS_NAME_XPATH)

    def get_all_drop_down_values(self):
        time.sleep(4)
        self.is_element_present(self.CLICK_ON_DROP_DOWN_XPATH)
        self.js_click(self.CLICK_ON_DROP_DOWN_XPATH)
        all_ele = WebDriverWait(self.driver, 25).until(EC.visibility_of_all_elements_located((By.XPATH,"//span[contains(@id,'radix-')]")))
        # all_ele = self.driver.find_elements(By.XPATH, "//span[contains(@id,'radix-')]")
        self.all_dropdown_values = []
        for ele in all_ele:
            self.all_dropdown_values.append(ele.text)

    def get_all_days_dropdown_values(self):
        time.sleep(4)
        self.is_element_present(self.CLICK_ON_DAYS_DROPDOWN_XPATH)
        self.js_click(self.CLICK_ON_DAYS_DROPDOWN_XPATH)
        all_days = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH,"//button[contains(@class,'flex w-full items-center gap-2')]/span")))
        self.all_days_dropdown_values = []
        for days in all_days:
            self.all_days_dropdown_values.append(days.text)

    def download_excel(self):
        print(self.get_currnt_time())
        # self.DOWNLOAD_FOLDER = "/Users/piyushshdravyakar/Downloads"
        self.DOWNLOAD_FOLDER = os.path.join(os.getcwd(), "downloads")
        # os.makedirs(self.DOWNLOAD_FOLDER, exist_ok=True)
        self.is_enable(self.CLICK_ON_EXCEL_DOWNLOAD_XPATH)
        self.is_element_present(self.CLICK_ON_EXCEL_DOWNLOAD_XPATH)
        self.js_click(self.CLICK_ON_EXCEL_DOWNLOAD_XPATH)
        self.hover_onElement(self.HOVER_ON_BELL_ICON_XPATH)
        self.is_element_present(self.CLICK_ON_DOWNLOAD_BUTTON_XPATH)
        self.until_clickable(self.CLICK_ON_DOWNLOAD_BUTTON_XPATH)
        time.sleep(2)
        self.downloaded = False
        for file in os.listdir(self.DOWNLOAD_FOLDER):
            if file.startswith(f"ClientNeedsAttention_export_{self.get_currnt_time()}") and file.endswith(".xlsx"):
                self.downloaded = True
                print("Downloaded File:", file)
                break

    def search_user_name_in_search_box(self):
        self.username = self.get_text(self.GET_FIRST_NAME_XPATH).lower()
        self.send_key(self.SEND_USER_NAME_IN_SEARCH_XPATH, self.username)
        self.get_usernames = WebDriverWait(self.driver,15).until(EC.visibility_of_all_elements_located((By.XPATH,'//div[@data-widget-id="Client Needs Attention"]//tbody/tr/td/div/span')))
        self.all_usernames_in_list = []
        for username in self.get_usernames:
            all_username = username.text
            self.all_usernames_in_list.append(all_username.lower())

    def critical_status_displayed_less_than_today(self):
        time.sleep(3)
        self.is_displayed(self.GET_EXPIRY_DATE_XPATH)
        self.wait_until_displayed(self.GET_EXPIRY_DATE_XPATH)
        self.is_element_present(self.GET_EXPIRY_DATE_XPATH)
        self.get_expiry_date = self.get_text(self.GET_EXPIRY_DATE_XPATH)
        self.wait_until_displayed(self.GET_EXPIRY_DATE_XPATH)
        print(self.get_expiry_date)
        expiry_date = datetime.strptime(self.get_expiry_date, "%d-%b-%Y").date()
        today = datetime.today().date()
        time.sleep(6)
        days_difference = (expiry_date - today).days
        self.get_status = self.get_text(self.GET_USER_STATUS_XPATH)
        if days_difference <= 0:
            self.expected_status = "Critical"
        elif 1 <= days_difference <= 7:
            self.expected_status = "High"
        elif 8 <= days_difference <= 15:
            self.expected_status = "Medium"
        elif 16 <= days_difference <= 30:
            self.expected_status = "Low"
        else:
            self.expected_status = None



    def user_navigate_to_onboarding_using_take_action_button(self):
        self.wait_until_displayed(self.GET_FIRST_NAME_XPATH)
        self.first_name = self.get_text(self.GET_FIRST_NAME_XPATH).lower()
        self.wait_until_displayed(self.CLICK_ON_TAKE_ACTION_BUTTON_XPATH)
        self.js_click(self.CLICK_ON_TAKE_ACTION_BUTTON_XPATH)
        self.wait_until_displayed(self.GET_TEXT_FROM_ONBOARDING_ACCOUNT_XPATH)
        self.get_expected_text = self.get_text(self.GET_TEXT_FROM_ONBOARDING_ACCOUNT_XPATH).lower()


    def select_irpq_review_date(self):
        time.sleep(4)
        self.is_element_present(self.CLICK_ON_DROP_DOWN_XPATH)
        self.js_click(self.CLICK_ON_DROP_DOWN_XPATH)
        self.js_click(self.CLICK_ON_IRPQ_NEXT_REVIEW_DATE_XPATH)

    def click_on_take_action_and_go_risk_analysis_form(self):
        time.sleep(30)
        self.irpq_next_review_dt = self.get_text(self.GET_EXPIRY_DATE_XPATH)
        self.irpq_expiry_date = str(datetime.strptime(self.irpq_next_review_dt, "%d-%b-%Y").date())
        print(self.irpq_expiry_date)
        self.until_clickable(self.CLICK_ON_TAKE_ACTION_BUTTON_XPATH)
        self.scroll_down_toElement(self.CLICK_OM_RISK_ANALYSIS_FORM_XPATH)
        self.do_click(self.CLICK_OM_RISK_ANALYSIS_FORM_XPATH)
        self.do_click(self.CLICK_ON_VIEW_RISK_PROFILE_BUTTON_XPATH)
        self.get_irpq_date_from_risk_form = self.get_text(self.GET_IRPQ_DATE_FROM_RISK_ANALYSIS_FORM_XPATH)
        cleaned_date = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', self.get_irpq_date_from_risk_form)
        self.formatted_date = datetime.strptime(cleaned_date, "%B %d, %Y").strftime("%Y-%m-%d")
        print(self.formatted_date)







