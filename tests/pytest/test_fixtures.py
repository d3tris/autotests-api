import pytest


@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] Sending data to the analytics service")


@pytest.fixture(scope="session")
def settings():
    print("[SESSION] Initialize autotest settings")


@pytest.fixture(scope="class")
def user():
    print("[CLASS] Creating user data 1 time per test class")


@pytest.fixture(scope="function")
def users_client(settings):
    print("[FUNCTION] Creating API client for each autotest")


class TestUserFlow:
    def test_user_can_login(self, settings, user, users_client):
        ...

    def test_user_can_create_course(self, settings, user, users_client):
        ...


class TestAccountFlow:
    def test_user_account(self, settings, user, users_client):
        ...


@pytest.fixture
def user_data() -> dict:
    print("Create user before test (setup)") # code before test
    yield {"username": "test_user", "email": "test@example.com"} # test itself is being performed
    print("Delete user after test (teardown)") # code after test

def test_user_email(user_data: dict):
    print(user_data)
    assert user_data["email"] == "test@example.com"


def test_user_name(user_data: dict):
    print(user_data)
    assert user_data["username"] == "test_user"
