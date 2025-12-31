#!/usr/bin/env python3
import os
import sys

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from src.cli.interface import CommandLineInterface
from src.services.loader import ImageLibraryLoader
from src.services.search_engine import SearchEngine


def main():
    cli = CommandLineInterface()
    args = cli.parse_args()

    try:
        # Load image library
        loader = ImageLibraryLoader(args.csv)
        images = loader.load()

        # Create search criteria
        criteria = cli.create_search_criteria(args)

        # Perform search
        search_engine = SearchEngine(images)
        results = search_engine.search(criteria)

        # Display results
        cli.display_results(results, len(images), args.verbose)

    except FileNotFoundError:
        print(f"Error: CSV file '{args.csv}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
