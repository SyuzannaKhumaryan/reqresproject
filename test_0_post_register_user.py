import requests
import pytest
import allure

@pytest.mark.smoke
@pytest.mark.regression
@allure.suite("User Registration")
@allure.feature("Reqres Feature")
@allure.title("Register user successfully")
@allure.description("This test registers a user with valid credentials and checks for a successful response.")
@allure.severity('BLOCKER')
def test_post_register_user():
    with allure.step("Define user data and headers"):
        body = {
                "email": "eve.holt@reqres.in",
                "password": "pistol"
            }
        headers = {'Content-Type': 'application/json'}

    with allure.step("Send POST request to register user"):
        response = requests.post("https://reqres.in/api/register",
                                     headers=headers,
                                     json=body)

    with allure.step("Verify response status code is 200"):
        assert response.status_code == 200, f"Request failed with status code {response.status_code}"

    response_data = response.json()
    with allure.step("Verify response contains a valid token"):
        assert len(response_data.get('token', 'None')) > 0, 'Token length is 0'
    with allure.step("Verify response contains 'id'"):
        assert "id" in response_data, "Response does not contain 'id'"

    with allure.step("Verify response contains 'token'"):
        assert "token" in response_data, "Response does not contain 'token'"



@pytest.mark.smoke
@pytest.mark.regression
@allure.suite("User Registration")
@allure.feature("Reqres Feature")
@allure.title("Register user with missing fields")
@allure.description("This test attempts to register a user with missing password and expects a 400 error response.")
@allure.severity('BLOCKER')
def test_negative_post_register_user():
    with allure.step("Define user data and headers with missing password"):
        body = {
                "email": "sydney@fife"
            }
        headers = {'Content-Type': 'application/json'}

    with allure.step("Send POST request to register user with invalid data"):
        response = requests.post("https://reqres.in/api/register",
                                headers=headers,
                                json=body)

    with allure.step("Verify response status code is 400"):
        assert response.status_code == 400, f"Request failed with status code {response.status_code}"

