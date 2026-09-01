from playwright.sync_api import sync_playwright, Playwright
import pytest

@pytest.mark.api
def test_getApi(playwright: Playwright):
    context = playwright.request.new_context(http_credentials={"username":"value","password":"value"})
    # respBody = context.get("https://dummyjson.com/products/?limit=5", headers={"Authorization": "Bearer 1234"})
    respBody = context.get("https://dummyjson.com/products/?limit=5", headers={"x-api-key": "1234"})
    # print(respBody.json())
    assert respBody.status ==200
    data = respBody.json()
    print(data["products"][1]["title"])
    assert data["products"][1]["title"] == "Eyeshadow Palette with Mirror"




@pytest.mark.api
def test_PostApi(playwright: Playwright):
    context = playwright.request.new_context()
    body = {
        "title": "Gaming Chair",
        "price": 299.99,
        "brand": "DXRacer"
        }
    respBody = context.post("https://dummyjson.com/products/add", headers={"Authorization": "Bearer 1234"}, data=body)
    # print(respBody.json())
    assert respBody.status ==201
    data = respBody.json()
    print(data["products"][1]["title"])
       