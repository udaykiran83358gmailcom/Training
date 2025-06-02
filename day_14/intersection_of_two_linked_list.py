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
            print(temp.data,end="->")
            temp=temp.next
        print()
    def check(self,obj2):
        h1=self.head
        h2=obj2.head
        print(h1.data,h2.data)
    def insert_common(self,common):
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=common.head
    def find_len(self,obj2):
        len1=self.find(self.head)
        len2=self.find(obj2.head)
        h1=self.head
        h2=obj2.head
        if len1>len2:
            for _ in range(len1-len2):
                h1=h1.next
        else:
            for _ in range(len2-len1):
                h2=h2.next
        while h1 and h2:
            if h1==h2:
                print("the intersecction point is",h1.data)
                break
            h1=h1.next
            h2=h2.next
        else:
            print("print no intersection")



        print(len1,len2)
    def find(self,head):
        temp=head
        c=0
        while head:
            c+=1
            head=head.next
        return c



    



obj=insert()
obj2=insert()
common=insert()
obj.inserted(1)
obj.inserted(4)
obj.inserted(10)
obj.inserted(2)
obj.inserted(3)
obj.inserted(23)
obj.display()
obj2.inserted(100)
obj2.inserted(100)
obj2.inserted(100)
obj2.inserted(100)
obj2.inserted(100)
obj2.display()
common.inserted(50)
common.inserted(34)
common.inserted(45)

obj.check(obj2)
obj.insert_common(common)
obj2.insert_common(common)
obj.display()
obj2.display()
common.display()
obj.find_len(obj2)