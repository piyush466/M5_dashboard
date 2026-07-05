import time

import allure
import pytest
from new_pages.client_dashboard_filter import ClientDashboard_Filter
from new_pages.dashboard_page1 import DashboardList
from new_pages.login_page1 import Login
from utilities.configpar import ConfigReader


class Test_ClientDashboard_Filter():

    username = ConfigReader.read_config("tenant42", "username")
    password = ConfigReader.read_config("tenant42", "password")
    client_username = ConfigReader.read_config("client-tenant5", "username")
    client_password = ConfigReader.read_config("client-tenant5", "password")

    @allure.title("Test 01 - User can see all 104 checkbox")
    @pytest.mark.assetFilter
    def test_01_user_can_see_the_all_104_checkboxes(self,setup):
        login = Login(setup)
        client_dashboard = ClientDashboard_Filter(setup)
        login.do_login(self.username, self.password)
        client_dashboard.navigate_client_dashboard()
        client_dashboard.open_asset_filter()
        client_dashboard.assertion(client_dashboard.get_length(client_dashboard.VERIFY_LENGH_OF_CHECK_BOX_XPATH),
                                   104)

    @allure.title("Test 02 - User can create the new filter")
    @pytest.mark.assetFilter
    def test_02_user_can_create_new_filter(self,setup):
        login = Login(setup)
        dashboard = DashboardList(setup)
        client_dashboard = ClientDashboard_Filter(setup)
        login.do_login(self.username, self.password)
        client_dashboard.navigate_client_dashboard()
        client_dashboard.open_asset_filter()
        client_dashboard.create_new_filter(dashboard.fake_name())
        client_dashboard.assertion(client_dashboard.get_text(client_dashboard.VERIFY_SAVED_MESSAGE_DISPLAYED_XPATH),
                                   "Filter saved successfully")

    @allure.title("Test 03 - User can delete the filter")
    @pytest.mark.assetFilter
    def test_03_user_can_delete_filter(self,setup):
        login = Login(setup)
        dashboard = DashboardList(setup)
        client_dashboard = ClientDashboard_Filter(setup)
        name = dashboard.fake_name()
        login.do_login(self.username, self.password)
        client_dashboard.navigate_client_dashboard()
        client_dashboard.open_asset_filter()
        client_dashboard.create_new_filter(name)
        client_dashboard.delete_create_filter(name)
        client_dashboard.assertion(client_dashboard.get_text(client_dashboard.VERIFY_FILTER_DELETE_XPATH),
                                   "Filter deleted successfully")

    @allure.title("Test 04 - user can edit the filter")
    @pytest.mark.assetFilter
    def test_04_user_can_edit_filter(self,setup):
        login = Login(setup)
        dashboard = DashboardList(setup)
        client_dashboard = ClientDashboard_Filter(setup)
        name = dashboard.fake_name()
        login.do_login(self.username, self.password)
        client_dashboard.navigate_client_dashboard()
        client_dashboard.open_asset_filter()
        client_dashboard.create_new_filter(name)
        client_dashboard.update_created_filter(name,dashboard.fake_name())
        client_dashboard.assertion(client_dashboard.get_text(client_dashboard.VERIFY_FILTER_UPDATE_XPATH),
                                   "Filter updated successfully")

    @allure.title("Test 05 - User can do make primary filter")
    @pytest.mark.assetFilter
    def test_05_user_can_make_primary_filter(self,setup):
        login = Login(setup)
        dashboard = DashboardList(setup)
        client_dashboard = ClientDashboard_Filter(setup)
        name = dashboard.fake_name()
        login.do_login(self.username, self.password)
        client_dashboard.navigate_client_dashboard()
        client_dashboard.open_asset_filter()
        client_dashboard.create_new_filter(name)
        client_dashboard.make_primary_filter(name)
        client_dashboard.assertion(client_dashboard.make_primary, True)

    @allure.title("Test 06 - User can make primary for client")
    @pytest.mark.assetFilter
    def test_06_user_can_make_primary_for_client(self,setup):
        login = Login(setup)
        dashboard = DashboardList(setup)
        client_dashboard = ClientDashboard_Filter(setup)
        name = dashboard.fake_name()
        login.do_login(self.username, self.password)
        client_dashboard.navigate_client_dashboard()
        client_dashboard.open_asset_filter()
        client_dashboard.create_new_filter(name)
        client_dashboard.make_primary_for_client(name)
        login.do_login(self.client_username, self.client_password)
        client_dashboard.open_asset_filter()
        client_dashboard.go_to_saved_filter(name)
        client_dashboard.assertion(client_dashboard.element, True)

    @allure.title("test 07 - User remove the multi-asset checkbox and check after remove portfolio value is change or not")
    @pytest.mark.assetFilter
    def test_07_after_update_data_is_change(self,setup):
        login = Login(setup)
        client_dashboard = ClientDashboard_Filter(setup)
        login.do_login(self.username, self.password)
        client_dashboard.navigate_client_dashboard()
        client_dashboard.open_asset_filter()
        client_dashboard.apply_filter_without_multi_asset_investment()
        client_dashboard.assert_not_equal(client_dashboard.portfolio_value,
                                          client_dashboard.after_removed_multi_asset_checkbox)

    @allure.title("Test 05 - User can do make primary filter")
    @pytest.mark.assetFilter2
    def test_05_user_can_make_primary_filter2(self, setup):
        driver, username, password = setup

        login = Login(driver)  # 🔧 FIX 1: Pass only driver instead of full setup tuple
        dashboard = DashboardList(driver)  # 🔧 FIX 1
        client_dashboard = ClientDashboard_Filter(driver)  # 🔧 FIX 1

        name = dashboard.fake_name()

        login.do_login(username, password)
        client_dashboard.navigate_client_dashboard()
        client_dashboard.open_asset_filter()
        client_dashboard.create_new_filter(name)
        client_dashboard.make_primary_filter(name)
        client_dashboard.assertion(client_dashboard.make_primary, True)
