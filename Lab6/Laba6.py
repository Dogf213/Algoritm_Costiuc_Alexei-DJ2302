class BucketNode:
    def __init__(self, key: str, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity: int, hash_func=hash):
        self.capacity = capacity
        self.buckets = [None] * capacity
        self.hash_func = hash_func

    def compute_index(self, key: str) -> int:
        return self.hash_func(key) % self.capacity

    def add(self, key: str, value):
        index = self.compute_index(key)
        new_node = BucketNode(key, value)
        current = self.buckets[index]
        
        if current is None:
            self.buckets[index] = new_node
            return new_node.value

        # Check if key exists and replace
        prev = None
        while current:
            if current.key == key:
                current.value = value
                return current.value
            prev = current
            current = current.next

        prev.next = new_node
        return new_node.value

    def find(self, key: str):
        index = self.compute_index(key)
        current = self.buckets[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def remove(self, key: str) -> bool:
        index = self.compute_index(key)
        current = self.buckets[index]
        prev = None

        while current:
            if current.key == key:
                if prev is None:
                    self.buckets[index] = current.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next

        return False

    def free(self):
        for i in range(self.capacity):
            self.buckets[i] = None

    def __str__(self):
        result = []
        for i, bucket in enumerate(self.buckets):
            current = bucket
            bucket_str = f"[{i}]:"
            while current:
                bucket_str += f" ({current.key}: {current.value}) ->"
                current = current.next
            result.append(bucket_str + " None")
        return "\n".join(result)

# Пример использования
if __name__ == "__main__":
    table = HashTable(5)
    table.add("apple", 10)
    table.add("banana", 20)
    table.add("apricot", 30)  # может коллидировать с "apple"
    print("Table after insertions:")
    print(table)

    print("\nFind 'banana':", table.find("banana"))
    print("Find 'orange':", table.find("orange"))

    print("\nRemove 'banana':", table.remove("banana"))
    print("Table after removal:")
    print(table)

    print("\nFreeing table...")
    table.free()
    print(table)
