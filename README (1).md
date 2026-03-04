# E-Commerce API Test Suite

A professional API test suite built with Python and Pytest, testing a RESTful user management API that simulates a real e-commerce platform. This project covers authentication flows, user management, and edge case handling across 25+ automated test cases.

## Tools and Technologies

- Python 3.x
- Pytest
- Requests library
- Reqres API (https://reqres.in)

## Project Structure

```
ecommerce-api-tests/
├── conftest.py              # Shared fixtures and configuration
├── pytest.ini               # Pytest settings
├── requirements.txt         # Project dependencies
└── tests/
    ├── test_authentication.py   # Login and registration tests
    ├── test_get_users.py        # User retrieval tests
    └── test_user_management.py  # Create, update, delete tests
```

## Test Coverage

### Authentication Tests
- Successful login returns 200 and a valid token
- Login with missing password returns 400
- Login with missing email returns 400
- Successful registration returns token
- Registration with missing password returns 400
- Registration with undefined user returns 400

### User Retrieval Tests
- Get all users returns 200
- Response contains user data
- Pagination fields exist in response
- Page 2 returns different users than page 1
- Get single user returns correct ID and all required fields
- Non-existent user returns 404

### User Management Tests
- Create user returns 201 with correct name, job, ID and timestamp
- Create user with missing fields documents API behavior
- Update user returns 200 with updated job and timestamp
- Partial update via PATCH returns 200
- Delete user returns 204 with empty response body

## How to Run

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run all tests:
```bash
pytest -v
```
4. Run a specific test file:
```bash
pytest tests/test_authentication.py -v
```
5. Generate an HTML report:
```bash
pytest --html=reports/report.html
```

## Key Testing Concepts Demonstrated

- Pytest fixtures for reusable setup (conftest.py)
- Test classes for logical grouping
- Descriptive test names and docstrings
- Positive and negative test cases
- Status code validation
- Response body field validation
- Boundary and edge case testing
- API authentication header management

## Bugs and Observations

| Observation | Expected | Actual |
|-------------|----------|--------|
| Create user with empty payload | 400 Bad Request | 201 Created |
| Reqres accepts any payload structure | Validation error | Silent acceptance |

## Author

Madoc Quaye — QA Engineer
GitHub: github.com/madoc-q
LinkedIn: linkedin.com/in/madoc-quaye
