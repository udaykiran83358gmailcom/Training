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
    def reverse(self):
        prev=None
        curr=self.head
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        self.head=prev
    def second_largest(self):
        f_max,s_max=0,0
        temp=self.head
        while temp.next:
            if temp.data>f_max:
                s_max=f_max
                f_max=temp.data
            elif temp.data>s_max:
                s_max=temp.data
            temp=temp.next
        print(f_max,s_max)
    def conigutive(self,k):
        temp=self.head
        g=0
        while temp:
            cur=temp.next
            while cur:
                if (temp.data+cur.data)==k:
                    g+=1
                cur=cur.next
            temp=temp.next
        print("the number of pairs",g)
    def conti(self,k):
        temp=self.head
        cur=temp.next
        c=0
        while temp.next:
            if cur.data+temp.data==k:
                c+=1
            temp=temp.next
        print(c)
    def find_sorted(self):
        slow=self.head
        fast=slow
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        while slow:
            print(slow.data)
            slow=slow.next

    def find_ele(self,k):
        slow=self.head
        fast=slow.next
        c=0
        while fast or slow:
            if slow.data==k:
                print(c)
                break
            elif fast.data==k:
                print(c+1)
                break
            c+=2
            slow=slow.next.next
            fast=fast.next.next
    def find_kth_node_last(self,k):
        c=1
        # temp=self.head
        # while temp:
        #     c+=1
        #     temp=temp.next
        # temp=self.head
        # print(c)
        # f=c-k
        # while f>0:
        #     temp=temp.next
        #     f-=1

        # print(temp.data)
        slow=fast=self.head
        while fast:
            fast=fast.next
            k-=1
            if k<-1:
                slow=slow.next
        slow.next=slow.next.next
     
        self.display()
    def swap(self):
        slow=self.head
       
        while slow and slow.next:
            fast=slow.next
            slow.data,fast.data=fast.data,slow.data
            slow=fast.next
        print()
        self.display()
        

        



        



            
            
        
        





             
                     

    

obj=insert()
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)
obj.insert(5)
# obj.insert(6)
# obj.insert(6)
obj.display()    
obj.reverse()
obj.display()
# obj.second_largest()
# obj.conigutive(5)
# obj.conti(5)
# obj.find_sorted()
# obj.find_ele(5)
# obj.find_kth_node_last(3)
# obj.swap()

