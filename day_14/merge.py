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
            print(temp.data)
            temp=temp.next
    def middle(self,mid):
        fast=slow=mid
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next
        return slow
    def merge(self,head):
        if not head  or not head.next:
            return head
        mid=self.middle(head)
        mid_next=mid.next
        mid.next=None 
        l=self.merge(head)
        r=self.merge(mid_next)
        return self.merge_sort(l,r)
    def merge_sort(self,l,r):
        dummy=Node(0)
        t=dummy
        while l and r:
            if l.data>r.data:
                t.next=r
                r=r.next
            else:
                t.next=l
                l=l.next
            t=t.next
        while l:
            t.next=l
            l=l.next
            t=t.next
        while r:
            t.next=r
            r=r.next
            t=t.next
        return dummy.next

    def sort(self):
        self.merge(self.head)
         
obj=insert()
obj.inserted(1)
obj.inserted(4)
obj.inserted(10)
obj.inserted(2)
obj.inserted(3)
obj.display()
obj.sort()
obj.display()
