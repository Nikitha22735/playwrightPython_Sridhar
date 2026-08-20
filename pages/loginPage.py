from playwright.sync_api import sync_playwright, expect

class loginPage:
    def __init__(self,page):
        self.emailtextBox = page.get_by_role("textbox", name="Enter mobile number or email")
        self.continueBtn = page.get_by_role("button", name="Continue")
        self.pwtextBox= page.get_by_role("textbox", name="Password")
        self.signInBtn = page.get_by_role("button", name="Sign in")
        self.pwErrorMsg = page.get_by_text("Your password is incorrect")

    def enterEmailId(self,id):
        self.emailtextBox.fill(id)

    def clickOnContinueBtn(self):
        self.continueBtn.click()

    def enterPw(self,pw):
        self.pwtextBox.fill(pw)

    def clickOnSignInBtn(self):
            self.signInBtn.click()

    def validateTheVisiblityOfPwErrorMsg(self):
     expect(self.pwErrorMsg).to_be_visible()