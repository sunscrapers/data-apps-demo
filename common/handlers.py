import re
from dataclasses import asdict
from dataclasses import dataclass
from typing import Dict
from typing import List
from typing import Optional

import requests
from bs4 import BeautifulSoup
from bs4 import Tag

from common.constants import GITHUB_TRENDING_PAGE_URL
from common.constants import GithubTrendingDateRange
from common.schemas import RepositoryData

repo_name_pattern: str = r"([\w\-\_\.]+)"
stars_count_pattern: str = r"([\w\,]+)"


@dataclass
class GithubTrendingHandler:
    """
    A class for retrieving the latest Github trending data for Python language repositories
    by scraping HTML and returning the data as a list of RepositoryData objects or dicts.
    """

    date_range: Optional[GithubTrendingDateRange] = None

    def __get_text_from_strings(self, pattern: str, strings: List[str]) -> List[str]:
        repo_name_parts: List[str] = []

        for input_string in strings:
            matches = re.search(pattern, input_string)
            if matches:
                try:
                    extracted_text = matches.group(1)
                    repo_name_parts.append(extracted_text)
                except IndexError:
                    pass
        return repo_name_parts

    def __gen_repo_name(self, strings: List[str]) -> Optional[str]:
        if not len(strings) == 2:
            return "Unknown"
        return " / ".join(strings)

    def __gen_stars_count(self, strings: List[str]) -> int:
        if len(strings) != 1:
            return 0

        stars_count_str: str = strings[0]
        stars_count_numbers: List[str] = stars_count_str.split(",")

        try:
            return int(int("".join(stars_count_numbers)))
        except ValueError:
            return 0

    def get_repo_full_name(self, repo: Tag) -> str:
        repo_name_heading: Tag = repo.find("h2", class_="h3 lh-condensed")
        repo_name_link: Tag = repo_name_heading.find("a", class_="Link")

        repo_full_name_strings: List[str] = self.__get_text_from_strings(
            pattern=repo_name_pattern, strings=list(repo_name_link.strings)
        )

        return self.__gen_repo_name(repo_full_name_strings)

    def get_repo_stars_count(self, repo: Tag) -> int:
        stars_count_block: Tag = repo.find("div", class_="f6 color-fg-muted mt-2")
        stars_count_link: Tag = stars_count_block.find("a", class_="Link")

        repo_stars_count_strings: List[str] = self.__get_text_from_strings(
            pattern=stars_count_pattern, strings=list(stars_count_link.strings)
        )
        return self.__gen_stars_count(strings=repo_stars_count_strings)

    def get_repo_trending_stars_count(self, repo: Tag) -> int:
        trending_stars_count_block: Tag = repo.find("span", class_="d-inline-block float-sm-right")
        trending_stars_count_strings: List[str] = self.__get_text_from_strings(
            pattern=stars_count_pattern,
            strings=list(trending_stars_count_block.strings),
        )
        return self.__gen_stars_count(strings=trending_stars_count_strings)

    def get_repo_data(self, repo: Tag) -> RepositoryData:
        repo_full_name: str = self.get_repo_full_name(repo=repo)
        repo_stars_count: int = self.get_repo_stars_count(repo=repo)
        repo_trending_stars_count: int = self.get_repo_trending_stars_count(repo=repo)

        return RepositoryData(
            full_name=repo_full_name,
            stars_count=repo_stars_count,
            trending_stars_count=repo_trending_stars_count,
        )

    def get_repos(self) -> List[Tag]:
        date_range: GithubTrendingDateRange = self.date_range if self.date_range else GithubTrendingDateRange.weekly
        url = f"{GITHUB_TRENDING_PAGE_URL}?since={date_range.value}"

        page_response: requests.Response = requests.get(url, timeout=10)
        if not page_response.status_code == 200:
            raise Exception("Error during loading Github Trending page")

        soup: BeautifulSoup = BeautifulSoup(page_response.content, "html.parser")
        return soup.find_all("article", class_="Box-row")

    def get_repos_data(self) -> List[RepositoryData]:
        repositories: List[Tag] = self.get_repos()

        if not repositories:
            return []

        repos_data: List[RepositoryData] = []
        for repo in repositories:
            repos_data.append(self.get_repo_data(repo=repo))

        return repos_data

    def get_json_repos_data(self) -> List[Dict[str, str]]:
        repos_data: List[RepositoryData] = self.get_repos_data()

        return [asdict(repo_data) for repo_data in repos_data]
