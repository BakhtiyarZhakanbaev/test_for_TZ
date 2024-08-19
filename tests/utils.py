import random
import requests

def get_random_gender(valid_genders):
    """
    Returns a random gender from the list of valid genders.
    """
    return random.choice(valid_genders)

def get_user_id_by_gender(base_url, gender):
    """
    Fetches a list of user IDs for a given gender and returns the first one.
    """
    response = requests.get(f"{base_url}/users", params={"gender": gender}, headers={"accept": "application/json"})
    response_data = response.json()

    if response_data["idList"]:
        return response_data["idList"][0]  # Return the first ID from the list
    else:
        return None  # Return None if no users are found

def get_user_by_id(base_url, user_id):
    """
    Fetches user information by user ID.
    """
    response = requests.get(f"{base_url}/user/{user_id}", headers={"accept": "application/json"})
    return response

def validate_response_code(response, expected_status_code):
    """
    Validates that the response status code matches the expected status code.
    """
    assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, got {response.status_code}"