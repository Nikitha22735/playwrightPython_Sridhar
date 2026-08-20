from playwright.sync_api import sync_playwright, expect
import pytest

from pages.loginPage import loginPage
from pages.homePage import homePage

@pytest.mark.login
def test_positivelogin(page,navigateToAmazon):    
    homePageObj = homePage(page)
    loginPageObj = loginPage(page)
    homePageObj.clickOnAccountsNdList()
    loginPageObj.enterEmailId("trainingplaywright@gmail.com")
    loginPageObj.clickOnContinueBtn()
    loginPageObj.enterPw("Welcome@04")
    loginPageObj.clickOnSignInBtn()
    homePageObj.validateTheVisiblityOfSearchBar()

@pytest.mark.login
def test_negitiveLogin_pwInvalid(page,navigateToAmazon):
    homePageObj = homePage(page)
    loginPageObj = loginPage(page)
    homePageObj.clickOnAccountsNdList()
    loginPageObj.enterEmailId("trainingplaywright@gmail.com")
    loginPageObj.clickOnContinueBtn()
    loginPageObj.enterPw("Welcome@03")
    loginPageObj.clickOnSignInBtn()
    loginPageObj.validateTheVisiblityOfPwErrorMsg()