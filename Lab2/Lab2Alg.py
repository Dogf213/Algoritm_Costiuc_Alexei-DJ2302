import random
import time
from bisect import bisect_left

# ---------- SEARCH ALGORITHMS ----------

def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

def insert_bst(root, key):
    if root is None:
        return BSTNode(key)
    if key < root.key:
        root.left = insert_bst(root.left, key)
    else:
        root.right = insert_bst(root.right, key)
    return root

def bst_search(root, key):
    while root:
        if key == root.key:
            return True
        root = root.left if key < root.key else root.right
    return False

def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        if arr[high] == arr[low]:
            break
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if pos < 0 or pos >= len(arr):
            break
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# ---------- TESTING FRAMEWORK ----------

def measure_time(search_func, data, key):
    start = time.perf_counter()
    search_func(data, key)
    end = time.perf_counter()
    return end - start

def test_search_algorithms():
    sizes = [1000, 5000, 10000]
    shuffle_types = ['sorted', 'reversed', 'random']
    algorithms = {
        'Linear Search': linear_search,
        'Binary Search': binary_search,
        'BST Search': None,  # special handling
        'Interpolation Search': interpolation_search
    }

    for size in sizes:
        base_data = list(range(size))
        target = random.choice(base_data)

        print(f"\n=== Array size: {size} ===")
        for shuffle_type in shuffle_types:
            if shuffle_type == 'sorted':
                data = base_data[:]
            elif shuffle_type == 'reversed':
                data = base_data[::-1]
            elif shuffle_type == 'random':
                data = base_data[:]
                random.shuffle(data)

            print(f"\n-- {shuffle_type.title()} array --")
            for name, func in algorithms.items():
                total_time = 0
                for _ in range(5):
                    if name == 'BST Search':
                        root = None
                        for val in data:
                            root = insert_bst(root, val)
                        start = time.perf_counter()
                        bst_search(root, target)
                        end = time.perf_counter()
                        elapsed = end - start
                    else:
                        elapsed = measure_time(func, data, target)
                    total_time += elapsed
                avg_time = total_time / 5
                print(f"{name}: {avg_time:.6f} seconds")

if __name__ == "__main__":
    test_search_algorithms()
