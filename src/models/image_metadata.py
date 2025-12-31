from typing import Any, Optional


class ImageMetadata:
    def __init__(self, **kwargs: Any) -> None:
        self.data: dict[str, Any] = kwargs
        self.tags: list[str] = self._parse_tags(kwargs.get("User Tags", ""))

    def _parse_tags(self, tag_string: str) -> list[str]:
        if not tag_string:
            return []
        # Remove quotes and split by comma
        cleaned = tag_string.strip('"').replace('""', '"')
        return [tag.strip() for tag in cleaned.split(",") if tag.strip()]

    def get(self, field: str, default: Any = None) -> Any:
        return self.data.get(field, default)

    def matches_tag_value(self, field: str, operator: str, value: str) -> bool:
        field_value = self.get(field)
        if field_value is None:
            return False

        if operator == "=":
            return str(field_value).lower() == str(value).lower()
        elif operator == ">":
            try:
                return float(field_value) > float(value)
            except (ValueError, TypeError):
                return False
        elif operator == "<":
            try:
                return float(field_value) < float(value)
            except (ValueError, TypeError):
                return False
        return False

    def has_tag(self, tag: str) -> bool:
        return tag.lower() in [t.lower() for t in self.tags]

    def get_coordinates(self) -> Optional[tuple[float, float]]:
        coord_str = self.get("(Center) Coordinate", "")
        if not coord_str:
            return None

        try:
            # Handle different coordinate formats
            if "°" in coord_str:
                # DMS format: "36° 00' N, 138° 00' E"
                parts = coord_str.split(",")
                lat_part = parts[0].strip()
                lon_part = parts[1].strip()

                lat = self._parse_dms(lat_part)
                lon = self._parse_dms(lon_part)
                return (lat, lon)
            else:
                # Decimal format: "51.05011, -114.08529"
                parts = coord_str.split(",")
                lat = float(parts[0].strip())
                lon = float(parts[1].strip())
                return (lat, lon)
        except:
            return None

    def _parse_dms(self, dms_str: str) -> float:
        # Simple DMS parser for formats like "36° 00' N"
        dms_str = dms_str.strip()
        if "N" in dms_str or "S" in dms_str:
            sign = 1 if "N" in dms_str else -1
            dms_str = dms_str.replace("N", "").replace("S", "")
        elif "E" in dms_str or "W" in dms_str:
            sign = 1 if "E" in dms_str else -1
            dms_str = dms_str.replace("E", "").replace("W", "")
        else:
            sign = 1

        # Extract degrees
        degrees = float(dms_str.split("°")[0].strip())
        return degrees * sign
