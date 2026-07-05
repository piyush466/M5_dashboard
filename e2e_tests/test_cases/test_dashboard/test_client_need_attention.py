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

    def test_01_verify_all_columns_are_displayed(self, setup):
        """Verify that all columns are displayed in the Client Need Attention widget."""
        login = Login(setup)
        dashboard = DashboardList(setup)
        clinetAttention = ClinetNeedAttentionWidget(setup)
        login.do_login(self.username, self.password)
        clinetAttention.navigate_to_client_need_attention_widget()
        dashboard.assertion(
            dashboard.get_text(clinetAttention.GET_ALL_COLUMNS_NAME_XPATH),
            "CLIENT NAME STATUS EXPIRY DATE ACTION"
        )

    def test_02_verify_all_dropdown_values_are_displayed(self, setup):
        """Verify that all filter dropdown values are displayed."""
        login = Login(setup)
        dashboard = DashboardList(setup)
        clinetAttention = ClinetNeedAttentionWidget(setup)
        login.do_login(self.username, self.password)
        clinetAttention.navigate_to_client_need_attention_widget()
        clinetAttention.get_all_drop_down_values()
        clinetAttention.assertion(
            clinetAttention.all_dropdown_values,
            ["Document Expiry", "IRPQ Next Review", "Due Diligence Next Review"]
        )

    def test_03_verify_all_due_days_dropdown_values_are_displayed(self, setup):
        """Verify that all Due Days dropdown values are displayed."""
        login = Login(setup)
        clinetAttention = ClinetNeedAttentionWidget(setup)
        login.do_login(self.username, self.password)
        clinetAttention.navigate_to_client_need_attention_widget()
        clinetAttention.get_all_days_dropdown_values()
        clinetAttention.assertion(
            clinetAttention.all_days_dropdown_values,
            ["Expired", "Due in 7 days", "Due in 15 days", "Due in 30 days"]
        )

    def test_04_verify_user_can_download_excel_file(self, setup):
        """Verify that the user can download the Excel file successfully."""
        login = Login(setup)
        clinetAttention = ClinetNeedAttentionWidget(setup)
        login.do_login(self.username, self.password)
        clinetAttention.navigate_to_client_need_attention_widget()
        clinetAttention.download_excel()
        assert clinetAttention.downloaded, "Excel file was not downloaded."

    def test_05_verify_user_can_search_client_by_name(self, setup):
        """Verify that the user can search for a client by name."""
        login = Login(setup)
        clinetAttention = ClinetNeedAttentionWidget(setup)
        login.do_login(self.username, self.password)
        clinetAttention.navigate_to_client_need_attention_widget()
        clinetAttention.search_user_name_in_search_box()

    def test_06_verify_critical_status_is_displayed_when_expiry_date_is_less_than_today(self, setup):
        """Verify that Critical status is displayed when the expiry date is less than today."""
        login = Login(setup)
        clinetAttention = ClinetNeedAttentionWidget(setup)
        login.do_login(self.username, self.password)
        clinetAttention.navigate_to_client_need_attention_widget()
        clinetAttention.critical_status_displayed_less_than_today()
        clinetAttention.assertion(
            clinetAttention.get_status,
            clinetAttention.expected_status
        )

    def test_07_verify_pagination_is_displayed(self, setup):
        """Verify that pagination is displayed in the Client Need Attention widget."""
        login = Login(setup)
        clinetAttention = ClinetNeedAttentionWidget(setup)
        login.do_login(self.username, self.password)
        clinetAttention.navigate_to_client_need_attention_widget()
        clinetAttention.assertion(
            clinetAttention.is_displayed(clinetAttention.PAGINATION_TEXT_DISPLAYED_XPATH),
            True
        )

    def test_08_verify_take_action_button_navigates_to_onboarding_page(self, setup):
        """Verify that the Take Action button navigates the user to the onboarding page."""
        login = Login(setup)
        clinetAttention = ClinetNeedAttentionWidget(setup)
        login.do_login(self.username, self.password)
        clinetAttention.navigate_to_client_need_attention_widget()
        clinetAttention.user_navigate_to_onboarding_using_take_action_button()
        clinetAttention.assertion(
            clinetAttention.first_name,
            clinetAttention.get_expected_text
        )