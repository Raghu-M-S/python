class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_data(self,data):
        node=Node(data,self.head)
        self.head=node

    def print_data(self):
        itr=self.head
        llist=''
        while itr:
            llist+=str(itr.data) + '  ------> '
            itr=itr.next
        print(llist)

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return 

        itr=self.head
        while itr.next:
            itr=itr.next

        itr.next = Node(data,None)

    def insert_new_link(self,data):
        self.head=None
        for d in data:
            print(self.insert_at_end(d))

    def find_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    
    def remove(self,index):
        if index<0 or index>self.find_length():
            return False
        
        prev=None
        curr=self.head
        count=0
        while curr and count!=index:
            prev=curr
            curr=curr.next
            count+=1

        prev.next=curr.next
        curr=None

    def swap_node(self,key1,key2):
        if key1==key2:
            return False
        prev=None
        curr=self.head
        while curr and curr.data!=key1:
            prev=curr
            curr=curr.next
        
        prev_1=None
        curr_1=self.head
        while curr_1 and curr_1.data!=key2:
            prev_1=curr_1
            curr_1=curr_1.next

        if prev:
            prev.next=curr_1
        else:
            self.head=curr_1
        
        if prev_1:
            prev_1.next=curr
        else:
            self.head = curr

        curr.next,curr_1.next = curr_1.next,curr.next
