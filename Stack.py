class Stack:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        """Returns True if Stack is empty, False otherwise"""
        return len(self.data) == 0

    def push(self, item):
        """Adds an item to the top of stack"""
        self.data.append(item)

    def pop(self):
        """Removes the item from the top of stack. Returns the removed item"""
        return self.data.pop()

    def peek(self):
        """Returns the top item in the stack, but doesn't remove it"""
        return self.data[len(self.data) - 1]

    def size(self):
        """Returns the (int) size of the stack"""
        return len(self.data)

    def __str__(self):
        """Returns a string representation of all items in stack"""
        stack_str = ""
        for i in range(len(self.data)):
            stack_str += self.data[i] + " "
        return stack_str


### TEST SUITE ###
# Use the following code to help you implement the Stack
my_stack = Stack()

print('Is Stack empty? Should be True: \n', my_stack.isEmpty())

my_stack.push('A')
my_stack.push('B')
my_stack.push('C')
my_stack.push('D')

print('Popped item should be D: \n', my_stack.pop())
print('Top item should be C: \n', my_stack.peek())
print('Here are all the items in the stack - Should be A B C: \n', my_stack)
print('The size of stack should be 3: \n', my_stack.size())

# Bonus Question - How would our Stack implementation change if we
# created it with a LinkedList instead of a List?
# What is a LinkedList?