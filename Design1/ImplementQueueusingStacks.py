class MyQueue:

    def __init__(self):
     #Initializing an array of in stack
        self.inn=[]
     #Initializing an array of out stack  
        self.out=[]    
        
    def push(self, x: int) -> None:
        #Pushing the values of input in "Instack" 
        self.inn.append(x)
        

    def pop(self) -> int:
        #storing the peek value in temperory variable
        element=self.peek()
        #returning all the values till the last element
        self.out=self.out[:-1]
        #returning the popped value 
        return element

    def peek(self) -> int:
        #Checking whether the Outstack is empty or not
        if len(self.out)==0:
        #if the outstack is empty then append the instack values to outstack
            while self.inn:
            #Popping all the elements and adding it to the outstack
                self.out.append(self.inn.pop()) 
            #returning the last element from the outstack
        return self.out[-1]
                
            
        

    def empty(self) -> bool:
        #Removing all the elements in "Instack " and "Outstack"
        return len(self.inn)+len(self.out)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()