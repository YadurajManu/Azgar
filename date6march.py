# 1. Create a list with 7 different data types and remove last 4 elements
my_list = [10, "Hello", 3.14, True, [1, 2, 3], {"key": "value"}, (4, 5)]
removed1 = my_list.pop()
removed2 = my_list.pop()
removed3 = my_list.pop()
removed4 = my_list.pop()

print("Updated List:", my_list)
print("Removed Elements:", removed1, removed2, removed3, removed4)

# 2. Create two lists and insert the first list into the second
list1 = [1, 2, 3, 4, 5, 6]
list2 = ['a', 'b', 'c', 'd', 'e', 'f']
list2.extend(list1)  # Insert elements of list1 into list2

print("Updated List2:", list2)

# 3. Remove all even numbers from the given list
numbers = [2, 3, 5, 6, 7, 8, 9]
odd_numbers = []  # Empty list to store odd numbers

for num in numbers:
    if num % 2 != 0:  # Check if number is odd
        odd_numbers.append(num)

print("List after removing even numbers:", odd_numbers)

# 4. Using a list as a stack (Last In, First Out)
stack = [1, "apple", 3.14, True, [5, 6], {"name": "Bob"}, (8, 9)]
stack.append("new")  # Push
stack.append(99)

print("Stack after push:", stack)

stack.pop()  
stack.pop()


print("Stack after pop:", stack)


queue = [1, "banana", 3.14, False, [7, 8], {"age": 25}, (2, 3)]
queue.append("new")  
queue.append(100)

print("Queue after enqueue:", queue)

queue.pop(0)  
queue.pop(0)

print("Queue after dequeue:", queue)