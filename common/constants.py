from enum import Enum

GITHUB_TRENDING_PAGE_URL = "https://github.com/trending"


class GithubTrendingDateRange(Enum):
    daily = "daily"
    weekly = "weekly"
    monthly = "monthly"
