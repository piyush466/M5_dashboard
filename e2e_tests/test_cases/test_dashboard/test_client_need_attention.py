from faker import Faker

from new_pages.dashboard.client_need_attention_widget import ClinetNeedAttentionWidget
from new_pages.dashboard_page1 import DashboardList
from new_pages.login_page1 import Login
from utilities.configpar import ConfigReader


class TestClientNeedAttention:
    fake_name = Faker()
    name = fake_name.name()
    username = ConfigReader.read_config("tenant5", "username")
    password = ConfigReader.read_config("tenant5", "password")

    def open_client_need_attention_widget(self, setup):
        login = Login(setup)
        client_attention = ClinetNeedAttentionWidget(setup)
        login.do_login(self.username, self.password)
        client_attention.navigate_to_client_need_attention_widget()
        return client_attention

    def test_01_verify_all_columns_are_displayed(self, setup):
        """Verify that all columns are displayed in the Client Need Attention widget."""
        client_attention = self.open_client_need_attention_widget(setup)
        client_attention.assertion(
            client_attention.get_text(client_attention.GET_ALL_COLUMNS_NAME_XPATH),
            "CLIENT NAME STATUS EXPIRY DATE ACTION")

    def test_02_verify_all_dropdown_values_are_displayed(self, setup):
        """Verify that all filter dropdown values are displayed."""
        client_attention = self.open_client_need_attention_widget(setup)
        client_attention.get_all_drop_down_values()
        client_attention.assertion(
            client_attention.all_dropdown_values,
            ["Document Expiry", "IRPQ Next Review", "Due Diligence Next Review"])

    def test_03_verify_all_due_days_dropdown_values_are_displayed(self, setup):
        """Verify that all Due Days dropdown values are displayed."""
        client_attention = self.open_client_need_attention_widget(setup)
        client_attention.get_all_days_dropdown_values()
        client_attention.assertion(
            client_attention.all_days_dropdown_values,
            ["Expired", "Due in 7 days", "Due in 15 days", "Due in 30 days"])

    def test_04_verify_user_can_download_excel_file(self, setup):
        """Verify that the user can download the Excel file successfully."""
        client_attention = self.open_client_need_attention_widget(setup)
        client_attention.download_excel()
        assert client_attention.downloaded, "Excel file was not downloaded."

    def test_05_verify_user_can_search_client_by_name(self, setup):
        """Verify that the user can search for a client by name."""
        client_attention = self.open_client_need_attention_widget(setup)
        client_attention.search_user_name_in_search_box()
        client_attention.assert_In(client_attention.username,client_attention.all_usernames_in_list)

    def test_06_verify_critical_status_is_displayed_when_expiry_date_is_less_than_today(self, setup):
        """Verify that Critical status is displayed when the expiry date is less than today."""
        client_attention = self.open_client_need_attention_widget(setup)
        client_attention.critical_status_displayed_less_than_today()
        client_attention.assertion(
            client_attention.get_status,
            client_attention.expected_status)

    def test_07_verify_pagination_is_displayed(self, setup):
        """Verify that pagination is displayed in the Client Need Attention widget."""
        client_attention = self.open_client_need_attention_widget(setup)
        client_attention.assertion(
            client_attention.is_displayed(client_attention.PAGINATION_TEXT_DISPLAYED_XPATH),
            True)

    def test_08_verify_take_action_button_navigates_to_onboarding_page(self, setup):
        """Verify that the Take Action button navigates the user to the onboarding page."""
        client_attention = self.open_client_need_attention_widget(setup)
        client_attention.user_navigate_to_onboarding_using_take_action_button()
        client_attention.assertion(
            client_attention.first_name,
            client_attention.get_expected_text)


    def test_09_verify_user_can_select_irpq_next_review_date(self,setup):
        client_attention = self.open_client_need_attention_widget(setup)
        client_attention.select_irpq_review_date()
        client_attention.assertion(client_attention.is_displayed(client_attention.CLICK_ON_IRPQ_NEXT_REVIEW_DATE_XPATH),True)


    def test_10_verify_irpq_next_review_date_match_risk_analysis_form(self,setup):
        client_attention = self.open_client_need_attention_widget(setup)
        client_attention.select_irpq_review_date()
        client_attention.click_on_take_action_and_go_risk_analysis_form()
        client_attention.assertion(client_attention.irpq_expiry_date,client_attention.formatted_date)
