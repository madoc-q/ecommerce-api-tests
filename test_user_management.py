import requests
import pytest

BASE_URL = "https://reqres.in/api"


class TestCreateUser:
    """Tests for creating new users."""

    def test_create_user_returns_201(self, base_url, headers):
        """Verify that creating a user returns 201 Created."""
        payload = {"name": "Madoc Quaye", "job": "QA Engineer"}
        response = requests.post(f"{base_url}/users", json=payload, headers=headers)
        assert response.status_code == 201, f"Expected 201 but got {response.status_code}"

    def test_create_user_returns_id(self, base_url, headers):
        """Verify that a new user is assigned an ID."""
        payload = {"name": "Madoc Quaye", "job": "QA Engineer"}
        response = requests.post(f"{base_url}/users", json=payload, headers=headers)
        assert "id" in response.json(), "Expected 'id' in response"

    def test_create_user_returns_correct_name(self, base_url, headers):
        """Verify that the created user has the correct name."""
        payload = {"name": "Madoc Quaye", "job": "QA Engineer"}
        response = requests.post(f"{base_url}/users", json=payload, headers=headers)
        assert response.json()["name"] == "Madoc Quaye", "Name in response does not match request"

    def test_create_user_returns_correct_job(self, base_url, headers):
        """Verify that the created user has the correct job title."""
        payload = {"name": "Madoc Quaye", "job": "QA Engineer"}
        response = requests.post(f"{base_url}/users", json=payload, headers=headers)
        assert response.json()["job"] == "QA Engineer", "Job in response does not match request"

    def test_create_user_returns_timestamp(self, base_url, headers):
        """Verify that the response includes a creation timestamp."""
        payload = {"name": "Madoc Quaye", "job": "QA Engineer"}
        response = requests.post(f"{base_url}/users", json=payload, headers=headers)
        assert "createdAt" in response.json(), "Expected 'createdAt' timestamp in response"

    def test_create_user_with_missing_fields(self, base_url, headers):
        """Verify API behavior when required fields are missing."""
        payload = {}
        response = requests.post(f"{base_url}/users", json=payload, headers=headers)
        # Reqres accepts empty payload — this documents that behavior
        assert response.status_code in [200, 201, 400], f"Unexpected status code: {response.status_code}"


class TestUpdateUser:
    """Tests for updating existing users."""

    def test_update_user_returns_200(self, base_url, headers):
        """Verify that updating a user returns 200."""
        payload = {"name": "Madoc Quaye", "job": "Senior QA Engineer"}
        response = requests.put(f"{base_url}/users/2", json=payload, headers=headers)
        assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

    def test_update_user_returns_updated_job(self, base_url, headers):
        """Verify that the response reflects the updated job title."""
        payload = {"name": "Madoc Quaye", "job": "Senior QA Engineer"}
        response = requests.put(f"{base_url}/users/2", json=payload, headers=headers)
        assert response.json()["job"] == "Senior QA Engineer", "Job was not updated correctly"

    def test_update_user_returns_timestamp(self, base_url, headers):
        """Verify that the response includes an updated timestamp."""
        payload = {"name": "Madoc Quaye", "job": "Senior QA Engineer"}
        response = requests.put(f"{base_url}/users/2", json=payload, headers=headers)
        assert "updatedAt" in response.json(), "Expected 'updatedAt' timestamp in response"

    def test_partial_update_user_returns_200(self, base_url, headers):
        """Verify that a partial update using PATCH returns 200."""
        payload = {"job": "Lead QA Engineer"}
        response = requests.patch(f"{base_url}/users/2", json=payload, headers=headers)
        assert response.status_code == 200, f"Expected 200 but got {response.status_code}"


class TestDeleteUser:
    """Tests for deleting users."""

    def test_delete_user_returns_204(self, base_url, headers):
        """Verify that deleting a user returns 204 No Content."""
        response = requests.delete(f"{base_url}/users/2", headers=headers)
        assert response.status_code == 204, f"Expected 204 but got {response.status_code}"

    def test_delete_user_returns_empty_body(self, base_url, headers):
        """Verify that a successful delete returns an empty response body."""
        response = requests.delete(f"{base_url}/users/2", headers=headers)
        assert response.text == "", "Expected empty response body after delete"
