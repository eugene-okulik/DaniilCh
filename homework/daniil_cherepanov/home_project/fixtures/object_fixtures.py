import pytest


@pytest.fixture
def create_object_body():
    return {
        "name": "test_object",
        "data": {
            "year": 2025,
            "price": 500
        }
    }


@pytest.fixture
def patch_object_body():
    return {
        "name": "updated_test_object"
    }


@pytest.fixture
def put_object_body():
    return {
        "name": "replaced_test_object",
        "data": {
            "year": 2026,
            "price": 700
        }
    }