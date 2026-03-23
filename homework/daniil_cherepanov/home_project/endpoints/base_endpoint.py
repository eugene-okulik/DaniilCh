from utils.assertions import Assertions


class BaseEndpoint:
    BASE_URL = "http://objapi.course.qa-practice.com/object"

    def __init__(self):
        self.response = None
        self.response_json = None

    def should_have_status(self, code):
        Assertions.status_code(self.response, code)
        return self

    def should_have_field(self, path, value):
        Assertions.field_value(self.response_json, path, value)
        return self
