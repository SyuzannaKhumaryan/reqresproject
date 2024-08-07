import requests
import pytest
import allure



@pytest.mark.regression
@allure.suite("Get User by ID")
@allure.feature("Reqres Feature")
@allure.severity("NORMAL")
@allure.title("Test retrieving user by ID")
@allure.description("This test retrieves a user by ID and verifies the response.")
def test_get_user_by_id():
    with allure.step("Step 1: Send GET request to retrieve user by ID 2"):
        response = requests.get("https://reqres.in/api/users/2")

    with allure.step("Step 2: Verify the response status code is 200"):
        assert response.status_code == 200, f"Request failed with status code {response.status_code}"

    with allure.step("Step 3: Verify the response JSON body is not empty"):
        assert len(response.json()) > 0, "The list shouldn't be empty"

    with allure.step("Step 4: Parse the response JSON data"):
        response_data = response.json()

    with allure.step("Step 5: Verify the presence of 'data' key in response"):
        assert 'data' in response_data, "Data key not found in response"

    with allure.step("Step 6: Verify the presence of 'id' key in data object"):
        assert 'id' in response_data['data'], "Id key not found in data object"

    with allure.step("Step 7: Verify the 'id' value in data object is 2"):
        assert response_data['data']['id'] == 2, f"Expected user ID 2, but got {response_data['data'].get('id', None)}"

    with allure.step("Step 8: Verify the presence of 'email' key in data object"):
        assert 'email' in response_data['data'], "Email key not found in data object"

    with allure.step("Step 9: Verify the 'email' value in data object is a string"):
        assert isinstance(response_data['data']['email'], str), "Expected email to be a string"

    with allure.step("Step 10: Verify the presence of 'first_name' key in data object"):
        assert 'first_name' in response_data['data'], "First_name key not found in data object"

    with allure.step("Step 11: Verify the 'first_name' value in data object is a string"):
        assert isinstance(response_data['data']['first_name'], str), "Expected first_name to be a string"

    with allure.step("Step 12: Verify the presence of 'last_name' key in data object"):
        assert 'last_name' in response_data['data'], "Last_name key not found in data object"

    with allure.step("Step 13: Verify the 'last_name' value in data object is a string"):
        assert isinstance(response_data['data']['last_name'], str), "Expected last_name to be a string"

    with allure.step("Step 14: Verify the presence of 'avatar' key in data object"):
        assert 'avatar' in response_data['data'], "Avatar key not found in data object"

    with allure.step("Step 15: Verify the 'avatar' value in data object is a string"):
        assert isinstance(response_data['data']['avatar'], str), "Expected avatar to be a string"

    with allure.step("Step 16: Verify the presence of 'support' key in response"):
        assert 'support' in response_data, "Support key not found in response"

    with allure.step("Step 17: Verify the presence of 'url' key in support object"):
        assert 'url' in response_data['support'], "Url key not found in support object"

    with allure.step("Step 18: Verify the 'url' value in support object is a string"):
        assert isinstance(response_data['support']['url'], str), "Expected url in support to be a string"

    with allure.step("Step 19: Verify the presence of 'text' key in support object"):
        assert 'text' in response_data['support'], "Text key not found in support object"

    with allure.step("Step 20: Verify the 'text' value in support object is a string"):
        assert isinstance(response_data['support']['text'], str), "Expected text in support to be a string"

    with allure.step('Printing response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)


@pytest.mark.regression
@allure.suite("Get User by ID")
@allure.feature("Reqres Feature")
@allure.severity("NORMAL")
@allure.title("Test retrieving user by invalid ID")
@allure.description("This test retrieves a user by an invalid ID and verifies the response.")
def test_negative_get_user_by_id():
    with allure.step("Step 1: Send GET request to retrieve user by invalid ID 606"):
        response = requests.get("https://reqres.in/api/users/606")

    with allure.step("Step 2: Verify the response status code is 404"):
        assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"
