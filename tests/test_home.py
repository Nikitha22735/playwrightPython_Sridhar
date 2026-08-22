from playwright.sync_api import sync_playwright, expect, Page
import pytest
from pages.homePage import homePage

@pytest.mark.home
def test_validate_home_screen(page: Page):
    page.goto("https://www.amazon.in/")
    homePageObj = homePage(page)
    homePageObj.validateTheVisibilityOfLogo()
    homePageObj.validateTheVisiblityOfSearchBar()


