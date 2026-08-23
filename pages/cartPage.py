import re

import allure
from playwright.sync_api import expect


class cartPage:
	def __init__(self, page):
		self.cartLink = page.get_by_role("link", name=re.compile(r"item[s]? in cart"))

	@allure.step("validateCartCount")
	def validateCartCount(self, expected_count):
		expect(self.cartLink).to_contain_text(str(expected_count))
