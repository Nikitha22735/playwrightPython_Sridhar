import allure
from playwright.sync_api import sync_playwright, expect

class homePage:
    def __init__(self,page):
        self.accountsNdList = page.get_by_role("link", name="Hello, sign in Account & Lists")
        self.searchBar = page.get_by_role("searchbox", name="Search Amazon.in")
        self.amazonLogo = page.locator('[aria-label="Amazon.in"]')

    @allure.step("clickOnAccountsNdList")
    def clickOnAccountsNdList(self):
        self.accountsNdList.click()

    @allure.step("validateTheVisiblityOfSearchBar")
    def validateTheVisiblityOfSearchBar(self):
        expect(self.searchBar).not_to_be_visible()

    @allure.step("validateTheVisibilityOfLogo")
    def validateTheVisibilityOfLogo(self):
         expect(self.amazonLogo).to_be_visible()
