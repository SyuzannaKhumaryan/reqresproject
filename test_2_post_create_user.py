import requests
import pytest
import allure

@pytest.mark.smoke
@pytest.mark.regression
@allure.suite("User Creation")
@allure.feature("Reqres Feature")
@allure.severity("CRITICAL")
@allure.title("Test creating a new user")
@allure.description("This test creates a new user with a name and job, then verifies the response.")
def test_create_user():
    body = {
        "name": "morpheus",
        "job": "leader"
    }
    headers = {"Content-Type": "application/json"}

    with allure.step("Step 1: Send POST request to create a new user"):
        response = requests.post("https://reqres.in/api/users",
                                 json=body,
                                 headers=headers)

    with allure.step("Step 2: Check response status code"):
        assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"

    with allure.step("Step 3: Parse response data"):
        response_data = response.json()

    with allure.step("Step 4: Verify the presence of 'name' in the response"):
        assert 'name' in response_data, "Name key not found in response"

    with allure.step("Step 5: Verify the 'name' field is a string"):
        assert isinstance(response_data['name'], str), "Expected name to be a string"

    with allure.step("Step 6: Verify the 'name' field matches the request"):
        assert response_data['name'] == body['name'], f"Expected name {body['name']}, but got {response_data.get('name', 'None')}"

    with allure.step("Step 7: Verify the presence of 'job' in the response"):
        assert 'job' in response_data, "Job key not found in response"

    with allure.step("Step 8: Verify the 'job' field is a string"):
        assert isinstance(response_data['job'], str), "Expected job to be a string"

    with allure.step("Step 9: Verify the 'job' field matches the request"):
        assert response_data['job'] == body['job'], f"Expected job {body['job']}, but got {response_data.get('job', 'None')}"

    with allure.step("Step 10: Verify the presence of 'id' in the response"):
        assert 'id' in response_data, "Id key not found in response"

    with allure.step("Step 11: Verify the 'id' field is a string"):
        assert isinstance(response_data['id'], str), "Expected id to be a string"

    with allure.step("Step 12: Verify the presence of 'createdAt' in the response"):
        assert 'createdAt' in response_data, "CreatedAt key not found in response"

    with allure.step("Step 13: Print success message with user ID and created timestamp"):
        print("User created successfully.")
        print(f"User ID: {response_data['id']}")
        print(f"Created At: {response_data['createdAt']}")

