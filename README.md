# Image Library Management System

A Python application for managing and searching digital photo metadata, similar to Adobe Lightroom's organizational capabilities.

## Features

- Load image metadata from CSV files
- Search by tag-value pairs with comparison operators (=, >, <)
- Search by user tags
- Geospatial search within polygon boundaries
- Command-line interface for easy querying

## Tech Stack

- Python 3.x (standard library only)

## Recommended Development Environment

- **VS Code** (Visual Studio Code)

### Recommended Extensions

- Black Formatter
- isort
- Pylance
- Pylint
- Python
- Python Debugger
- Amazon Q

## Setup

1. **Clone the repository**

2. **Create and activate a Python virtual environment**
   ```sh
   python -m venv .venv
   source .venv/Scripts/activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Basic Search Examples

1. **Search for favorite images with high DPI:**
   ```sh
   python main.py --tag "Favorite=Yes" --tag "DPI>200"
   ```

2. **Search by user tags:**
   ```sh
   python main.py --user-tag "Urban" --user-tag "Dusk"
   ```

3. **Search within a geographic polygon:**
   ```sh
   python main.py --polygon "51.129,-114.010 50.742,-113.948 50.748,-113.867"
   ```

4. **Combined search (favorites in Europe with specific coordinates):**
   ```sh
   python main.py --tag "Favorite=Yes" --tag "Continent=Europe" --polygon "45.0,0.0 55.0,0.0 55.0,15.0 45.0,15.0"
   ```

### Command Line Options

- `--csv PATH`: Specify CSV file path (default: image_library.csv)
- `--tag EXPR`: Add tag criteria (format: field=value, field>value, field<value)
- `--user-tag TAG`: Match specific user tags
- `--polygon COORDS`: Define search polygon (format: "lat1,lon1 lat2,lon2 lat3,lon3")

### Supported Operators

- `=`: Exact match (case-insensitive for strings)
- `>`: Greater than (for numeric values)
- `<`: Less than (for numeric values)

## Architecture

The system follows a modular architecture:

- **Models**: Data structures for images and search criteria
- **Services**: Core business logic (loading, searching, geospatial)
- **CLI**: Command-line interface and argument parsing

## Technical Notes

- Uses point-in-polygon algorithm for geospatial searches
- Supports multiple coordinate formats (decimal degrees, DMS notation)
- All search criteria use AND logic
- Handles variable metadata fields per image
- Parses comma-separated user tags from CSV

## Commercial Considerations

For a production system, I would add:

- Database backend for better performance with large datasets
- Caching and indexing for frequently searched fields
- More robust error handling and validation
- Unit tests and integration tests
- Configuration management
- Logging and monitoring
- REST API for web interface integration
- Batch processing capabilities for large imports
