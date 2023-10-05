class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def paretoPoints(points):
    points.sort(key=lambda p: (-p.x, p.y))
    return _paretoPoints(points)

def _paretoPoints(points):
    if len(points) <= 1:
        return points

    mid = len(points) // 2
    left = _paretoPoints(points[:mid])
    right = _paretoPoints(points[mid:])

    return merge(left, right)

def merge(left, right):
    merged = []
    max_y = -1
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i].x > right[j].x or (left[i].x == right[j].x and left[i].y < right[j].y):
            if left[i].y > max_y:
                merged.append(left[i])
                max_y = left[i].y
            i += 1
        else:
            if right[j].y > max_y:
                merged.append(right[j])
                max_y = right[j].y
            j += 1
            
    while i < len(left):
        if left[i].y > max_y:
            merged.append(left[i])
            max_y = left[i].y
        i += 1
    
    while j < len(right):
        if right[j].y > max_y:
            merged.append(right[j])
            max_y = right[j].y
        j += 1
            
    return merged
