#!/usr/bin/env python3
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.services.loader import ImageLibraryLoader
from src.services.search_engine import SearchEngine
from src.cli.interface import CommandLineInterface

def main():
    cli = CommandLineInterface()
    args = cli.parse_args()
    
    try:
        # Load image library
        loader = ImageLibraryLoader(args.csv)
        images = loader.load()
        print(f"Loaded {len(images)} images from {args.csv}")
        
        # Create search criteria
        criteria = cli.create_search_criteria(args)
        
        # Perform search
        search_engine = SearchEngine(images)
        results = search_engine.search(criteria)
        
        # Display results
        cli.display_results(results)
        
    except FileNotFoundError:
        print(f"Error: CSV file '{args.csv}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()