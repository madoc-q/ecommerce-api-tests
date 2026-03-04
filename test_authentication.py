import requests
import pytest

BASE_URL = "https://reqres.in/api"


class TestAuthentication:
    """Tests for user authentication flows."""

    def test_successful_login_returns_200(self, base_url, headers):
        """Verify that valid credentials return a successful response."""
        payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
        response = requests.post(f"{base_url}/login", json=payload, headers=headers)
        assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

    def test_successful_login_returns_token(self, base_url, headers):
        """Verify that a valid login returns an authentication token."""
        payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
        response = requests.post(f"{base_url}/login", json=payload, headers=headers)
        assert "token" in response.json(), "Expected token in login response"
        assert len(response.json()["token"]) > 0, "Token should not be empty"

    def test_login_missing_password_returns_400(self, base_url, headers):
        """Verify that login without a password returns 400."""
        payload = {"email": "eve.holt@reqres.in"}
        response = requests.post(f"{base_url}/login", json=payload, headers=headers)
        assert response.status_code == 400, f"Expected 400 but got {response.status_code}"

    def test_login_missing_password_returns_error_message(self, base_url, headers):
        """Verify that a missing password returns a descriptive error message."""
        payload = {"email": "eve.holt@reqres.in"}
        response = requests.post(f"{base_url}/login", json=payload, headers=headers)
        assert "error" in response.json(), "Expected error message in response"

    def test_login_missing_email_returns_400(self, base_url, headers):
        """Verify that login without an email returns 400."""
        payload = {"password": "cityslicka"}
        response = requests.post(f"{base_url}/login", json=payload, headers=headers)
        assert response.status_code == 400, f"Expected 400 but got {response.status_code}"

    def test_successful_registration_returns_200(self, base_url, headers):
        """Verify that valid registration credentials return a successful response."""
        payload = {"email": "eve.holt@reqres.in", "password": "pistol"}
        response = requests.post(f"{base_url}/register", json=payload, headers=headers)
        assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

    def test_successful_registration_returns_token(self, base_url, headers):
        """Verify that a successful registration returns a token."""
        payload = {"email": "eve.holt@reqres.in", "password": "pistol"}
        response = requests.post(f"{base_url}/register", json=payload, headers=headers)
        assert "token" in response.json(), "Expected token in registration response"

    def test_registration_missing_password_returns_400(self, base_url, headers):
        """Verify that registration without a password returns 400."""
        payload = {"email": "eve.holt@reqres.in"}
        response = requests.post(f"{base_url}/register", json=payload, headers=headers)
        assert response.status_code == 400, f"Expected 400 but got {response.status_code}"

    def test_registration_undefined_user_returns_400(self, base_url, headers):
        """Verify that registering an undefined user returns 400."""
        payload = {"email": "madoc@test.com", "password": "password123"}
        response = requests.post(f"{base_url}/register", json=payload, headers=headers)
        assert response.status_code == 400, f"Expected 400 but got {response.status_code}"
