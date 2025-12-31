# Image Library Management System

A Python application for managing and searching digital photo metadata.

## Features

- Load image metadata from CSV file
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

## Testing

### Running Unit Tests

To run the test suite:
```sh
pytest tests/ -v
```

## Usage

### Getting Help

To see all available options and usage information:
```sh
python main.py --help
```

### Basic Search Examples

1. **Search for favorite images with high DPI (summary only):**
   ```sh
   python main.py --tag "Favorite=Yes" --tag "DPI>200"
   ```

2. **Search for large images with specific size criteria:**
   ```sh
   python main.py --tag "Image Size (MB)>=20" --tag "Image X<4000"
   ```

3. **Search by user tags with detailed results:**
   ```sh
   python main.py --user-tag "Urban" --user-tag "Dusk" --verbose
   ```

4. **Search for medium resolution images:**
   ```sh
   python main.py --tag "DPI>=150" --tag "DPI<=600"
   ```

5. **Search within a geographic polygon:**
   ```sh
   python main.py --polygon "51.129,-114.010 50.742,-113.948 50.748,-113.867"
   ```

6. **Combined search (favorites in Europe with specific coordinates):**
   ```sh
   python main.py --tag "Favorite=Yes" --tag "Continent=Europe" --polygon "45.0,0.0 55.0,0.0 55.0,15.0 45.0,15.0"
   ```

### Command Line Options

- `--csv PATH`: Specify CSV file path (default: image_library.csv)
- `--tag EXPR`: Add tag criteria (format: field=value, field>value, field<value, field>=value, field<=value)
- `--user-tag TAG`: Match specific user tags
- `--polygon COORDS`: Define search polygon (format: "lat1,lon1 lat2,lon2 lat3,lon3")
- `--verbose, -v`: Show detailed results for each image found (default: summary only)

### Supported Operators

- `=`: Exact match (case-insensitive for strings)
- `>`: Greater than (for numeric values)
- `<`: Less than (for numeric values)
- `>=`: Greater than or equal to (for numeric values)
- `<=`: Less than or equal to (for numeric values)

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

### Polygon Search Requirements

- **Coordinate Order**: Polygon coordinates must be provided in sequential order (clockwise or counter-clockwise)
- **Format**: Each coordinate pair as "latitude,longitude" separated by spaces
- **Minimum Points**: At least 3 coordinate pairs required to form a polygon
- **Closure**: The polygon is automatically closed (last point connects back to first point)
- **Example**: `"52.0,-115.0 52.0,-113.0 50.0,-113.0 50.0,-115.0"` creates a rectangle

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

### Advanced File Loading

If opting for a CSV or other file format over a database, additional optimizations could include:

- **Streaming processing**: Iterator-based loading to maintain constant memory usage
- **Parallel processing**: Multi-threaded CSV parsing for faster loading
- **Chunked processing**: Process data in configurable batch sizes
- **Progress indicators**: Real-time loading progress for large datasets
- **File validation**: Schema validation and data quality checks during loading
- **Incremental loading**: Only load new/changed records since last import
