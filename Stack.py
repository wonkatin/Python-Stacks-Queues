class Stack:
    def __init__(self):
        pass

    def isEmpty(self):
        """Returns True if Stack is empty, False otherwise"""
        pass

    def push(self, item):
        """Adds an item to the top of stack"""
        pass

    def pop(self):
        """Removes the item from the top of stack. Returns the removed item"""
        pass

    def peek(self):
        """Returns the top item in the stack, but doesn't remove it"""
        pass

    def size(self):
        """Returns the (int) size of the stack"""
        pass

    def __str__(self):
        """Returns a string representation of all items in stack"""
        return ""


my_stack = Stack()

print('Is Stack empty?', my_stack.isEmpty())

my_stack.push('A')
my_stack.push('B')
my_stack.push('C')
my_stack.push('D')

print('Popped item:', my_stack.pop())
print('Top item:', my_stack.peek())

print('Here are all the items in the stack:', my_stack)
print('The size of my stack is:', my_stack.size())

# BONUS - Implement the Stack with a Linked List