class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class bst:
    def __init__(self):
        self.root=None
    def insert(self,data):
        new=Node(data)
        if self.root==None:
            self.root=new
        else:
            self.insertion(self.root,new)
    def insertion(self,root,new):
        if root.data>new.data:
            if root.left==None:
                root.left=new
            else:
                self.insertion(root.left,new)
        else:
            if root.right==None:
                root.right=new
            else:
                self.insertion(root.right,new)

    def display(self):
        # preorder
        node=self.root
        st=[node]
        while st:
            curr=st.pop() 
            print(curr.data,end=" ")
            if curr.right:
                st.append(curr.right)
            if curr.left:
                st.append(curr.left)
    def height(self):
        node=self.root
        st=[(node,1)]
        
        maxi=1
        while st:
            curr,c=st.pop()
            if not curr.left and not curr.right:
                maxi=max(maxi,c)

            if curr.left:
                st.append((curr.left,c+1))
            if curr.right:
                st.append((curr.right,c+1))
          
        print(maxi)
    def height_of_leaf_node(self):
        node=self.root
        st=[(node,1)]
        while st:
            curr,c=st.pop()
            if not curr.left and not curr.right:
                print(curr.data,c)
            if curr.left:
                st.append((curr.left,c+1))
            if curr.right:
                st.append((curr.right,c+1))
    def path(self):
        node=self.root
        st=[(node,[node.data])]
        while st:
            curr,path=st.pop()
            if not curr.left and not curr.right:
                print(path)
            if curr.right:
                st.append((curr.right,path+[curr.right.data]))
            if curr.left:
                st.append((curr.left,path+[curr.left.data]))
    def dele_leaf_node(self,k):
        node=self.root
        st=[node]
        while st:
            curr=st.pop()
            if curr.left and curr.left.data==k:
                if not curr.left.left and not curr.left.right:
                    curr.left=None
            if curr.right and curr.right.data==k:
                if not curr.right.left and not curr.right.right:
                    curr.right=None
            if curr.data>k and curr.left:
                st.append(curr.left)
            elif curr.data<k and curr.right:
                st.append(curr.right)
    def del_node_with_one_child(self,k):
        node=self.root
        parent=None
        while node:
            if node.data==k:
                if (node.left and not node.right) or (node.right and not node.left):
                    if node.left:
                        child=node.left
                    else:
                        child =node.right
                    if parent==None:
                        self.root=None
                    else:
                        if parent.left==None:
                            parent.left=child
                        else:
                            parent.right=child


               
            parent=node
            if node.data>k:
                node=node.left
            else:
                node=node.right
    def del_node(self,k):
        node=self.root
        par=None
        while node.data!=k:
            
            if node.data>k:
                par=node
                node=node.left
            else:
                par=node
                node=node.right
        print(par.data,node.data)
                








        



            

obj=bst()
obj.insert(5) 
obj.insert(2)
obj.insert(8)
obj.insert(1)
obj.insert(7)
obj.display()
print()
obj.height()
obj.height_of_leaf_node()
obj.path()
obj.dele_leaf_node(1)
obj.display()
print()
obj.insert(1)
obj.display()
print()
obj.del_node_with_one_child(8)
obj.display()
print()
obj.insert(8)
obj.display()
print()
obj.insert(9)
obj.display()
print()
obj.del_node(8)