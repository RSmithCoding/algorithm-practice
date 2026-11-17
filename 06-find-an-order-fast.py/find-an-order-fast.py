"""Generate a sorted list of 10,000 order numbers. Write a function that finds one by checking
 each in turn (linear search), then another that keeps halving the list (binary search). Count the checks each takes."""

orders = []

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
            print("Number not found.")


 

def binary_search(order_number):
    orders.sort()
    checks = 0
    start = 0
    end = len(orders) -1
    found = False

    while start <= end:
        mid = (start + end) // 2
        checks = checks + 1
        if order_number == orders[mid]:
            print(f"{order_number} found in check_list as mid - {mid} - {orders[mid]} with {checks} check")
            found = True
            break
        elif order_number < orders[mid]:
            print(f"{order_number} is smaller than {orders[mid]}")
            end = mid-1
        elif order_number > orders[mid]:
            print(f"{order_number} is greater than {orders[mid]}")
            start = mid+1

    if not found:
        print("Number not found")
  


order_gen()
orders.sort()

number_to_search = 8392



print("Search 1: Linear Search:\n")
linear_search(number_to_search)          
print("\nSearch 2: Binary Search\n")
binary_search(number_to_search)



