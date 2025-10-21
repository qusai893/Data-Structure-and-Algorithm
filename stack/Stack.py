class Stack:
    
    def __init__(self):
        self.s = []
        
    # insert new element to the end of the stack
    def push(self,value):
        self.s.append(value)
        
    def pop(self):
        if self.isEmpty():
            print("The List already Empty !")
            return None
        else:
            self.s.pop()
        
        
    def isEmpty(self):
        if len(self.s) == 0:
            return True
        else:
            return False
        
    def top(self):
        return self.s[-1]
    
stack = Stack()

stack.push(10)
stack.push(5)
print("before pop",stack.top())
stack.pop()
print("after pop ",stack.top())

    

