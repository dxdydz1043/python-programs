class Node:

    def __init__(self,data,left=None,right=None,parent=None):
        self.data=data
        self.right=right
        self.left=left
        self.parent=parent

class Splay_tree:

    def __init__(self):
        self.root=None
        self.isroot=False
    
    def zig(self,pos):          # right_rotate

        temp_1=pos.parent
        temp_2=pos.right
        temp_3=temp_1.parent
        pos.parent=temp_1.parent
        pos.right=temp_1
        temp_1.parent=pos
        temp_1.left=temp_2

        if temp_2:
            temp_2.parent=temp_1

        if temp_3:
            if temp_3.right is temp_1:
                temp_3.right=pos
            else:
                temp_3.left=pos
        else:
            self.root=pos
    
    def zag(self,pos):          # left_rotate

        temp_1=pos.parent
        temp_2=pos.left
        temp_3=temp_1.parent
        pos.parent=temp_1.parent
        pos.left=temp_1
        temp_1.parent=pos
        temp_1.right=temp_2

        if temp_2:
            temp_2.parent=temp_1

        if temp_3:
            if temp_3.right is temp_1:
                temp_3.right=pos
            else:
                temp_3.left=pos
        else:
            self.root=pos

    def zig_zig(self,pos):

        self.zig(pos.parent)
        self.zig(pos)
    
    def zag_zag(self,pos):

        self.zag(pos.parent)
        self.zag(pos)
    
    def zig_zag(self,pos):

        self.zag(pos)
        self.zig(pos)
    
    def zag_zig(self,pos):
        
        self.zig(pos)
        self.zag(pos)
    
    def splay(self,pos):
        while pos.parent:
            gp=pos.parent.parent
            p=pos.parent

            if gp:
                if gp.left==p and p.left==pos:
                    self.zig_zig(pos)
                elif gp.right==p and p.right==pos:
                    self.zag_zag(pos)
                elif gp.left==p and p.right==pos:
                    self.zig_zag(pos)
                else:
                    self.zag_zig(pos)
            
            elif p:
                if p.left==pos:
                    self.zig(pos)
                else:
                    self.zag(pos)
    
    def insert(self,item):
        if not self.isroot:
            self.root=Node(item)
            self.isroot=True
        else:
            ptr=self.root
            temp=None
            while ptr!=None:
                if item>ptr.data:
                    temp=ptr
                    ptr=ptr.right
                else:
                    temp=ptr
                    ptr=ptr.left
            if item>temp.data:
                temp.right=Node(item,parent=temp)
                self.splay(temp.right)
            else:
                temp.left=Node(item,parent=temp)
                self.splay(temp.left)

    def display(self):
        s=self.root
        def traversal(s):
            if s!=None:
                print('['+str(s.data),end='')
                traversal(s.left)
                traversal(s.right)
                print(']',end='')
        traversal(s)
        print()
    
    def inorder(self,pos):
        if pos:
            print(pos.data,end=' ')
            self.inorder(pos.left)
            self.inorder(pos.right)
        
l=[7,4,3,2,11,1,12,8,9,6,10,5]
s=Splay_tree()
for i in l:
    s.insert(i)
    s.inorder(s.root)
    print()
