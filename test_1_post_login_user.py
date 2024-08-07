import requests
import pytest
import allure



@pytest.mark.smoke
@pytest.mark.regression
@allure.suite("User Authentication")
@allure.feature("Reqres Feature")
@allure.title("Login user successfully")
@allure.description("This test logs in a user with valid credentials and checks for a successful response.")
@allure.severity('BLOCKER')
def test_post_login_user():
    with allure.step("Define user data and headers"):
        body = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
            }
        headers = {'Content-Type': 'application/json'}

    with allure.step("Send POST request to login user"):
        response = requests.post("https://reqres.in/api/login",
                             headers=headers,
                             json=body)

    with allure.step("Verify response status code is 200"):
        assert response.status_code == 200, f"Request failed with status code {response.status_code}"

    with allure.step("Verify response contains a valid token"):
        response_data = response.json()
        assert len(response_data.get('token', "None")) > 0, 'Token length is 0'
        assert "token" in response_data, "Response does not contain 'token'"

    with allure.step('Printing response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)




    print(response_data)

@pytest.mark.smoke
@pytest.mark.regression
@allure.suite("User Authentication")
@allure.feature("Reqres Feature")
@allure.title("Login user with missing fields")
@allure.description("This test attempts to log in a user with a missing password and expects a 400 error response.")
@allure.severity('NORMAL')

def test_negative_post_login_user():
    with allure.step("Define user data and headers with missing password"):
        body = {
                "email": "peter@klaven"
            }
        headers = {'Content-Type': 'application/json'}

    with allure.step("Send POST request to login user with invalid data"):
        response = requests.post("https://reqres.in/api/login",
                                 headers=headers,
                                 json=body)

    with allure.step("Verify response status code is 400"):
        assert response.status_code == 400, f"Request failed with status code {response.status_code}"



