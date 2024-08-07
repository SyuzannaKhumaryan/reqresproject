import requests
import pytest
import allure

@pytest.mark.regression
@allure.suite("Update User")
@allure.feature("Reqres Feature")
@allure.severity("CRITICAL")
@allure.title("Test updating user details")
@allure.description("This test updates a user by ID and verifies the response.")
def test_update_user():
    body = {
        "name": "morpheus",
        "job": "zion resident"
    }
    headers = {"Content-Type": "application/json"}

    with allure.step("Step 1: Send PUT request to update user with ID 2"):
        response = requests.put("https://reqres.in/api/users/2",
                                json=body,
                                headers=headers)

    with allure.step("Step 2: Verify the response status code is 200"):
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    with allure.step("Step 3: Parse the response JSON data"):
        response_data = response.json()

    with allure.step("Step 4: Verify the presence of 'name' key in response"):
        assert 'name' in response_data, "Name key not found in response"

    with allure.step("Step 5: Verify the 'name' value in response is a string"):
        assert isinstance(response_data['name'], str), "Expected name to be a string"

    with allure.step("Step 6: Verify the 'name' value in response matches the request body"):
        assert response_data['name'] == body['name'], f"Expected name {body['name']}, but got {response_data.get('name', 'None')}"

    with allure.step("Step 7: Verify the presence of 'job' key in response"):
        assert 'job' in response_data, "Job key not found in response"

    with allure.step("Step 8: Verify the 'job' value in response is a string"):
        assert isinstance(response_data['job'], str), "Expected job to be a string"

    with allure.step("Step 9: Verify the 'job' value in response matches the request body"):
        assert response_data['job'] == body['job'], f"Expected job {body['job']}, but got {response_data.get('job', 'None')}"

    with allure.step("Step 10: Verify the presence of 'updatedAt' key in response"):
        assert 'updatedAt' in response_data, "updatedAt key not found in response"

    with allure.step("Step 11: Verify the 'updatedAt' value in response is a string"):
        assert isinstance(response_data['updatedAt'], str), "Expected updatedAt to be a string"

    with allure.step("Step 12: Print update confirmation and updated timestamp"):
        print("User updated successfully.")
        print(f"Updated At: {response_data['updatedAt']}")
