import pytest  # noqa
from playwright.sync_api import Page


def test_001_visit_dashboard(page: Page):
    page.goto("/")

    # Check if heading is visible
    page.get_by_role("link", name="Top Github Trending Repositories").hover()

    # Test dark theme switcher
    page.locator("#theme-switch div").click()

    # Test light theme switcher
    page.locator("path").nth(3).click()

    # Check if second graph is visible
    page.locator(".bk-Canvas > div:nth-child(11)").first.hover()

    # Switch to `This week` tab
    page.get_by_text("This week").click()

    # Check if second graph is visible
    page.locator("div:nth-child(11) > .bk-Canvas > div:nth-child(11)").hover()

    # Switch to `This month` tab
    page.get_by_text("This month").click()

    # Check if second graph is visible
    page.locator("div:nth-child(12) > .bk-Canvas > div:nth-child(11)").hover()
