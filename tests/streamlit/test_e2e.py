import pytest  # noqa
from playwright.sync_api import Locator
from playwright.sync_api import Page


def test_001_visit_dashboard(page: Page):
    page.goto("/")

    # Check if heading is visible
    page.get_by_text("Github Trending Python Repositories").hover()

    # Check if `Today` tab is visible
    page.get_by_label("Today").locator("canvas").hover()

    # Check if `This week` tab is visible
    tab: Locator = page.get_by_role("tab", name="This week")
    assert tab.get_attribute("aria-selected") == "false"
    tab.click()
    assert tab.get_attribute("aria-selected") == "true"

    # Check if `This week` graph is visible
    page.get_by_label("This week").locator("canvas").hover()
    assert page.get_by_label("Today").locator("canvas").is_hidden()

    # Check if `This month` tab is visible
    tab: Locator = page.get_by_role("tab", name="This month")
    assert tab.get_attribute("aria-selected") == "false"
    tab.click()
    assert tab.get_attribute("aria-selected") == "true"

    # Check if `This month` graph is visible
    page.get_by_label("This month").locator("canvas").hover()

    # Check if fullscreen is working properly
    page.get_by_role("button", name="View fullscreen").hover()
    page.get_by_role("button", name="View fullscreen").click()

    # Check if exit fullscreen is working properly
    page.get_by_role("button", name="Exit fullscreen").click()
    page.get_by_role("tab", name="This week").hover()
