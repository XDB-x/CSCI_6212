import time
import matplotlib.pyplot as plt
import numpy as np
import math

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


# Function to generate random points
def generate_random_points(num_points):
    return [Point(np.random.randint(0, 1000), np.random.randint(0, 1000)) for _ in range(num_points)]

sizes = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000]
times = []

for size in sizes:
    points = generate_random_points(size)
    sorted_points = sorted(points, key=lambda p: (p.x, p.y))

    start_time = time.time()
    paretoPoints(sorted_points)
    end_time = time.time()

    times.append(end_time - start_time)



# Now adding the theoretical O(n log n) curve
theoretical_times = [x * math.log(x) for x in sizes]  # We just compute n*log(n) for each size
normalized_theoretical_times = [t / max(theoretical_times) for t in theoretical_times]  # Normalizing to [0, 1]
normalized_actual_times = [t / max(times) for t in times]  # Normalizing the actual times to [0, 1] too
print(normalized_theoretical_times)
print(normalized_actual_times)
plt.plot(sizes, normalized_actual_times, label='Actual Time')
plt.plot(sizes, normalized_theoretical_times, label='Theoretical O(n log n)', linestyle='--')
plt.xlabel('Input Size')
plt.ylabel('Normalized Execution Time')
plt.title('Execution Time vs Input Size')
plt.legend()
plt.grid(True)
plt.show()