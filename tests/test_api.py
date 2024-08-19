import pytest

from utils import get_random_gender, get_user_id_by_gender, get_user_by_id, validate_response_code


def test_get_user_by_random_gender(base_url, valid_genders):
    """
    Test that fetches a user ID by random gender and verifies the user's gender matches the requested one.
    """
    # Step 1: Get a random gender
    random_gender = get_random_gender(valid_genders)

    # Step 2: Get user ID by this random gender
    user_id = get_user_id_by_gender(base_url, random_gender)

    # If no user ID is found, skip the test (to handle cases where there might be no users with that gender)
    if not user_id:
        pytest.skip(f"No users found with gender {random_gender}")

    # Step 3: Fetch user information by user ID
    response = get_user_by_id(base_url, user_id)
    validate_response_code(response, 200)

    # Step 4: Verify that the gender in the response matches the one used in the request
    user_data = response.json()
    assert user_data["user"][
               "gender"] == random_gender, f"Expected gender {random_gender}, but got {user_data['user']['gender']}"