import time

from selenium.webdriver.common.by import By


class RiskProfile:
    """
    This class stores all locators for the Risk Profile form.
    Each constant represents a specific element in the Risk Profile workflow.
    """

    # ======= Navigation / Page Sections =======
    CLICK_ON_RISK_PROFILE_PAGE_XPATH = (By.XPATH, "//*[text()='Risk Analysis']")  # Risk Analysis menu or page link
    CLICK_ON_KNOWLEDGE_AND_EXPERIENCE_XPATH = (By.XPATH, "//*[text()='Knowledge & Experience']")  # Knowledge & Experience section

    # ======= Radio Buttons - Knowledge & Experience =======
    CLICK_ON_YES_RADIO_BUTTONS_XPATH = (
        By.XPATH,
        "//*[text()='Professional Experience']//ancestor::table/tbody/tr/td[2]/input"
    )  # Yes option for Professional Experience

    CLICK_ON_15_RADIO_BUTTONS_XPATH = (
        By.XPATH,
        "//*[text()='Annual Trading Frequency']//ancestor::table/tbody/tr/td[4]/input"
    )  # Option for Annual Trading Frequency (15+ times/year)

    CLICK_ON_1_5_RADIO_BUTTONS_XPATH = (
        By.XPATH,
        "//*[text()='Investment Period']//ancestor::table/tbody/tr/td[8]/input"
    )  # Option for Investment Period (1-5 years)

    CLICK_ON_KNOWLEDGE_RADIO_BUTTONS_XPATH = (
        By.XPATH,
        "//*[text()='Knowledge']//ancestor::table/tbody/tr/td[3]/input"
    )  # Knowledge rating option

    CLICK_ON_TRAINING_RADIO_BUTTONS_XPATH = (
        By.XPATH,
        "//*[text()='Training']//ancestor::table/tbody/tr/td[6]/input"
    )  # Training level option

    CLICK_ON_RISK_ACKNO_RADIO_BUTTONS_XPATH = (
        By.XPATH,
        "//*[text()='Risk Acknowledgement']//ancestor::table/tbody/tr/td[8]/input"
    )  # Risk acknowledgement "Yes" option

    # ======= Client's Investment Profile =======
    CLICK_ON_CLIENT_INVESTMENT_PROFILE_XPATH = (
        By.XPATH,
        "(//*[contains(text(),'Investment Profile')])[1]"
    )  # Expand/click on Investment Profile section

    CLICK_ON_RADIO_BTN_CLIENT_INVESTMENT_PROFILE_XPATH = (
        By.XPATH,
        "(//*[contains(text(),'Investment Profile')])[1]//ancestor::div[1]//child::label//parent::div/div/div[1]"
    )  # Radio button for Investment Profile selection

    # ======= Client Details Form =======
    CLICK_ON_CLEINT_DETAILS_FORM_XPATH = (
        By.XPATH,
        "(//*[contains(text(),'Client Details')])[1]"
    )  # Expand/click on Client Details form section

    CLICK_ON_CLIENT_DETAILS_RADIO_BTN_XAPTH = (
        By.XPATH,
        "//*[contains(text(),'Client Details')]//parent::h3//parent::div/parent::div/div[1]/div[2]//child::label//parent::div/div/div[1]"
    )  # Radio button in Client Details section

    # ======= USD Amount Input =======
    ENTER_USD_AMOUNT_ID = (By.ID, "assetAmount")  # Asset amount input field

    # ======= Leverage Declaration Dropdown =======
    CLICK_ON_RISK_DROP_XPATH = (
        By.XPATH,
        "//div[@id='leverageDeclaration']//button"
    )  # Dropdown for leverage declaration

    SELECT_VALUE_VIA_XPATH = (
        By.XPATH,
        "//*[text()='Other Needs']"
    )  # Dropdown option: Other Needs

    # ======= Evaluate & Confirmation =======
    CLICK_ON_EVALUATE_BUTTON_XPATH = (By.XPATH, "//*[text()='Evaluate']")  # Evaluate button
    CLICK_ON_YES_BUTTON_XPATH = (By.XPATH, "//button[text()='Yes']")  # Yes button for confirmation popup

    # ======= Date Picker =======

    CLICK_ON_CALENDER_XPATH = (By.XPATH, "(//*[text()='Select review date'])[2]")  # Calendar widget open button
    CLICK_ON_DATE_XPATH = (By.XPATH, "//*[text()='13']")  # Select date '13' from calendar
    CLICK_ON_SAVE_BUTTON = (By.XPATH, "(//*[text()='Save'])[2]")  # Save date selection

    # ======= Success Message =======
    VALIDATE_MESSAGE_SHOW_XPATH = (By.XPATH, "//*[text()='Form Submitted Successfully']")  # Final success message
