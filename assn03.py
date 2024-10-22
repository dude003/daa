class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.value_per_weight = value / weight

    def __lt__(self, other):
        return self.value_per_weight < other.value_per_weight

def fractional_knapsack(items, capacity):
    items.sort(reverse=True)
    total_value = 0
    for item in items:
        if item.weight <= capacity:
            capacity -= item.weight
            total_value += item.value
        else:
            fraction = capacity / item.weight
            total_value += item.value * fraction
            break
    return total_value

def main():
    num_items = int(input("Enter the number of items: "))
    items = []
    for i in range(num_items):
        weight = float(input(f"Enter the weight of item {i+1}: "))
        value = float(input(f"Enter the value of item {i+1}: "))
        items.append(Item(weight, value))

    capacity = float(input("Enter the capacity of the knapsack: "))

    total_value = fractional_knapsack(items, capacity)
    print(f"Total value in the knapsack: {total_value:.2f}")

if __name__ == "__main__":
    main()
