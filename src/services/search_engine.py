from .geospatial import point_in_polygon

class SearchEngine:
    def __init__(self, images):
        self.images = images
    
    def search(self, criteria):
        results = []
        
        for image in self.images:
            if self._matches_criteria(image, criteria):
                results.append(image)
        
        return results
    
    def _matches_criteria(self, image, criteria):
        # Check tag-value criteria (AND operation)
        for field, operator, value in criteria.tag_criteria:
            if not image.matches_tag_value(field, operator, value):
                return False
        
        # Check user tags (AND operation)
        for tag in criteria.user_tags:
            if not image.has_tag(tag):
                return False
        
        # Check polygon constraint
        if criteria.polygon:
            coords = image.get_coordinates()
            if not coords or not point_in_polygon(coords, criteria.polygon):
                return False
        
        return True