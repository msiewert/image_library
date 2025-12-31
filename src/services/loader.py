import csv
from ..models.image_metadata import ImageMetadata

class ImageLibraryLoader:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.images = []
    
    def load(self):
        with open(self.csv_path, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Clean empty values
                cleaned_row = {k: v for k, v in row.items() if v.strip()}
                if cleaned_row:  # Only add non-empty rows
                    self.images.append(ImageMetadata(**cleaned_row))
        return self.images