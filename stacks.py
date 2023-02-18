

# stack
class Stack:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return not self.item
    
    def push(self,item):
        self.item.append(item)

    def pop(self):
        return self.item.pop()
    
    def peek(self):
        return self.item[-1]
    
    def size(self):
        return len(self.item)
    
    def __str__(self):
        return str(self.item)

    
if __name__ == "__main__":
    s = Stack()
    s.push(3)
    s.pop()
    print("stack : ",s)
    print("the size of the stack is  : ",s.size())
    if s == None:
        print("stack is empty : ",s.is_empty())
    else:
        print("stack containing elements : ",s)    


    

