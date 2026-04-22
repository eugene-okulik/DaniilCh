import pytest

from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from endpoints.get_object import GetObject
from endpoints.patch_object import PatchObject
from endpoints.put_object import PutObject
from fixtures.object_fixtures import CREATE_OBJECT_BODY


@pytest.fixture
def create_object_endpoint():
    return CreateObject()


@pytest.fixture
def get_object_endpoint():
    return GetObject()


@pytest.fixture
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture
def patch_object_endpoint():
    return PatchObject()


@pytest.fixture
def put_object_endpoint():
    return PutObject()


@pytest.fixture
def created_object_id(create_object_endpoint, delete_object_endpoint):
    create_object_endpoint.create_object(CREATE_OBJECT_BODY)
    create_object_endpoint.check_status_code(200)
    create_object_endpoint.check_field_exists("id")

    obj_id = create_object_endpoint.response_json["id"]

    yield obj_id

    delete_object_endpoint.delete_object(obj_id)
