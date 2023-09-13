import re

import pytest  # noqa
from playwright.sync_api import Locator
from playwright.sync_api import Page


def test_001_visit_dashboard(page: Page):
    page.goto("/")

    assert (
        page.get_by_role("heading", name="Github Trending Python Repositories").text_content()
        == "Github Trending Python Repositories"
    )
    daily_graph: Locator = page.locator(".nsewdrag")
    daily_graph.hover()
    assert daily_graph.is_visible()

    page.locator("div").filter(has_text=re.compile(r"^This week$")).click()
    assert page.locator(".nsewdrag").is_visible()

    page.locator("div").filter(has_text=re.compile(r"^This month$")).click()
    assert page.locator(".nsewdrag").is_visible()
