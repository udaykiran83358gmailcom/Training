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
    def sort(self):
        temp=self.head
        while True:
            swap=False
            curr=temp
            # f=0
            while curr.next:
                if curr.data>curr.next.data:
                    curr.data,curr.next.data=curr.next.data,curr.data
                    swap=True
                curr=curr.next
            if not swap:
                break
        self.display()
    def kth_large(self,k):
        temp=self.head
        curr=self.head
        while temp:
            temp=temp.next
        if k<0:
            curr=curr.next
        k-=1
        print(curr.data)





obj=insert()
obj.insert(4)
obj.insert(3)
obj.insert(2)
obj.insert(1)
obj.insert(0)
obj.display()
print()
obj.sort()
obj.kth_large(2)