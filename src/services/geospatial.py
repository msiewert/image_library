def point_in_polygon(
    point: tuple[float, float], polygon: list[tuple[float, float]]
) -> bool:
    """
    Check if a point is inside a polygon using ray casting algorithm.
    
    Ray Casting Algorithm:
    - Cast a horizontal ray from the point going right to infinity
    - Count how many times the ray crosses polygon edges
    - Odd number of crossings = point is INSIDE
    - Even number of crossings = point is OUTSIDE
    
    Example: Point inside a rectangle crosses 1 edge (odd) = inside
             Point outside crosses 0 or 2 edges (even) = outside
    """
    x, y = point  # Extract coordinates of the test point
    n = len(polygon)  # Number of polygon vertices
    inside = False  # Start assuming point is outside (even crossings = 0)

    # Get first vertex to start the edge loop
    p1x, p1y = polygon[0]
    
    # Check each edge of the polygon
    for i in range(1, n + 1):
        # Get next vertex (wraps around to first vertex at end)
        p2x, p2y = polygon[i % n]
        
        # Check if ray intersects this edge
        # Ray must be between the y-coordinates of the edge endpoints
        if y > min(p1y, p2y):  # Ray is above the lower endpoint
            if y <= max(p1y, p2y):  # Ray is below (or at) the higher endpoint
                if x <= max(p1x, p2x):  # Point is to the left of the rightmost edge point
                    
                    # Calculate where ray intersects the edge (if not horizontal)
                    if p1y != p2y:  # Edge is not horizontal
                        # Linear interpolation to find x-coordinate of intersection
                        # Formula: x = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    
                    # Count this as a crossing if:
                    # - Edge is vertical (p1x == p2x), OR
                    # - Point is to the left of intersection point
                    if p1x == p2x or x <= xinters:
                        # Toggle inside/outside status (count the crossing)
                        # Each crossing flips our state: outside→inside or inside→outside
                        inside = not inside
        
        # Move to next edge: current endpoint becomes start of next edge
        p1x, p1y = p2x, p2y

    return inside
