import requests
import pytest
import allure

@pytest.mark.smoke
@pytest.mark.regression
@allure.suite("Delete User")
@allure.feature("Reqres Feature")
@allure.severity("CRITICAL")
@allure.title("Test deleting user by ID")
@allure.description("This test deletes a user by ID and verifies the response status code.")
def test_delete_user():
    headers = {"Content-Type": "application/json"}

    with allure.step("Step 1: Send DELETE request to delete user with ID 2"):
        response = requests.delete("https://reqres.in/api/users/2",
                                   headers=headers)

    with allure.step("Step 2: Verify the response status code is 204"):
        assert response.status_code == 204, f"Expected status code 204, but got {response.status_code}"

    with allure.step("Step 3: Print deletion confirmation"):
        print("User deleted successfully.")


