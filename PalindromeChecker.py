import sys
from collections import deque

class PalindromeChecker:
    def __init__(self):
        self.stack = []           # for LIFO
        self.queue = deque()      # for FIFO

    def push_character(self, ch):
        self.stack.append(ch)

    def enqueue_character(self, ch):
        self.queue.append(ch)

    def pop_character(self):
        return self.stack.pop()

    def dequeue_character(self):
        return self.queue.popleft()


# Input
s = input("Enter a word: ").strip()

# Create the PalindromeChecker object
checker = PalindromeChecker()

# Populate the stack and queue with characters of s
for char in s:
    checker.push_character(char)
    checker.enqueue_character(char)

# Compare characters
is_palindrome = True
for _ in range(len(s) // 2):
    if checker.pop_character() != checker.dequeue_character():
        is_palindrome = False
        break

# Output result
if is_palindrome:
    print(f"The word, {s}, is a palindrome.")
else:
    print(f"The word, {s}, is not a palindrome.")
