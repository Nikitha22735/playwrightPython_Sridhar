import allure
from playwright.sync_api import expect


class resultsPage:
	def __init__(self, page):
		self.searchSuggestion = page.get_by_role("link", name="Wireless Charger")
		self.sortByButton = page.locator("#a-autoid-0-announce").get_by_text("Sort by:")
		self.addToCartButtons = page.get_by_role("button", name="Add to cart")

	@allure.step("validateSearchSuggestion")
	def validateSearchSuggestion(self):
		expect(self.searchSuggestion).to_be_visible()

	@allure.step("clickSortBy")
	def clickSortBy(self):
		self.sortByButton.click()

	@allure.step("addFirstProductToCart")
	def addFirstProductToCart(self):
		self.addToCartButtons.first.click()
