import pytest

from locators.risk_profile_locators import RiskProfile
from new_pages.Individual_onboarding_pages import Individual_Onboarding
from new_pages.dashboard_page1 import DashboardList
from new_pages.login_page1 import Login
from utilities.configpar import ConfigReader


class TestIndividualOnboarding:
    # username = ConfigReader.read_config("tenant5", "username")
    # password = ConfigReader.read_config("tenant5", "password")

    @pytest.mark.BasicDetails
    def test_user_can_fill_basic_details_onboarded_form(self,setup):
        login = Login(setup)
        ind_onboard = Individual_Onboarding(setup)
        login.do_login(self.username, self.password)
        ind_onboard.go_to_the_client_onboarding()
        ind_onboard.fill_basic_detail_form("piyush", "shetty",
                                           "10/02/2025", "24/01/2025", "23/01/2007",
                                           "8411878794", "piyushd@valuefy.com", "SBI Bank")

    @pytest.mark.RiskProfile
    def test_user_can_fill_risk_profile_page(self,setup):
        login = Login(setup)
        ind_onboard = Individual_Onboarding(setup)
        login.do_login(self.username, self.password)
        ind_onboard.go_to_the_client_onboarding()
        ind_onboard.fill_risk_profile_form()
        ind_onboard.assertion(ind_onboard.form_created,
                              "Form Submitted Successfully")


    def test_user_can_fill_other_details_page(self,setup):
        login = Login(setup)
        ind_onboard = Individual_Onboarding(setup)
        login.do_login(self.username, self.password)
        ind_onboard.go_to_the_client_onboarding()
        ind_onboard.fill_other_details_page()

    @pytest.mark.regulatoryDetails
    def test_user_can_fill_regulatory_details(self,setup):
        login = Login(setup)
        ind_onboard = Individual_Onboarding(setup)
        login.do_login(self.username, self.password)
        ind_onboard.go_to_the_client_onboarding()
        ind_onboard.fill_regulatory_details_page()


    def test_fill_all_pages(self,setup):
        login = Login(setup)
        ind_onboard = Individual_Onboarding(setup)
        login.do_login(self.username, self.password)
        ind_onboard.go_to_the_client_onboarding()
        # ind_onboard.fill_basic_detail_form("piyush", "shetty",
        #                                    "10/02/2025", "24/01/2025", "23/01/2007",
        #                                    "8411878794", "piyushd@valuefy.com", "SBI Bank")
        #
        # ind_onboard.fill_other_details_page()
        ind_onboard.fill_risk_profile_form()
        ind_onboard.fill_regulatory_details_page()



    @pytest.mark.parametrize("run", range(200000))  # runs test 100 times
    def test_click_every_five_second(self, setup, run):
        login = Login(setup)
        ind_onboard = Individual_Onboarding(setup)
        login.do_login(self.username, self.password)







