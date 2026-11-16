"""Generate a sorted list of 10,000 order numbers. Write a function that finds one by checking
 each in turn (linear search), then another that keeps halving the list (binary search). Count the checks each takes."""

orders = []
check_list = check_list = orders


def order_gen():
    first_order = int(1001)
    orders.append(first_order)
    while len(orders) < 10000:
        first_order = first_order + 1
        orders.append(first_order)
        continue



def linear_search(order_number):
    search_count1 = 0
    for order in orders:
        search_count1 = search_count1 + 1
        if order == order_number:
            print(f"{order_number} Found! Matching {order} in {search_count1} checks")
            break
        else:
            continue

def binary_search(order_number):
    first = int(str(order_number)[0])
    
    print(first)

order_gen()

number_to_search = 8392

print("Search 1: Linear Search:\n")
linear_search(number_to_search)          
print("\nSearch 2: Binary Search\n")
binary_search(number_to_search)

print(check_list)