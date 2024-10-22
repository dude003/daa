from queue import PriorityQueue

class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = bound

    def __lt__(self, other):
        return self.bound > other.bound

def bound(node, n, W, items):
    if node.weight >= W:
        return 0
    profit_bound = node.profit
    j = node.level + 1
    total_weight = node.weight

    while j < n and total_weight + items[j][1] <= W:
        total_weight += items[j][1]
        profit_bound += items[j][0]
        j += 1

    if j < n:
        profit_bound += (W - total_weight) * items[j][0] / items[j][1]

    return profit_bound

def knapsack(W, items, n):
    Q = PriorityQueue()
    u = Node(-1, 0, 0, 0)
    v = Node(-1, 0, 0, 0)
    u.bound = bound(u, n, W, items)
    Q.put(u)
    max_profit = 0

    while not Q.empty():
        u = Q.get()
        if u.bound > max_profit:
            v.level = u.level + 1
            v.weight = u.weight + items[v.level][1]
            v.profit = u.profit + items[v.level][0]

            if v.weight <= W and v.profit > max_profit:
                max_profit = v.profit

            v.bound = bound(v, n, W, items)

            if v.bound > max_profit:
                Q.put(Node(v.level, v.profit, v.weight, v.bound))

            v.weight = u.weight
            v.profit = u.profit
            v.bound = bound(v, n, W, items)

            if v.bound > max_profit:
                Q.put(Node(v.level, v.profit, v.weight, v.bound))

    return max_profit

def main():
    num_items = int(input("Enter the number of items: "))
    items = []
    for i in range(num_items):
        value = int(input(f"Enter the value of item {i+1}: "))
        weight = int(input(f"Enter the weight of item {i+1}: "))
        items.append((value, weight))

    capacity = int(input("Enter the capacity of the knapsack: "))

    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    max_profit = knapsack(capacity, items, num_items)
    print(f"Total maximum profit: {max_profit}")

if __name__ == "__main__":
    main()
