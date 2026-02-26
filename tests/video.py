# import { test, expect } from '@playwright/test';

# test('test', async ({ page }) => {
#   await page.goto('http://172.16.1.28:8053/authentication/login');
#   await page.getByRole('textbox', { name: 'Enter your Email Address' }).click();
#   await page.getByRole('textbox', { name: 'Enter your Email Address' }).fill('test_demo01@gmail.com');
#   await page.getByRole('textbox', { name: 'Enter your password Address' }).click();
#   await page.getByRole('textbox', { name: 'Enter your password Address' }).fill('Test@123');
#   await page.getByRole('button', { name: 'login Sign In' }).click();
#   await page.getByText('Sign Out').click();
# });


import pytest
from playwright.sync_api import sync_playwright

def test_login_logout():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://172.16.1.28:8053/authentication/login')
        page.fill('input[name="email"]', 'test_demo01@gmail.com')
        page.fill('input[name="password"]', 'Test@123')
        page.click('button:has-text("login Sign In")')
        page.click('text=Sign Out')
        browser.close()