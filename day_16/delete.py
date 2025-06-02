class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class bst:
    def __init__(self):
        self.root=None
    def create(self,data):
        if self.root is None:
            self.root=node(data)
        else:
            self.insertion(self.root,data)
    def insertion(self,root,data):
        if root.data>data:
            if root.left==None:
                root.left=node(data)
            else:
                self.insertion(root.left,data)
        else:
            if root.right==None:
                root.right=node(data)
            else:
                self.insertion(root.right,data)
    def display(self):
        node=self.root
        st=[node]
        while st:
            curr=st.pop()
            print(curr.data,end=" ")
            if curr.right:
                st.append(curr.right)
            if curr.left:
                st.append(curr.left)
    def delete(self,k):
        node=self.root
        parent=None
        while node:
            if node.data==k:
                if not (node.left and node.right):
                    if parent.left==node:
                        parent.left=None
                    else:
                        parent.right=None
                elif (not node.left and node.right) or (node.left and not node.right):
                    if node.left:
                        child=node.left
                    else:
                        child=node.right
                    if parent==node.left:
                        parent.left=child
                    else:
                        parent.right=child
                else:
                    succ_par=node
                    succ=node.right
                    while succ.left:
                        succ_par=succ
                        succ=succ.left
                    node.data=succ.data
                    if succ_par.left==succ:
                        succ_par.left=succ.left
                    else:
                        succ_par.right=succ.right
                print(f'node {k}  is deleted')
                return

            



            parent=node
            if node.data>k:
                node=node.left
            else:
                node=node.right



obj=bst()
obj.create(10)
obj.create(8)
obj.create(7)
obj.create(9)
obj.create(12)
obj.create(11)
obj.create(13)
obj.create(15)
obj.display()
obj.delete(11)
obj.display()