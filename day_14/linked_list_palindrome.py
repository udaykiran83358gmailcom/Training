class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class insert:
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
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
    def reverse(self,node):
        curr=node
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev

    def check_pal(self):
        slow=fast=self.head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        prev=self.reverse(slow.next)
        slow=self.head

        while prev:
            if slow.data!=prev.data:
                print("not pal")
                break
            slow=slow.next
            prev=prev.next
        else:
            print("pal")
        
       



obj=insert()
obj.insert(1)
obj.insert(2)
obj.insert(2)
obj.insert(1)
obj.insert(0)
obj.display()
print()
# obj.reverse()
# obj.display()
obj.check_pal()