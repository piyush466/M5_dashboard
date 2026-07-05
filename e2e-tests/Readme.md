For allure result:: python3 -m pytest -v -s ./test_cases/test_2fa_page.py --alluredir=allure-result
allure serve allure-result

For html report:: python3 -m pytest -v -s ./test_cases/test_2fa_page.py --html=reports/test_case_2fa.html

Running individual test cases:: python3 -m pytest -v -s ./test_cases/test_2fa_page.py





