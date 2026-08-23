import pytest
from playwright.sync_api import Page

from pages.cartPage import cartPage
from pages.homePage import homePage
from pages.resultsPage import resultsPage


@pytest.mark.results
def test_validate_results_screen(page: Page, navigateToAmazon):
	homePageObj = homePage(page)
	resultsPageObj = resultsPage(page)
	cartPageObj = cartPage(page)

	homePageObj.searchForProduct("iphone")
	resultsPageObj.addFirstProductToCart()
	cartPageObj.validateCartCount(1)
