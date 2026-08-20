import pytest


@pytest.fixture()
def navigateToAmazon(page):
    page.goto("https://www.amazon.in/")