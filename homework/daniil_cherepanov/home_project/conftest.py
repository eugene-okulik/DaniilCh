import pytest
import allure

from fixtures.object_fixtures import *

def pytest_sessionstart(session):
    with allure.step("=== START TEST SESSION ==="):
        print("\n=== START TESTING ===")


def pytest_sessionfinish(session, exitstatus):
    with allure.step("=== FINISH TEST SESSION ==="):
        print("\n=== TESTING FINISHED ===")


@pytest.fixture(autouse=True)
def test_wrapper():
    with allure.step("=== BEFORE TEST ==="):
        print("\n--- BEFORE TEST ---")
    yield
    with allure.step("=== AFTER TEST ==="):
        print("\n--- AFTER TEST ---")