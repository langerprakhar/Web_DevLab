import numpy as np
import collections
import itertools

# Mean, Variance, Standard Deviation
nums = list(map(int, input().split()))
mean, var, std = np.mean(nums), np.var(nums), np.std(nums)
print(f"Mean: {mean}, Variance: {var}, Standard Deviation: {std}")

# Student Details and Analysis
students = []
for _ in range(int(input("Enter number of students: "))):
    data = input("Enter student details (Name, Roll, Dept, Address, Gender, Marks): ").split()
    name, roll, dept, addr, gender = data[:5]
    marks = list(map(int, data[5:]))
    total = sum(marks)
    percentage = total / len(marks)
    students.append((name, roll, dept, addr, gender, marks, total, percentage))

students.sort(key=lambda x: x[6])
max_marks = students[-1][0]
min_marks = students[0][0]
fail_students = [s[0] for s in students if min(s[5]) < 10]
print(f"Topper: {max_marks}, Lowest scorer: {min_marks}, Failed students: {fail_students}")

# Top 10 Words in File
word_count = collections.Counter(open("file.txt").read().split())
print(dict(word_count.most_common(10)))

# Sort File Content
with open("file.txt") as f:
    lines = sorted(f.readlines())
with open("sorted_file.txt", "w") as f:
    f.writelines(lines)

# Unique Subsets
class Subsets:
    def get_subsets(self, nums):
        return [list(sub) for i in range(len(nums) + 1) for sub in itertools.combinations(nums, i)]
print(Subsets().get_subsets([1, 2, 3]))

# Pair Sum to Target
class PairSum:
    def find_pair(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return lookup[target - num], i
            lookup[num] = i
print(PairSum().find_pair([2, 7, 11, 15], 9))

# Inventory Management
class Inventory:
    def __init__(self):
        self.items = {}
    def add_item(self, id, name, stock, price):
        self.items[id] = {"name": name, "stock": stock, "price": price}
    def update_item(self, id, stock, price):
        if id in self.items:
            self.items[id].update({"stock": stock, "price": price})
    def check_item(self, id):
        return self.items.get(id, "Item not found")

# Restaurant Management
class Restaurant:
    def __init__(self):
        self.menu, self.tables, self.orders = {}, [], {}
    def add_item(self, name, price):
        self.menu[name] = price
    def book_table(self, table):
        self.tables.append(table)
    def take_order(self, table, item):
        self.orders.setdefault(table, []).append(item)
    def print_data(self):
        return self.menu, self.tables, self.orders

r = Restaurant()
r.add_item("Pasta", 250)
r.book_table(5)
r.take_order(5, "Pasta")
print(r.print_data())
