#!/usr/bin/env python3
import csv
import random
from typing import Any


def generate_fake_data(num_records=5000, start_index=0) -> list[Any]:
    # Data pools for realistic generation
    file_extensions = ["jpg", "jpeg", "png", "tiff", "tif", "raw", "cr2", "nef", "arw"]

    locations = [
        ("New York", 40.7128, -74.0060, "North America"),
        ("London", 51.5074, -0.1278, "Europe"),
        ("Tokyo", 35.6762, 139.6503, "Asia"),
        ("Sydney", -33.8688, 151.2093, "Australia"),
        ("Paris", 48.8566, 2.3522, "Europe"),
        ("Los Angeles", 34.0522, -118.2437, "North America"),
        ("Berlin", 52.5200, 13.4050, "Europe"),
        ("Mumbai", 19.0760, 72.8777, "Asia"),
        ("Cairo", 30.0444, 31.2357, "Africa"),
        ("Rio de Janeiro", -22.9068, -43.1729, "South America"),
        ("Vancouver", 49.2827, -123.1207, "North America"),
        ("Barcelona", 41.3851, 2.1734, "Europe"),
        ("Singapore", 1.3521, 103.8198, "Asia"),
        ("Cape Town", -33.9249, 18.4241, "Africa"),
        ("Buenos Aires", -34.6118, -58.3960, "South America"),
    ]

    user_tags_pool = [
        "Landscape",
        "Portrait",
        "Street",
        "Nature",
        "Urban",
        "Sunset",
        "Sunrise",
        "Beach",
        "Mountain",
        "Forest",
        "City",
        "Architecture",
        "Food",
        "Travel",
        "Family",
        "Wedding",
        "Event",
        "Macro",
        "Wildlife",
        "Sports",
        "Concert",
        "Festival",
        "Holiday",
        "Vacation",
        "Work",
        "Art",
        "Abstract",
        "Black and White",
        "Vintage",
        "HDR",
        "Panorama",
        "Night",
        "Golden Hour",
        "Blue Hour",
    ]

    hockey_teams = [
        "Flames",
        "Oilers",
        "Canucks",
        "Leafs",
        "Canadiens",
        "Senators",
        "Jets",
        "Rangers",
        "Bruins",
        "Blackhawks",
    ]

    records = []

    for i in range(num_records):
        # Generate filename
        ext = random.choice(file_extensions)
        location_name, lat, lon, continent = random.choice(locations)
        filename = f"{location_name.replace(' ', '_')}_{start_index + i + 1:06d}.{ext}"

        # Generate image properties
        if ext in ["raw", "cr2", "nef", "arw"]:
            size = round(random.uniform(15.0, 45.0), 2)
            dpi = random.choice([300, 600, 1200])
            bit_color = random.choice([14, 16])
        elif ext in ["tiff", "tif"]:
            size = round(random.uniform(8.0, 35.0), 2)
            dpi = random.choice([300, 600, 1200])
            bit_color = random.choice([24, 32, 48])
        else:
            size = round(random.uniform(1.5, 25.0), 2)
            dpi = random.choice([72, 96, 150, 300])
            bit_color = random.choice([24, 32])

        # Image dimensions based on common camera resolutions
        resolutions = [
            (1920, 1080),
            (3840, 2160),
            (4000, 3000),
            (6000, 4000),
            (5472, 3648),
            (4032, 3024),
            (3264, 2448),
            (2048, 1536),
        ]
        width, height = random.choice(resolutions)

        # Coordinates with some variation around the location
        coord_lat = lat + random.uniform(-0.5, 0.5)
        coord_lon = lon + random.uniform(-0.5, 0.5)

        # Format coordinates (mix of decimal and DMS)
        if random.choice([True, False]):
            coordinate = f"{coord_lat:.5f}, {coord_lon:.5f}"
        else:
            lat_dir = "N" if coord_lat >= 0 else "S"
            lon_dir = "E" if coord_lon >= 0 else "W"
            coordinate = f"{abs(coord_lat):.0f}° {random.randint(0,59):02d}' {lat_dir}, {abs(coord_lon):.0f}° {random.randint(0,59):02d}' {lon_dir}"

        # Generate tags (1-5 tags per image)
        num_tags = random.randint(1, 5)
        tags = random.sample(user_tags_pool, num_tags)
        user_tags = f'"""{", ".join(tags)}"""'

        record = {
            "Filename": filename,
            "Type": ext,
            "Image Size (MB)": size,
            "Image X": width,
            "Image Y": height,
            "DPI": dpi,
            "(Center) Coordinate": (
                coordinate if random.random() > 0.1 else ""
            ),  # 90% have coordinates
            "Favorite": "Yes" if random.random() < 0.15 else "",  # 15% are favorites
            "Continent": (
                continent if random.random() > 0.05 else ""
            ),  # 95% have continent
            "Bit color": (
                bit_color if random.random() > 0.2 else ""
            ),  # 80% have bit color
            "Alpha": "Y" if random.random() < 0.3 else "",  # 30% have alpha
            "Hockey Team": (
                random.choice(hockey_teams) if random.random() < 0.1 else ""
            ),  # 10% have hockey team
            "User Tags": (
                user_tags if random.random() > 0.1 else ""
            ),  # 90% have user tags
        }

        records.append(record)

    return records


def write_csv(records, filename="image_library.csv", append=False) -> None:
    fieldnames = [
        "Filename",
        "Type",
        "Image Size (MB)",
        "Image X",
        "Image Y",
        "DPI",
        "(Center) Coordinate",
        "Favorite",
        "Continent",
        "Bit color",
        "Alpha",
        "Hockey Team",
        "User Tags",
    ]

    mode = "a" if append else "w"
    with open(filename, mode, newline="", encoding="utf-8-sig") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not append:
            writer.writeheader()
        writer.writerows(records)


if __name__ == "__main__":
    import os

    # Check if file exists to determine starting index
    start_index = 0
    if os.path.exists("image_library.csv"):
        with open("image_library.csv", "r", encoding="utf-8-sig") as f:
            lines = f.readlines()
            start_index = len(lines) - 1 if lines else 0  # Subtract header

    print(f"Generating 5000 fake image records starting from index {start_index}...")
    records = generate_fake_data(5000, start_index)
    write_csv(records, append=(start_index > 0))

    # Count final total
    with open("image_library.csv", "r", encoding="utf-8-sig") as f:
        total_lines = len(f.readlines()) - 1  # Subtract header

    print(
        f"Generated {len(records)} records in image_library.csv (total: {total_lines} records)"
    )
