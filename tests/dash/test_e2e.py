import re

import pytest  # noqa
from playwright.sync_api import Page


def test_001_visit_dashboard(page: Page):
    page.goto("/")

    # Check if heading is visible
    page.get_by_role("heading", name="Github Trending Python Repositories").hover()

    # Check if graph is visible
    page.locator(".nsewdrag").hover()

    # Clik into second tab
    page.locator("div").filter(has_text=re.compile(r"^This week$")).click()
    page.locator(".nsewdrag").hover()

    # Clik into third tab
    page.locator("div").filter(has_text=re.compile(r"^This month$")).click()
    page.locator(".nsewdrag").hover()
