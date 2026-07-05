import json

with open("//test_data/individual_onbaording_data.json", 'r') as file:
    test_data = json.load(file)

with open("//test_data/Individual_onboarding_data/related_member_form_data.json", "r") as file:
    related_member_data = json.load(file)

with open("//test_data/Corporate_onboarding_data/corporate_basic_details_form_data.json", "r") as file:
    corporate_basic_details_data = json.load(file)

