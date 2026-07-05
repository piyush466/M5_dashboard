from selenium.webdriver.common.by import By


class RelatedMembersLocators:

    CLICK_ON_RELATED_MEMBER_PAGE_XPATH = (
        By.XPATH, "//span[text()='Related Members']"
    )

    CLICK_ON_ADD_ANOTHER_BUTTON_XPATH = (
        By.XPATH, "//*[text()='Add Another']"
    )

    CLICK_ON_NO_RADIO_BUTTON_XPATH = (
        By.XPATH, "//*[text()='No']"
    )

    CLICK_ON_SELECT_MEMEBER_TYPE_DROPDOWN_XPATH = (
        By.XPATH, "//*[text()='Select Member Type']"
    )

    SELECT_INDIVIDUAL_FROM_MEMBER_TYPE_DROPDOWN_XPATH = (
        By.XPATH, "//*[text()='Individual']"
    )

    CLICK_ON_CONFOIM_BUTTOM_XPATH = (
        By.XPATH, "//*[text()='Confirm']"
    )

    CLICK_ON_MARITAL_STATUS_DROPDOWN_XPATH = (
        By.XPATH, "//div[@id='relatedMembers-0-maritalStatus']//button"
    )

    SELECT_VALUE_FROM_MARITAL_STATUS_DROPDOWN_XPATH = (
        By.XPATH, "//*[text()='Single']"
    )

    CLICK_ON_RELATION_DROPDOWN_XPATH = (
        By.XPATH, "//div[@id='relatedMembers-0-relation']"
    )

    SELECT_VALUE_FROM_RELATION_STATUS_DROPDOWN_XPATH = (
        By.XPATH, "//*[text()='Child']"
    )

    CLICK_ON_TITLE_DROPDOWN_XPATH = (
        By.XPATH, "//div[@id='relatedMembers-0-title']"
    )

    SELECT_VALUE_FROM_TITLE_STATUS_DROPDOWN_XPATH = (
        By.XPATH, "//*[text()='Mr']"
    )

    ENTER_FIRST_NAME_XPATH = (
        By.XPATH, "//input[@id='relatedMembers-0-firstName']"
    )

    ENTER_LAST_NAME_XPATH = (
        By.XPATH, "//input[@id='relatedMembers-0-lastName']"
    )

    CLICK_ON_DATE_OF_BIRTH_XPATH = (
        By.XPATH, "//div[@id='relatedMembers-0-primaryIdDateOfBirth']//button"
    )

    ENTER_DATE_OF_BIRTH_XPATH = (
        By.XPATH, "//input[@placeholder='Select date']"
    )

    CLICK_ON_NATIONAL_ID_RADIO_BUTTON_XPATH = (
        By.XPATH, "//*[text()='National ID']"
    )

