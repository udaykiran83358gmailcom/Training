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
    def del_leaf_node(self,k):
        node=self.root
        parent=None
        while node:
            if node.data==k:
                if not node.left and not node.right:
                    if parent is None:
                        self.root=None
                    else:
                        if parent.left==node:
                            parent.left=None
                        else:
                            parent.right=None
                print(f'{k} leaf node is deleted')
                break
                    
            else:
                parent=node
                if  node.data>k:
                    node=node.left
                elif  node.data<k:
                    node=node.right
    def del_parent_with_one_child(self,k):
        node=self.root
        parent=None
        while node:
            if node.data==k:
                if (not node.left and node.right) or (not node.right and node.left):
                    if parent is None:
                        if node.left:
                            self.root=node.left
                        else:
                            self.root=node.right
                    else:
                        if node.left:
                            child=node.left
                        else:
                            child=node.right
                        if parent.left == node:
                            parent.left=child
                        else:
                            parent.right=child
                    print(f'{k} is deleted')
                    break
            else:
                parent=node
                if node.data>k:
                    node=node.left
                else:
                    node=node.right
    def del_parent_with_two_child(self, k):
        node = self.root
        parent = None

        while node:
            if node.data == k:
                if node.left and node.right:
                    succ_parent=node
                    succ=node.right
                    while succ.left:
                        succ_parent=succ
                        succ=succ.left
                    node.data=succ.data
                    succ_parent.left=None
                if succ_parent.left==succ:
                    succ_parent.left=succ.left
                else:
                    succ_parent.right=succ.right
                print(f"{k} deleted")
                return

                

                    
            if k < node.data:
                node = node.left
            else:
                node = node.right

        print(f"{k} not found in the tree")


                


                    
            




                    

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
obj.del_leaf_node(7)
obj.display()
obj.create(7)
obj.del_parent_with_one_child(13)
obj.display()
obj.create(13)
obj.display()
print()
obj.del_parent_with_two_child(12)
