
#Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

def find_pairs_with_sum(arr, target_sum):
    pairs = []
    seen = set()

    for num in arr:
        complement = target_sum - num
        if complement in seen:
            pairs.append((num, complement))
        seen.add(num)

    return pairs

arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
target_sum = 7
result = find_pairs_with_sum(arr, target_sum)
print(result)  


#Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.


def reverse_array_in_place(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

arr = [1, 2, 3, 4, 5]
reverse_array_in_place(arr)
print(arr)  

#3. Write a program to check if two strings are a rotation of each other?

def are_strings_rotation(str1, str2):
    if len(str1) != len(str2):
        return False

    concatenated = str1 + str1
    return str2 in concatenated

str1 = "abcd"
str2 = "cdab"
print(are_strings_rotation(str1, str2))  

#Q4. Write a program to print the first non-repeated character from a string?


def first_non_repeated_char(s):
    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for char in s:
        if char_count[char] == 1:
            return char

    return None

s = "aabbcde"
result = first_non_repeated_char(s)
print(result)  



#5. Read about the Tower of Hanoi algorithm. Write a program to implement it.


def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, source, destination)


num_disks = 3
tower_of_hanoi(num_disks, 'A', 'B', 'C')



#Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression

def is_operator(char):
    return char in {'+', '-', '*', '/'}

def postfix_to_prefix(expression):
    stack = []
    for char in expression:
        if not is_operator(char):
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(char + operand1 + operand2)

    return stack.pop()

postfix_expr = "ab+c*"
prefix_expr = postfix_to_prefix(postfix_expr)
print(prefix_expr)




#Q7. Write a program to convert prefix expression to infix expression


def is_operator(char):
    return char in {'+', '-', '*', '/'}

def prefix_to_infix(expression):
    stack = []
    for char in reversed(expression):
        if not is_operator(char):
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append("(" + operand1 + char + operand2 + ")")

    return stack.pop()

prefix_expr = "*+abc"
infix_expr = prefix_to_infix(prefix_expr)
print(infix_expr)  




#Q8. Write a program to check if all the brackets are closed in a given code snippet.

def are_brackets_closed(code):
    stack = []
    open_brackets = {'(', '[', '{'}
    close_brackets = {')', ']', '}'}
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for char in code:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()

    return not stack

code_snippet = "(a + [b * {c - d}] + e)"
print(are_brackets_closed(code_snippet))  



#Q9. Write a program to reverse a stack.

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

def reverse_stack(stack):
    if stack.is_empty():
        return

    temp = stack.pop()
    reverse_stack(stack)
    _insert_at_bottom(stack, temp)

def _insert_at_bottom(stack, item):
    if stack.is_empty():
        stack.push(item)
        return

    temp = stack.pop()
    _insert_at_bottom(stack, item)
    stack.push(temp)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("Original stack:", stack.items)
reverse_stack(stack)
print("Reversed stack:", stack.items)



#Q10. Write a program to find the smallest number using a stack.

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

def find_smallest_number(stack):
    if stack.is_empty():
        return None

    smallest = stack.pop()
    if not stack.is_empty():
        temp = find_smallest_number(stack)
        if temp < smallest:
            smallest = temp

    stack.push(smallest)
    return smallest

stack = Stack()
stack.push(5)
stack.push(2)
stack.push(9)
stack.push(1)
stack.push(7)

smallest_number = find_smallest_number(stack)
print("Smallest number in stack:", smallest_number)  
