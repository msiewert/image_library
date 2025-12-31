import argparse
import sys

from ..models.search_criteria import SearchCriteria


class CommandLineInterface:
    def __init__(self):
        self.parser = self._create_parser()

    def _create_parser(self):
        parser = argparse.ArgumentParser(description="Search image library")
        parser.add_argument(
            "--csv",
            default="image_library.csv",
            help="Path to CSV file (default: image_library.csv)",
        )
        parser.add_argument(
            "--tag",
            action="append",
            help="Tag criteria in format field=value, field>value, or field<value",
        )
        parser.add_argument("--user-tag", action="append", help="User tag to match")
        parser.add_argument(
            "--polygon", help='Polygon coordinates as "lat1,lon1 lat2,lon2 lat3,lon3"'
        )
        parser.add_argument(
            "--verbose", "-v",
            action="store_true",
            help="Show detailed results for each image found"
        )
        return parser

    def parse_args(self):
        return self.parser.parse_args()

    def create_search_criteria(self, args):
        criteria = SearchCriteria()

        # Parse tag criteria
        if args.tag:
            for tag_expr in args.tag:
                field, operator, value = self._parse_tag_expression(tag_expr)
                criteria.add_tag_criterion(field, operator, value)

        # Parse user tags
        if args.user_tag:
            for tag in args.user_tag:
                criteria.add_user_tag(tag)

        # Parse polygon
        if args.polygon:
            coords = self._parse_polygon(args.polygon)
            criteria.set_polygon(coords)

        return criteria

    def _parse_tag_expression(self, expr):
        if ">=" in expr:
            field, value = expr.split(">=", 1)
            return field.strip(), ">=", value.strip()
        elif "<=" in expr:
            field, value = expr.split("<=", 1)
            return field.strip(), "<=", value.strip()
        elif ">" in expr:
            field, value = expr.split(">", 1)
            return field.strip(), ">", value.strip()
        elif "<" in expr:
            field, value = expr.split("<", 1)
            return field.strip(), "<", value.strip()
        elif "=" in expr:
            field, value = expr.split("=", 1)
            return field.strip(), "=", value.strip()
        else:
            raise ValueError(f"Invalid tag expression: {expr}")

    def _parse_polygon(self, polygon_str):
        coords = []
        for coord_pair in polygon_str.split():
            lat, lon = coord_pair.split(",")
            coords.append((float(lat), float(lon)))
        return coords

    def display_results(self, results, total_loaded, verbose=False):
        if verbose:
            if not results:
                print("No images found matching the criteria.")
            else:
                print(f"Found {len(results)} image(s):")
                for image in results:
                    filename = image.get("Filename", "Unknown")
                    image_type = image.get("Type", "Unknown")
                    size = image.get("Image Size (MB)", "Unknown")
                    print(f"- {filename} ({image_type}, {size}MB)")

                    # Show coordinates if available
                    coords = image.get_coordinates()
                    if coords:
                        print(f"  Coordinates: {coords[0]:.5f}, {coords[1]:.5f}")

                    # Show user tags if available
                    if image.tags:
                        print(f"  Tags: {', '.join(image.tags)}")
                    print()
        
        # Always show summary at the end
        print(f"\nSummary:")
        print(f"Records loaded: {total_loaded}")
        print(f"Records found: {len(results)}")
