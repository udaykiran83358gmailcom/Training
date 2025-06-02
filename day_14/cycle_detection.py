class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head=None
    def insert(self,data):
        new=Node(data)
        if self.head==None:
            self.head=self.temp=new
        else:
            self.temp.next=new
            self.temp=new

    def display(self):
        temp = self.head
        while temp.next:
            print(temp.data, end="->")
            temp = temp.next
        temp.next=self.head.next.next
        
    def cycle(self):
        slow=fast=self.head
        while fast and fast.next:
            if slow==fast and slow !=self.head:
                print("loop ")
                break 
            slow=slow.next
            fast=fast.next.next
    def count_cycle(self):
        slow=fast=self.head
        while fast and fast.next:
            if slow==fast and slow!=self.head:
                break
            slow=slow.next
            fast=fast.next.next
        c=1
        slow=slow.next
        print(slow.data,fast.data)

        while slow!=fast:
            slow=slow.next
            c+=1
        print(c)
   
    


obj = LinkedList()
obj.insert(4)
obj.insert(2)
obj.insert(1)
obj.insert(5)
obj.insert(3)
obj.display()
obj.cycle()
obj.count_cycle()

# obj.count_cycle()