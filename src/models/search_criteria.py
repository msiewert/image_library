from typing import Optional


class SearchCriteria:
    def __init__(self) -> None:
        self.tag_criteria: list[tuple[str, str, str]] = (
            []
        )  # List of (field, operator, value) tuples
        self.polygon: Optional[list[tuple[float, float]]] = (
            None  # List of (lat, lon) tuples
        )
        self.user_tags: list[str] = []  # List of user tags to match

    def add_tag_criterion(self, field: str, operator: str, value: str) -> None:
        self.tag_criteria.append((field, operator, value))

    def add_user_tag(self, tag: str) -> None:
        self.user_tags.append(tag)

    def set_polygon(self, coordinates: list[tuple[float, float]]) -> None:
        self.polygon = coordinates
