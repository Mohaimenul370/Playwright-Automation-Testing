# import pytest
# from playwright.sync_api import Page, expect

# def test_login(page: Page):
#     page.goto("http://172.16.1.28:8053/authentication/login")

#     page.fill('input[name="Enter your Email Address"]', 'test_demo01@gmail.com')
#     page.fill('input[name="Enter your password Address"]', 'Test@123')
#     page.click('input[type="submit"]')

#     page.wait_for_load_state('networkidle')
#     assert "http://172.16.1.28:8053/" in page.url  # Update based on your post-login URL



# import pytest
# from playwright.sync_api import Page

# def test_login_with_media(page: Page, request):
#     page.context.tracing.start(
#         screenshots=True,
#         snapshots=True,
#         sources=True
#     )
#     page.goto("http://172.16.1.28:8053/authentication/login")
#     page.fill('input[name="email-input"]', 'test_demo01@gmail.com')
#     page.fill('input[name="password-input"]', 'Test@123')
#     page.click('input[type="submit"]')
#     page.wait_for_load_state('networkidle')
#     page.screenshot(path="screenshots/login_result.png")
#     assert "http://172.16.1.28:8053/" in page.url
#     page.context.tracing.stop(path="traces/trace_login.zip")
#     print("🎉 Login test passed!")

# import pytest
# from playwright.sync_api import Page

# def test_login_with_media(page: Page):
#     page.goto("http://172.16.1.28:8053/authentication/login")

#     page.fill('input[name="email-input"]', 'test_demo01@gmail.com')
#     page.fill('input[name="password-input"]', 'Test@123')
#     page.click('input[type="submit"]')

#     page.wait_for_load_state('networkidle')

#     page.screenshot(path="screenshots/login_result.png")

#     assert "http://172.16.1.28:8053/" in page.url
#     print("🎉 Login test passed!")


def test_login(page):
    # Visit the login page
    page.goto("http://172.16.1.28:8053/authentication/login")

    # Optional: clicks on body if needed (often not necessary)
    page.locator('body').click()
    page.locator('body').click()

    # Click the first input wrapper (if needed for focus or clearing)
    page.locator('.ant-input-affix-wrapper').first.click()

    # Fill email
    page.get_by_role("textbox", name="Enter your Email Address").fill("test_demo01@gmail.com")

    # Fill password
    page.get_by_role("textbox", name="Enter your password Address").click()
    page.get_by_role("textbox", name="Enter your password Address").fill("Test@123")

    # Click the login button
    page.get_by_role("button", name="login Sign In").click()

    # After successful login, click "Sign Out"
    page.get_by_text("Sign Out").click()

    # pytest tests/test_login.py --headed
    # pytest tests/test_smm_login_pytest.py --html=report.html --self-contained-html


