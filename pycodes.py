import numpy as np
import collections
import itertools

# ==================== Mean, Variance, Standard Deviation ====================
def calculate_statistics():
    print("\n=== Mean, Variance, Standard Deviation ===")
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    mean, var, std = np.mean(nums), np.var(nums), np.std(nums)
    print(f"Mean: {mean}")
    print(f"Variance: {var}")
    print(f"Standard Deviation: {std}")

# ==================== Student Details and Analysis ====================
def student_analysis():
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
def top_words():
    print("\n=== Top 10 Words in File ===")
    filename = input("Enter file name: ")
    try:
        word_count = collections.Counter(open(filename).read().split())
        top_words = dict(word_count.most_common(10))
        print("Top 10 words and their counts:")
        for word, count in top_words.items():
            print(f"{word}: {count}")
    except FileNotFoundError:
        print(f"{filename} not found!")

# ==================== Sort File Content ====================
def sort_file():
    print("\n=== Sort File Content ===")
    filename = input("Enter file name: ")
    try:
        with open(filename) as f:
            lines = sorted(f.readlines())
        with open("sorted_" + filename, "w") as f:
            f.writelines(lines)
        print(f"File content sorted and written to sorted_{filename}")
    except FileNotFoundError:
        print(f"{filename} not found!")

# ==================== Unique Subsets ====================
def unique_subsets():
    print("\n=== Unique Subsets ===")
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    subsets = [list(sub) for i in range(len(nums) + 1) for sub in itertools.combinations(nums, i)]
    print(f"All subsets of {nums}: {subsets}")

# ==================== Pair Sum to Target ====================
def pair_sum():
    print("\n=== Pair Sum to Target ===")
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    target = int(input("Enter target sum: "))
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            print(f"Indices of numbers in {nums} that sum to {target}: {lookup[target - num]}, {i}")
            return
        lookup[num] = i
    print("No such pair found.")

# ==================== Inventory Management ====================
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self):
        id = input("Enter item ID: ")
        name = input("Enter item name: ")
        stock = int(input("Enter stock quantity: "))
        price = float(input("Enter item price: "))
        self.items[id] = {"name": name, "stock": stock, "price": price}
        print(f"Added: {self.items[id]}")

    def update_item(self):
        id = input("Enter item ID to update: ")
        if id in self.items:
            stock = int(input("Enter new stock: "))
            price = float(input("Enter new price: "))
            self.items[id].update({"stock": stock, "price": price})
            print(f"Updated: {self.items[id]}")
        else:
            print("Item not found")

    def check_item(self):
        id = input("Enter item ID to check: ")
        print(f"Item check for ID {id}: {self.items.get(id, 'Item not found')}")

def inventory_management():
    print("\n=== Inventory Management ===")
    inv = Inventory()
    while True:
        print("\n1. Add Item\n2. Update Item\n3. Check Item\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            inv.add_item()
        elif choice == "2":
            inv.update_item()
        elif choice == "3":
            inv.check_item()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

# ==================== Restaurant Management ====================
class Restaurant:
    def __init__(self):
        self.menu = {}
        self.tables = []
        self.orders = {}

    def add_item(self):
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        self.menu[name] = price
        print(f"Added to menu: {name} - Rs.{price}")

    def book_table(self):
        table = input("Enter table number: ")
        if table not in self.tables:
            self.tables.append(table)
            print(f"Table {table} booked.")
        else:
            print("Table already booked!")

    def take_order(self):
        table = input("Enter table number: ")
        if table not in self.tables:
            print("Table not booked yet!")
            return
        item = input("Enter item name: ")
        if item not in self.menu:
            print("Item not available in menu!")
            return
        self.orders.setdefault(table, []).append(item)
        print(f"Order taken at table {table}: {item}")

    def print_data(self):
        print("\nCurrent Restaurant Data:")
        print(f"Menu: {self.menu}")
        print(f"Tables Booked: {self.tables}")
        print(f"Orders: {self.orders}")

def restaurant_management():
    print("\n=== Restaurant Management ===")
    r = Restaurant()
    while True:
        print("\n1. Add Item to Menu\n2. Book Table\n3. Take Order\n4. Show Data\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            r.add_item()
        elif choice == "2":
            r.book_table()
        elif choice == "3":
            r.take_order()
        elif choice == "4":
            r.print_data()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

# ==================== Main Menu ====================
def main():
    while True:
        print("\n===== Main Menu =====")
        print("1. Calculate Statistics")
        print("2. Student Analysis")
        print("3. Top 10 Words in File")
        print("4. Sort File Content")
        print("5. Unique Subsets")
        print("6. Pair Sum")
        print("7. Inventory Management")
        print("8. Restaurant Management")
        print("9. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            calculate_statistics()
        elif choice == "2":
            student_analysis()
        elif choice == "3":
            top_words()
        elif choice == "4":
            sort_file()
        elif choice == "5":
            unique_subsets()
        elif choice == "6":
            pair_sum()
        elif choice == "7":
            inventory_management()
        elif choice == "8":
            restaurant_management()
        elif choice == "9":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
