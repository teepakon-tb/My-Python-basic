class Node :
    def __init__(self):
        self.information = None
        self.left = None
        self.right = None
    
    def insert(self, information): #ฟังชั่นการinputข้อมูล
        if information != " ": # เปลี่ยนฝั่ง
            self.information = information
        else:
            return 
    
        information = input("โปรดป้อนข้อความเพื่อจัดเก็บใน Left child ของ {} (ถ้าไม่มีให้ป้อนค่าช่องว่าง 1 ช่อง) : ".format(self.information))
        if information != " ":
            self.left = Node()
            self.left.insert(information)    
                    
        information = input("โปรดป้อนข้อความเพื่อจัดเก็บใน Right child ของ {} (ถ้าไม่มีให้ป้อนค่าช่องว่าง 1 ช่อง) : ".format(self.information))
        if information != " ":
            self.right = Node()
            self.right.insert(information)      

    def in_order(self, tree): #การแสดงผลข้อมูลที่อยู่ในtreeโดนใช้รูปแบบของin order
        if tree != None:
            self.in_order(tree.left)
            print(tree.information)
            self.in_order(tree.right)   

    def post_order(self, tree):#การแสดงผลข้อมูลที่อยู่ในtreeโดนใช้รูปแบบของpost order โดย จะแสดงข้อมูลที่เริ่มต้นด้วย a,e,i,o,u
        if tree == None:
            return
        self.post_order(tree.left)
        self.post_order(tree.right)
        if tree.information.startswith("a"): #เช็คว่าตัวอักษรของข้อมูลขึ้นต้นด้วย a ไหม
            print(tree.information)
        if tree.information.startswith("e"): #เช็คว่าตัวอักษรของข้อมูลขึ้นต้นด้วย e ไหม
            print(tree.information)    
        if tree.information.startswith("i"): #เช็คว่าตัวอักษรของข้อมูลขึ้นต้นด้วย i ไหม
            print(tree.information)  
        if tree.information.startswith("o"): #เช็คว่าตัวอักษรของข้อมูลขึ้นต้นด้วย o ไหม
            print(tree.information)
        if tree.information.startswith("u"): #เช็คว่าตัวอักษรของข้อมูลขึ้นต้นด้วย u ไหม
            print(tree.information)  
                        
tree = Node()
x = input("โปรดป้อนข้อความเพื่อจัดเก็บที่ Root node : ")
tree.insert(x)
print("ผลลัพธ์จากการท่องไปในต้นไม้ทวิภาคด้วยขั้นตอนวิธีแบบ In-order")
tree.in_order(tree)
print("ผลลัพธ์จากกการท่องงไปในต้นไม้ทวิภาคด้วยขั้นตอนวิธีแบบ Post-order โดยแสดงข้อความที่จัดเก็บในแต่ละโหนดที่ขึ้นต้นด้วยตัวอักษร a หรือ e หรือ i หรือ o หรือ u :")
tree.post_order(tree)