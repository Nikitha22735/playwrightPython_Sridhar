from playwright.sync_api import sync_playwright, expect

class homePage:
    def __init__(self,page):
        self.accountsNdList = page.get_by_role("link", name="Hello, sign in Account & Lists")
        self.searchBar = page.get_by_role("searchbox", name="Search Amazon.in")

    def clickOnAccountsNdList(self):
        self.accountsNdList.click()

    def validateTheVisiblityOfSearchBar(self):
        expect(self.searchBar).to_be_visible()
