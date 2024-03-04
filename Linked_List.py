# Traversing of Linked List Nodes

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def traversing(self):
        PTR = self.head
        print(f"\n----------------------------")
        print(f"The linked Lists are : ", end="")
        while PTR!=None:
            print(f"|{PTR.data}", end="|-->")
            PTR = PTR.next
        print(" NULL")
        print("----------------------------")  

    def inserting_at_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, new_data):
        if(self.head==None):
            print(f"\nHead Empty ! Please Insert Data At Front.")

        else:
            new_node = Node(new_data)
            PTR = self.head 
            while PTR.next is not None:
                PTR = PTR.next
            PTR.next = new_node
        
    def sum_of_nodes(self):
        sum1 = 0
        if self.head == None:
            print(f"\nNo Element")
        else:
            PTR = self.head
            while PTR is not None:   
                sum1 += PTR.data
                PTR = PTR.next     
        return sum1

LL = Linked_list()

while(1):
    print(f"\n======= Linked List =======")
    print("1. Traversing the Linked List")
    print("2. Adding a Element at Front")
    print("3. Adding a Element at End")
    print("4. Sum of the Linked List")
    
    print()
    ch = int(input("Enter you choice : "))
    if(ch==1):
        LL.traversing()
    elif(ch==2):
        user_input1 = int(input("Enter you element : "))
        LL.inserting_at_front(user_input1)
        LL.traversing()
    elif(ch==3):
        user_input2 = int(input("Enter you element : "))
        LL.insert_at_end(user_input2)
        LL.traversing()
    elif(ch==4):
        sum1 = LL.sum_of_nodes()
        print(f"\nThe sum of all the nodes are : {sum1}")
    else:
        print("\n'Invalid Input' :(")


    