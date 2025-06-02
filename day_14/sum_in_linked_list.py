class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class insert:
    def __init__(self):
        self.head=None
    def inserted(self,data):
        new=Node(data)
        if self.head==None:
            self.temp=self.head=new
        else:
            self.temp.next=new
            self.temp=new 
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()
    def reverse(self):
        cur=self.head
        prev=None
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        return prev
    def find_sum(self,h1,h2):
        dum=Node(0)
        tail=dum
        carr=0
        tot=0
        while h1 and h2:
            tot=h1.data+h2.data+carr
            if tot>9:
                carr=tot//10
                curr=tot%10
                tail.next=Node(curr)
            else:
                tail.next=Node(tot)
            h1=h1.next
            h2=h2.next
            tail=tail.next
        if carr>0:
            tail.next=Node(carr)
        while h1:
            tail.next=Node(h1.data)
            h1=h1.next
        while h2:
            tail.next=Node(h2.data)
            h2=h2.next
        self.display(dum.next)








obj=insert()
obj2=insert()
obj.inserted(1)
obj.inserted(4)
obj.inserted(5)
obj.display()
obj2.inserted(1)
obj2.inserted(4)
obj2.inserted(5)
obj2.display()
h1=obj.reverse()
h2=obj.reverse()
