# define your sum_to_one() function above the function call

def sum_to_one(n):
    result = 1
    call_stack = []
    # Base case: n == 1
    while n != 1:
        execution_context = {'n_value':n}
        # store all necessary information to the call stack
        call_stack.append(execution_context)
        n -= 1
        print(call_stack)
    print('BASE CASE REACHED')
    return result, call_stack

sum_to_one(4)

"""
In the previous exercise, we used an iterative function to implement how a call stack accumulates execution contexts during recursive function calls.

We’ll now address the conclusion of this function, where the separate values stored in the call stack are accumulated into a single return value.
"""

def sum_to_one(n):
    result = 1
    call_stack = []

    while n != 1:
        execution_context = {"n_value": n}
        call_stack.append(execution_context)
        n -= 1
        print(call_stack)
    print("BASE CASE REACHED")
    while len(call_stack) > 0:
        return_value = call_stack.pop()
        print(call_stack)
        print('Adding n_value to result')
        result += return_value['n_value']
    return result, call_stack

sum_to_one(4)

"""
Now that we’ve built a mental model for how recursion is handled by Python, let’s implement the same function and make it truly recursive.
"""

def sum_to_one(n):
    if n == 1:
        return n
    else:
        print("Recursing with input: {0}".format(n))
        return n + sum_to_one(n-1)

print(sum_to_one(7))

##### Define factorial() below:

def factorial(n):
    if n <= 1:
        return 1
    else:
        print("Recursing with input: {0}".format(n))
        return n * factorial(n - 1)

print(factorial(12))

#####

def power_set(my_list):
    # base case: an empty list
    if len(my_list) == 0:
        return [[]]
    # recursive step: subsets without first element
    power_set_without_first = power_set(my_list[1:])
    # subsets with first element
    with_first = [ [my_list[0]] + rest for rest in power_set_without_first ]
    # return combination of the two
    return with_first + power_set_without_first

universities = ['MIT', 'Harvard', 'Stanford', 'NYU', 'Cambridge', 'Oxford', 'Imperial']
power_set_of_universities = power_set(universities)

for set in power_set_of_universities:
  print(set)

#####

def flatten(my_list):
    result = []
    for i in my_list:
        if isinstance(i, list):
            print('List found!')
            flat_list = flatten(i)
            result += flat_list
        else:
            result.append(i)
    return result

planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]

print(flatten(planets))

#####

def build_bst(my_list):
    if len(my_list) == 0:
        return 'No Child'

    middle_idx = len(my_list)//2
    middle_value = my_list[middle_idx]

    print('Middle index: {0}'.format(middle_idx))
    print('Middle value: {0}'.format(middle_value))

    tree_node = {'data' : middle_value}

    tree_node['left_child'] = build_bst(my_list[:middle_idx])

    tree_node['right_child'] = build_bst(my_list[middle_idx+1:])

    return tree_node

# For testing
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)

#####

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print("Recursive call with {0} as input".format(n))
        return fibonacci(n-2) + fibonacci(n-1)
