"""Generate a sorted list of 10,000 order numbers. Write a function that finds one by checking
 each in turn (linear search), then another that keeps halving the list (binary search). Count the checks each takes."""

orders = []
check_list = check_list = orders
list = []
list_copy = []


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



def get_counts(list_to_count):
    counter = 0
    while len(list_to_count) > 2:
        list_len = int(round(len(list_to_count)) / 2)
        del list_copy[0:list_len]
        counter = counter + 1
    return counter    

def binary_search(order_number,counter):
        steps = 0

        for i in range(counter):
            half = round(len(list)/2)
            
            if order_number <= list[half]:
                print(list[0:half+1])
                steps = steps + 1
                del list[half+1:len(list)]
            
            else:
                print(list[half+1:len(list)])
                steps = steps + 1
                del list[0:half+1]
            



order_gen()
list = orders.copy()
list_copy = orders.copy()
list.sort()

number_to_search = 8392

counter = get_counts(list_copy)


print(f"The list will need {counter} steps to narrow search")

print("Search 1: Linear Search:\n")
linear_search(number_to_search)          
print("\nSearch 2: Binary Search\n")
binary_search(number_to_search,counter)

# if len(list) == 2:
#     if number_to_search < list[1]:
#         steps = steps + 1
#         del list[1]
#         print(f"Order {number_to_search} found in list {list} with {steps} steps")
        
# else:
#     print(f"order {number_to_search} has been found in list {list} with {steps} steps **else")



