import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject


@pytest.fixture
def new_object_id():
    body = {
        "name": "fixture_object",
        "data": {
            "year": 2024,
            "price": 100
        }
    }

    creator = CreateObject().create_object(body)
    creator.should_have_status(200)

    obj_id = creator.response_json["id"]

    yield obj_id

    DeleteObject().delete_object(obj_id)
