class Node :
    def __init__(self):
        self.information = None
        self.left = None
        self.right = None
    
    def insert(self, information): #ฟังชั่นการinputข้อมูล
        if self.information == None:
            self.information = information
        elif information < self.information:
            if self.left == None:
                self.left  = Node()
                self.left.information  = information
            else:
                self.left.insert(information)
        elif information > self.information:
            if self.right == None:
                self.right  = Node()
                self.right.information  = information
            else:
                self.right.insert(information)    

    def post_order(self, tree):#การแสดงผลข้อมูลที่อยู่ในtreeโดนใช้รูปแบบของpost order โดย จะแสดงข้อมูลที่เริ่มต้นด้วย a,e,i,o,u
        if tree == None:
            return
        self.post_order(tree.left)
        self.post_order(tree.right)
        print(tree.information, end= " ")
    
    def findMaximumValue(self): #หาค่ามากที่สุดใน tree
        if self.right == None:
            return self.information
        return self.right.findMaximumValue()


tree = Node()
print ("โปรดป้อนจำนวนเต็มเพื่อจัดเก็บใน Binary search tree ถ้าไม่ต้องการเพิ่มข้อมูลอีกให้ป้อนเลข 12345")
largest = 0
while True:
    information = int(input('ข้อมูล = '))
    if information != 12345:
        tree.insert(information)
        largest = information
    else:
        break
    tree.findMaximumValue



print("ผลลัพธ์จากการท่องไปใน Binary search tree ด้วยขั้นตอนวิธีแบบ Post-order")
tree.post_order(tree)
print("\nจำนวนเต็มที่มากที่สุดจัดเก็บใน Binary search tree คือ ", tree.findMaximumValue())