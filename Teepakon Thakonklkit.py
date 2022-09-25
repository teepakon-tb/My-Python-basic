class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVL_Tree():
    def getHeight(self, root): #ฟังชั่นคำสั่งรส่วนสูงของต้นไม้
        if not root:
            return 0
        return root.height

    def getBalance(self, root): #ฟั่งชั้นbalance tree
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)


    def leftRotate(self, z): 
        y = z.right
        x = y.left
        y.left = z
        z.right = x
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        x = y.right
        y.right = z
        z.left = x 
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right)) 
        return y

    def insert(self, root, key): #ฟังชั่นคำสั่งเพิ่มข้อมูล        
        if not root:
            return Node(key)
        elif key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
 
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        balance = self.getBalance(root)
        if balance > 1 and key < root.left.data:
            return self.rightRotate(root)      
        if balance > 1 and key > root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and key < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        if balance < -1 and key > root.right.data:
            return self.leftRotate(root)
        return root

    def Preorder(self, root): #ฟังชั่นคำสั่งพรีออเดอร์
        if root:
            print(root.data, end = " ") 
            self.Preorder(root.left)
            self.Preorder(root.right)

AVL = AVL_Tree()
balance_tree = None
while True:
    information = int(input("โปรดป้อนจำนวณเต็มเพื่อสร้าง AVL tree : "))
    if information != int(9999): #ถ้า information ไม่เท่ากับ 9999 จะทำงาน
        balance_tree = AVL.insert(balance_tree, information)
    else:
        break    
print("ผลลัพธ์จากการท่องไปใน AVL tree ด้วยขันตอนวิธีเเบบ Pre-order")
AVL.Preorder(balance_tree)
