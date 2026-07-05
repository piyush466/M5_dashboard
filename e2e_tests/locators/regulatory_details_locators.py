from selenium.webdriver.common.by import By


class RegulatoryDetails:

    CLICK_ON_REGULATORY_DETAILS_PAGE_XPATH = (By.XPATH, "//*[contains(text(),'Regulatory Details')]")
    CLICK_ON_NO_RADIO_BUTTON_XPATH = (By.XPATH, "//button[@role='radio']//parent::div/label[text()='No']")

    CLICK_ON_PEP_DROP_DOWN_XPATH = (By.XPATH, "//div[@id='pepMeans']//button")
    SELECT_SENIOR_PUBLIC_FIGURE_XPATH = (By.XPATH,
                    "//*[contains(text(),'The client currently holds the position of Senior Public Figure')]")

    CLICK_ON_APPLICABLE_CLIENT_XPATH = (By.XPATH, "//div[@id='usPersonStatus']//button")
    SELECT_APPLICABLE_CLIENT_XPATH = (By.XPATH,
            "//*[contains(text(),'Account holder/Controlling person is not a U.S. citizen or resident in the U.S. for tax purposes.')]")

    ENTER_TEXTAREA_DETAILS_XPATH = (By.XPATH, "//textarea[@id='regulatoryAdditionalDetails']")

    CLICK_ON_CLIENT_CLASSIFICATION_XPATH = (By.XPATH, "//div[@id='clientClassification']//button")
    SELECT_CLIENT_CLASSIFICATION_XPATH = (By.XPATH,
                "//*[contains(text(),'Client meets the Assessed Professional Client criteria as per the completed Client Classification Form')]")

    CLICK_ON_CLASSIFICATION2_XPATH = (By.XPATH, "//div[@id='clientClassification-v']//button")
    SELECT_PROFESSIONAL_CLIENT_XPATH = (By.XPATH, "(//*[contains(text(),'Assessed Professional Client')])[2]")

    CLICK_ON_CHECKBOX_XPATH = (By.XPATH, "//div[@id='assessedProfessionalOptions']//button")

    CLICK_ON_APPLICABLE_EXPERIENCE_XPATH = (By.XPATH, "//div[@id='assessedProfessionalExperience']//button")
    SELECT_VALUE_FROM_APPLICABLE_DROP_DOWN = (By.XPATH ,
                    "(//*[contains(text(),'Has sufficient financial experience and understanding of relevant financial markets, products or transactions and any associated risks')])")

    CLICK_ON_APPLICABLE_EXPERIENCE2_XPATH = (By.XPATH, "//div[@id='assessedProfessionalMultiselect']//button")
    SELECT_VALUE_FROM_APPLICABLE_DROP_DOWN2_XPATH = (By.XPATH,
                                "//*[contains(text(),'Has at least USD 1,000,000 in net assets 1 and provided Quantum Partners (DIFC) Limited with sufficient proof thereof')]")

    CLICK_ON_UNDERTAKING_DROP_DOWN_XPATH = (By.XPATH, "//div[@id='undertakingOption']//button")
    SELECT_VALUE_FORM_UNDERTAKING_DROP_DOWM_XPATH = (By.XPATH,
                                "//*[contains(text(),'Has own funds  or called up capital of at least USD 1,000,000 and has provided Quantum Partners (DIFC) Limited with sufficient proof thereof')]")

    CLICK_ON_UNDERTAKING_DROP_DOWN2_XPATH = (By.XPATH, "//div[@id='controllerOption']//button")
    SELECT_VALUE_FROM_UNDERTAKING_DROP_DOWN2_XPATH = (By.XPATH,
                                "//*[contains(text(),'Has sufficient financial experience and understanding of relevant financial markets, products or transac􏰀ons and any associated risks')]")


    CLICK_ON_SELECT_APPLICABLE_DROP_DOWN_XPATH = (By.XPATH, "//div[@id='assessedProfessionalController']//button")
    SELECT_VALUE_FROM_APPLICABLE_DROP_DOWN_XPATH = (By.XPATH, "//*[text()='Holding Company,']")

    SEND_FOREIGN_TAX_NUMBER_XPATH = (By.XPATH, "//input[@id='foreignTaxIdentifyingNumber']")

    CLICK_ON_CHECKBOX_FTIN_XPATH = (By.XPATH, "//button[@id='checkIfFTINNotLegallyRequired']")

    SEND_REF_NUMBER_XPATH = (By.XPATH, "//input[@id='referenceNumbers']")

    FILE_UPLOAD_XPATH = (By.XPATH, "//label[@for='taxDeclaration-upload']")