import pytest

@pytest.fixture(scope="session")
def base_url():
    return "https://hr-challenge.dev.tapyou.com/api/test"

@pytest.fixture(scope="session")
def valid_genders():
    return ["male", "female", "any", "magic", "McCloud"]

@pytest.fixture(scope="session")
def invalid_genders():
    return ["randomtext", "12345", ""]