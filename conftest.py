import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    """
    This fixture launches a new browser context and page for every test.
    Using scope="function" ensures each test starts with a clean slate (no cookies/cache).
    """
    with sync_playwright() as p:
        
        browser = p.chromium.launch(headless=True)
        
        context = browser.new_context()
        
        page = context.new_page()
        
        yield page

        context.close()
        browser.close()