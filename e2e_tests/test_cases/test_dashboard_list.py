import pytest
import allure
from utilities.configpar import ConfigReader
from new_pages.dashboard_page1 import DashboardList
from new_pages.login_page1 import Login
from uihelper.helper_file import UI_Helper
from faker import Faker


class Test_Dashboard_list:
    fake_name = Faker()
    name = fake_name.name()
    username = ConfigReader.read_config("tenant5","username")
    password = ConfigReader.read_config("tenant5","password")


    @allure.title("Test 01 - User can successfully create a new dashboard")
    @pytest.mark.Dashboard2
    def test_01_user_can_create_dashboard(self, setup):
        login = Login(setup)
        dashboard = DashboardList(setup)
        login.do_login(self.username, self.password)
        dashboard.dashboard_creation(self.name, "Testing")
        dashboard.assertion(dashboard.get_text(dashboard.ASSERT_ON_SUCCESFUL_CREATION_DASHBOARD_XPATH),
                            "Dashboard created successfully")
        dashboard.delete_dashboard_part_2(self.name)


    @allure.title("Test 02 - User cannot create dashboard without entering required details")
    @pytest.mark.Dashboard
    def test_02_without_enter_any_detail_user_can_create_dashbard(self, setup):
        login = Login(setup)
        dashboard = DashboardList(setup)
        login.do_login(self.username, self.password)
        dashboard.dashboard_creation_without_input("  ", " ")
        dashboard.assertion(dashboard.get_text(dashboard.ASSERT_FOR_NAME_TEXT_BOX_XPATH), "Name can not be empty")

    @allure.title("Test 03 - User can edit the dashboard name")
    @pytest.mark.Dashboard
    def test_03_user_can_edit_the_dashboard_name(self, setup):
        login = Login(setup)
        dashboard = DashboardList(setup)
        random_name = UI_Helper.random_text()
        name = f"Dashboard{random_name}"
        login.do_login(self.username, self.password)
        dashboard.dashboard_creation(name, "Testing")
        dashboard.add_all_widget_and_save()
        dashboard.edit_dashboard_name("New_dashboard")
        dashboard.assertion(dashboard.get_text(dashboard.VERIFY_NEW_DASHBOARD_NAME_ID), "New_dashboard")
        dashboard.delete_dashboard_part_2(name)

    @allure.title("Test 04 - User can change the currency")
    @pytest.mark.Dashboard
    def test_04_user_can_change_the_currency(self, setup):
        login = Login(setup)
        dashboard = DashboardList(setup)
        login.do_login(self.username, self.password)
        dashboard.dashboard_creation(self.name, "Testing")
        dashboard.add_all_widget_and_save()
        dashboard.set_currency()
        dashboard.assertion(dashboard.get_text(dashboard.CLICK_ON_CURRENCY_DROP_DOWN_CSS), "INR - Indian Rupee")
        dashboard.delete_dashboard_part_2(self.name)

    @allure.title("Test 05 - User can on the toggle")
    @pytest.mark.Dashboard
    def test_05_user_can_on_the_toggle(self,setup):
        login = Login(setup)
        dashboard = DashboardList(setup)
        login.do_login(self.username, self.password)
        dashboard.handle_the_toggle()
        dashboard.assertion(dashboard.toggle, "true")


    @allure.title("Test 06 - Log is generated after dashboard creation")
    def test_06_create_dashboard_log_generate_or_not(self, setup):
        login = Login(setup)
        dashboard = DashboardList(setup)
        fake_name = Faker()
        name = fake_name.name()
        login.do_login(self.username, self.password)
        dashboard.dashboard_creation(name, "Testing")
        dashboard.after_create_dashboard_log_generate_check()
        assert name in dashboard.dasboard_creation_log
        assert name in dashboard.dasboard_visited_log
        dashboard.delete_dashboard(name)

    @allure.title("Test 07 - Add all widgets, save dashboard and verify logs")
    def test_07_after_create_dashboard_add_all_widget_and_save_and_verify_log(self, setup):
        login = Login(setup)
        dashboard = DashboardList(setup)
        fake_name = Faker()
        name = fake_name.name()
        login.do_login(self.username, self.password)
        dashboard.dashboard_creation(name, "Testing")
        dashboard.add_all_widget_and_save_navigate_acitvitylog()
        dashboard.assertion(dashboard.widget_update, "Widget updation")
        dashboard.assertion(dashboard.saved_dashboard, "Dashboard Saved")
        dashboard.delete_dashboard(name)

    @allure.title("Test 08 - Log is generated when navigating to a client dashboard")
    def test_08_check_after_navigate_to_client_dashboard_log_generation(self, setup):
        login = Login(setup)
        dashboard = DashboardList(setup)
        name = "piyush Dravyakar-21_03"
        login.do_login(self.username, self.password)
        dashboard.navigate_to_RM_dashboard_from_client_list(name)
        dashboard.validate_the_log_for_navigation_to_client_dashboard()
        assert name in dashboard.client_navigation

    @allure.title("Test 09 - Check logs after navigating from group list to client dashboard")
    def test_09_check_after_navigate_client_dashboard_from_group_list_logs(self, setup):
        login = Login(setup)
        dashboard = DashboardList(setup)
        login.do_login(self.username, self.password)
        dashboard.navigate_the_log_form_group_list_to_client_dashboard("tes new")
        dashboard.validate_the_log_for_navigation_to_client_dashboard()

    @allure.title("test 10 - User can change the date from date picker")
    @pytest.mark.Dashboard
    def test_10_user_can_change_the_date(self,setup):
        login = Login(setup)
        dashboard = DashboardList(setup)
        login.do_login(self.username, self.password)
        dashboard.dashboard_creation(f"New{self.name}", "Testing")
        dashboard.add_all_widget_and_save()
        dashboard.enter_date_in_calender("03/03/2016","29/06/2025")
        text = dashboard.get_text(dashboard.VERIFY_DATE_PERIOD_CSS)
        assert "2016" in text and "2025" in text, f"Expected '2016' and '2025' in text, but got: {text}"
        dashboard.delete_dashboard_part_2(f"New{self.name}")

    @allure.title("test 11 - user can change the theme")
    @pytest.mark.Dashboard
    def test_11_user_can_change_theme(self,setup):
        login = Login(setup)
        dashboard = DashboardList(setup)
        login.do_login(self.username, self.password)
        dashboard.change_the_theme()
        print(dashboard.is_displayed(dashboard.VERIFY_THEME_XPATH))
        dashboard.assertion(dashboard.is_displayed(dashboard.VERIFY_THEME_XPATH), True)







