def greet(name, message="Good day!"):
    print(f"Hello, {name}! {message}")

def sum_values(*args):
    total = 0
    for num in args:
        total += num
    return total

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Positional Parameters
print("Positional Parameters:")
greet("Alice")

# Default Parameters
print("\nDefault Parameters:")
greet("Bob", "How are you?")

# Keyword Parameters
print("\nKeyword Parameters:")
print_info(name="Charlie", age=25, city="London")

# Variable Length Parameters (positional)
print("\nVariable Length Parameters (positional):")
result = sum_values(1, 2, 3, 4, 5)
print("Sum of values:", result)

# Variable Length Parameters (keyword)
print("\nVariable Length Parameters (keyword):")
print_info(name="David", age=30, city="New York")
