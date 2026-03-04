import requests
import pytest

BASE_URL = "https://reqres.in/api"


class TestGetUsers:
    """Tests for retrieving user data."""

    def test_get_all_users_returns_200(self, base_url, headers):
        """Verify that the users list endpoint returns a successful response."""
        response = requests.get(f"{base_url}/users?page=1", headers=headers)
        assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

    def test_get_all_users_returns_data(self, base_url, headers):
        """Verify that the users list contains data."""
        response = requests.get(f"{base_url}/users?page=1", headers=headers)
        data = response.json().get("data", [])
        assert len(data) > 0, "Expected users list to be non-empty"

    def test_get_all_users_has_pagination(self, base_url, headers):
        """Verify that pagination fields exist in the response."""
        response = requests.get(f"{base_url}/users?page=1", headers=headers)
        body = response.json()
        assert "page" in body, "Expected 'page' field in response"
        assert "total" in body, "Expected 'total' field in response"
        assert "per_page" in body, "Expected 'per_page' field in response"

    def test_get_single_user_returns_200(self, base_url, headers):
        """Verify that fetching a specific user returns a successful response."""
        response = requests.get(f"{base_url}/users/2", headers=headers)
        assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

    def test_get_single_user_returns_correct_id(self, base_url, headers):
        """Verify that the correct user is returned when fetched by ID."""
        response = requests.get(f"{base_url}/users/2", headers=headers)
        user = response.json()["data"]
        assert user["id"] == 2, f"Expected user ID 2 but got {user['id']}"

    def test_get_single_user_has_required_fields(self, base_url, headers):
        """Verify that a user object contains all required fields."""
        response = requests.get(f"{base_url}/users/2", headers=headers)
        user = response.json()["data"]
        assert "id" in user, "Missing field: id"
        assert "email" in user, "Missing field: email"
        assert "first_name" in user, "Missing field: first_name"
        assert "last_name" in user, "Missing field: last_name"

    def test_get_nonexistent_user_returns_404(self, base_url, headers):
        """Verify that requesting a non-existent user returns 404."""
        response = requests.get(f"{base_url}/users/9999", headers=headers)
        assert response.status_code == 404, f"Expected 404 but got {response.status_code}"

    def test_page_2_returns_different_users(self, base_url, headers):
        """Verify that page 2 returns different users than page 1."""
        page1 = requests.get(f"{base_url}/users?page=1", headers=headers).json()["data"]
        page2 = requests.get(f"{base_url}/users?page=2", headers=headers).json()["data"]
        page1_ids = [u["id"] for u in page1]
        page2_ids = [u["id"] for u in page2]
        assert page1_ids != page2_ids, "Expected different users on page 1 and page 2"
