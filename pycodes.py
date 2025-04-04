import numpy as np
import collections
import itertools

# ==================== Mean, Variance, Standard Deviation ====================
print("\n=== Mean, Variance, Standard Deviation ===")
nums = list(map(int, input("Enter numbers separated by space: ").split()))
mean, var, std = np.mean(nums), np.var(nums), np.std(nums)
print(f"Mean: {mean}")
print(f"Variance: {var}")
print(f"Standard Deviation: {std}")

# ==================== Student Details and Analysis ====================
print("\n=== Student Details and Analysis ===")
students = []
n = int(input("Enter number of students: "))
for i in range(n):
    print(f"\nEnter details for student {i+1} (Name Roll Dept Address Gender Marks...):")
    data = input().split()
    name, roll, dept, addr, gender = data[:5]
    marks = list(map(int, data[5:]))
    total = sum(marks)
    percentage = total / len(marks)
    students.append((name, roll, dept, addr, gender, marks, total, percentage))

students.sort(key=lambda x: x[6])
max_marks = students[-1][0]
min_marks = students[0][0]
fail_students = [s[0] for s in students if min(s[5]) < 10]

print("\nSorted Student List (by total marks):")
for s in students:
    print(f"Name: {s[0]}, Total: {s[6]}, Percentage: {s[7]:.2f}%")

print(f"\nTopper: {max_marks}")
print(f"Lowest scorer: {min_marks}")
print(f"Failed students (any subject < 10 marks): {fail_students}")

# ==================== Top 10 Words in File ====================
print("\n=== Top 10 Words in File ===")
try:
    word_count = collections.Counter(open("file.txt").read().split())
    top_words = dict(word_count.most_common(10))
    print("Top 10 words and their counts:")
    for word, count in top_words.items():
        print(f"{word}: {count}")
except FileNotFoundError:
    print("file.txt not found!")

# ==================== Sort File Content ====================
print("\n=== Sort File Content ===")
try:
    with open("file.txt") as f:
        lines = sorted(f.readlines())
    with open("sorted_file.txt", "w") as f:
        f.writelines(lines)
    print("File content sorted and written to sorted_file.txt")
except FileNotFoundError:
    print("file.txt not found!")

# ==================== Unique Subsets ====================
print("\n=== Unique Subsets ===")
class Subsets:
    def get_subsets(self, nums):
        return [list(sub) for i in range(len(nums) + 1) for sub in itertools.combinations(nums, i)]

nums = [1, 2, 3]
print(f"All subsets of {nums}:")
print(Subsets().get_subsets(nums))

# ==================== Pair Sum to Target ====================
print("\n=== Pair Sum to Target ===")
class PairSum:
    def find_pair(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return lookup[target - num], i
            lookup[num] = i
        return None

nums = [2, 7, 11, 15]
target = 9
result = PairSum().find_pair(nums, target)
print(f"Indices of numbers in {nums} that sum to {target}: {result}")

# ==================== Inventory Management ====================
print("\n=== Inventory Management ===")
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, id, name, stock, price):
        self.items[id] = {"name": name, "stock": stock, "price": price}
        print(f"Added: {self.items[id]}")

    def update_item(self, id, stock, price):
        if id in self.items:
            self.items[id].update({"stock": stock, "price": price})
            print(f"Updated: {self.items[id]}")
        else:
            print("Item not found")

    def check_item(self, id):
        print(f"Item check for ID {id}:")
        print(self.items.get(id, "Item not found"))

inv = Inventory()
inv.add_item(1, "Pen", 100, 5)
inv.update_item(1, 80, 4)
inv.check_item(1)

# ==================== Restaurant Management ====================
print("\n=== Restaurant Management ===")
class Restaurant:
    def __init__(self):
        self.menu, self.tables, self.orders = {}, [], {}

    def add_item(self, name, price):
        self.menu[name] = price
        print(f"Added to menu: {name} - Rs.{price}")

    def book_table(self, table):
        self.tables.append(table)
        print(f"Table {table} booked.")

    def take_order(self, table, item):
        self.orders.setdefault(table, []).append(item)
        print(f"Order taken at table {table}: {item}")

    def print_data(self):
        print("\nCurrent Restaurant Data:")
        print(f"Menu: {self.menu}")
        print(f"Tables Booked: {self.tables}")
        print(f"Orders: {self.orders}")
        return self.menu, self.tables, self.orders

r = Restaurant()
r.add_item("Pasta", 250)
r.book_table(5)
r.take_order(5, "Pasta")
r.print_data()
