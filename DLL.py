# Traversing of doubly Linked List Nodes

class Node:
    def __init__(self, data=None, key=None):
        self.data = data
        self.next = None
        self.prev = None
        
        
        
class Linked_List:
    def  __init__(self):
        self.head = None
        
    def Traverse(self):
        if(self.head==None):
            print("Empty Linked List")
        else:        
            PTR = self.head
            print(f"\n----------------------------")
            print(f"The linked Lists are : ", end="")
            while(PTR!=None):
                print(f"|{PTR.data}", end="|<-->")
                PTR = PTR.next
            print(" NULL")
            print("----------------------------")  
               
    def insert_at_front(self, new_data):
        if(self.head==None):
            print("Empty Linked List")
        else: 
            new_node = Node(new_data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            
    def insert_at_end(self, new_data):
        if(self.head==None):
            print("Empty Linked List")
        else:
            new_node = Node(new_data)
            PTR = self.head 
            while(PTR.next!=None):
                PTR = PTR.next
            new_node.prev = PTR
            PTR.next = new_node         

    def insert_after_value(self, VAL, new_data):
        if(self.head==None):
            print("Empty Linked List")
        else:
            new_node = Node(new_data)
            PTR = self.head
            while PTR.data!=VAL and PTR!=None:
                PTR = PTR.next
            print(PTR.data)
            # new_node.prev = PTR 
            # new_node.next = PTR.next
            # PTR.next = new_node
            # PTR.next.prev = new_node           
        
        
        
        
        
LL = Linked_List()

LL.head = Node("55")
dn = Node("2")  
LL.head.next = dn
              
while(1):
    print(f"\n======= Linked List =======")
    print("1. Traversing the Linked List")
    print("2. Adding a Element at Front")
    print("3. Adding a Element at End")
    print("4. Insert Element after value")
    # print("4. Sum of the Linked List")
    
    print()
    ch = int(input("Enter you choice : "))
    if(ch==1):
        LL.Traverse()
    elif(ch==2):
        user1 = int(input(f"\nEnter number to be added in front : ")) 
        LL.insert_at_front(user1)
    elif(ch==3):
        user2 = int(input(f"\nEnter number to be added in end : ")) 
        LL.insert_at_end(user2)
    elif(ch==4):
        user3 = int(input(f"\nEnter Value to add after : ")) 
        user4 = int(input(f"\nEnter number to add : ")) 
        LL.insert_after_value(user3,user4)
    else:
        print(f"\ninvalid input")    