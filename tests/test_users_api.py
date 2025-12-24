import json
from utils.api_client import get_users, get_user_by_id, create_post


def test_get_users_status_code():
    """
    Verify that GET /users returns HTTP 200
    """
    response = get_users()
    assert response.status_code == 200


def test_get_users_not_empty():
    """
    Verify that GET /users returns a non-empty list
    """
    response = get_users()
    assert len(response.json()) > 0


def test_get_invalid_user():
    """
    Verify that requesting an invalid user ID returns 404
    """
    response = get_user_by_id(9999)
    assert response.status_code == 404


def test_create_post_data_driven():
    """
    Data-driven test for POST /posts using JSON test data
    """
    with open("test_data/posts.json") as f:
        data = json.load(f)

    for payload in data["posts"]:
        response = create_post(payload)

        assert response.status_code == 201
        assert response.json()["title"] == payload["title"]
        assert response.json()["body"] == payload["body"]
        assert response.json()["userId"] == payload["userId"]
