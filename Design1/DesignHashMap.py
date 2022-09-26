class MyHashMap(object):
    #create a claSS LISTNODE 
    class Listnode:
        #INITIALIZING A CONSTRUCTOR
        def __init__(self,key,val):
            #self is the object assiging the keyy and value which is only used inside this class
            self.key=key
            self.val=val
            self.next=None
            
    #creating a hashindes for hashmap        
    def hashindex(self,key):
        return key%10000
        

    def __init__(self):
        #creating a primary array for constructor
        self.hashmap=[None]*10000
        
    #where you should find a node and also the key is passed as an argument in findnode
    def findnode(self,head,key):
        #assigning the previous value to head node
        prev=head
        curr=prev.next
        #current is the next of previous node
        
        #do until the current node is equals to last of the node
        #finding the node at linkedlist (ie) where is my key in linked list
        while curr!=None and curr.key!=key:
            prev=curr
            curr=curr.next
                
        #else return the previous    
        return prev
            
        
    def put(self, key: int, value: int) -> None:
        #assigning the hashindex value 
        hash_index=self.hashindex(key)
        #checking whether the secondary data structure is created or not 
        if self.hashmap[hash_index]==None:
            #creating a dummy node as the head
            self.hashmap[hash_index]=self.Listnode(-1,-1)
            
        #passing the head to secondary data structure and passing the key
        #find node will create the previous here
        prev=self.findnode(self.hashmap[hash_index],key)
        #if a didnt find the last node insert it at hte last of linked list 
        if prev.next==None:
            prev.next=self.Listnode(key,value)
        else:
             #if it is present update  the value
            prev.next.val=value
       
            
    def get(self, key: int) -> int:
        hash_index=self.hashindex(key)
        
        #if the secondary data structure  is not created then return -1
        if self.hashmap[hash_index]==None:
            return -1
        #if the node is not there ie:the key we are searching for is not there
        
        prev=self.findnode(self.hashmap[hash_index],key)
        if prev.next== None:
            return -1
        else:
            return prev.next.val
            
            
        

    def remove(self, key: int) -> None:
        hash_index=self.hashindex(key)
        
        #if the secondary data structure  is not created then return nothing
        if self.hashmap[hash_index]==None:
            return
        
        
        prev=self.findnode(self.hashmap[hash_index],key)
        if prev.next==None:
            return None
        else:
            #if the element is removed then prev next value is previous of next of next 
            prev.next=prev.next.next    

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)