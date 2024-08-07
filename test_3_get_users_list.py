import requests
import pytest
import allure


@pytest.mark.regression
@allure.suite("Get Users List")
@allure.feature("Reqres Feature")
@allure.severity("CRITICAL")
@allure.title("Test getting users list")
@allure.description("This test retrieves the list of users from the API and verifies the response.")
def test_get_users_list():
    with allure.step("Step 1: Send GET request to retrieve users list"):
        response = requests.get("https://reqres.in/api/users?page=2")

    with allure.step("Step 2: Check response status code"):
        assert response.status_code == 200, f"Request failed with status code {response.status_code}"

    with allure.step("Step 3: Verify the response body is not empty"):
        assert len(response.json()) > 0, "The list shouldn't be empty"


