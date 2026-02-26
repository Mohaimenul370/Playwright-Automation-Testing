# from playwright.sync_api import sync_playwright

# def test_login():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()

#         print("🔍 Navigating to login page...")
#         page.goto("https://www.saucedemo.com/")  # Replace this with your URL

#         print("✍️ Filling in email and password...")
#         page.fill('input[name="user-name"]', 'standard_user')
#         page.fill('input[name="password"]', 'secret_sauce')

#         print("🖱️ Clicking login button...")
#         page.click('input[type="submit"]')

#         page.wait_for_load_state('networkidle')

#         print(f"✅ Current URL after login: {"https://www.saucedemo.com/inventory.html"}")
#         assert page.url == "https://www.saucedemo.com/inventory.html"  # Replace with actual post-login URL

#         print("🎉 Login test passed!")
#         browser.close()

# test_login()  # Don't forget to call the function

# test_login_pytest.py



# import pytest
# from playwright.sync_api import Page, expect

# def test_login(page: Page):
#     page.goto("https://www.saucedemo.com/")

#     page.fill('input[name="user-name"]', 'standard_user')
#     page.fill('input[name="password"]', 'secret_sauce')
#     page.click('input[type="submit"]')

#     page.wait_for_load_state('networkidle')
#     assert "https://www.saucedemo.com/inventory.html" in page.url  # Update based on your post-login URL


import pytest
from playwright.sync_api import Page

def test_login(page: Page):
    # Start trace
    page.context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    page.goto("https://www.saucedemo.com/")
    page.fill('input[name="user-name"]', 'standard_user')
    page.fill('input[name="password"]', 'secret_sauce')
    page.click('input[type="submit"]')
    page.wait_for_load_state('networkidle')
    page.screenshot(path="screenshots/sauce_login.png")

    assert "https://www.saucedemo.com/inventory.html" in page.url

    # Save trace
    page.context.tracing.stop(path="traces/sauce_trace.zip")
