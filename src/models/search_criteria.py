class SearchCriteria:
    def __init__(self):
        self.tag_criteria = []  # List of (field, operator, value) tuples
        self.polygon = None     # List of (lat, lon) tuples
        self.user_tags = []     # List of user tags to match
    
    def add_tag_criterion(self, field, operator, value):
        self.tag_criteria.append((field, operator, value))
    
    def add_user_tag(self, tag):
        self.user_tags.append(tag)
    
    def set_polygon(self, coordinates):
        self.polygon = coordinates