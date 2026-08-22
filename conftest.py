import allure
import pytest


@pytest.fixture()
def navigateToAmazon(page):
    page.goto("https://www.amazon.in/")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.failed:
        page = item.funcargs.get("page")
        if page:
            allure.attach(page.screenshot(),name="failed ss", attachment_type=allure.attachment_type.PNG)