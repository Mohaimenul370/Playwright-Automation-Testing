import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://172.16.1.28:8053/authentication/login")
    page.get_by_role("textbox", name="Enter your Email Address").click()
    page.get_by_role("textbox", name="Enter your Email Address").fill("test_demo01@gmail.com")
    page.get_by_role("textbox", name="Enter your password Address").click()
    page.get_by_role("textbox", name="Enter your password Address").fill("Test@123")
    page.get_by_role("button", name="login Sign In").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
