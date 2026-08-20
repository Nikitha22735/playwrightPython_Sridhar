from playwright.sync_api import sync_playwright, expect, Page

def test_validate_home_screen(page: Page):
    page.goto("https://www.amazon.in/")
    expect(page.locator('[aria-label="Amazon.in"]')).to_be_visible()
    expect(page.get_by_placeholder('Search Amazon.in')).to_be_visible()


