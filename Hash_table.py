class H_table: # h ย่อมาจาก hash
    def __init__(self, size):
        self.size = ["/"]*size
        self.num = 0  #จำนวนครั้งที่เกิด Collision
    
    def append(self, key, data):       
        if self.size[key] is "/":
            self.size[key] = data
        else:
            print("จัดเก็บข้อมูลในตารางไม่ได้เพราะตำแหน่งดังกล่าวในตารางแฮชจัดเก็บข้อมูล", self.size[key])
            self.num = self.num + 1 #คำนวณจำนวนครั้งที่เกิด Collision 

size = int(input("โปรดป้อนขนาดตารางแฮช : "))#ขนาด hash table
ht = H_table(size)

while True:
    k = int(input("โปรดป้อนคำ (key) ที่มีค่าตั้งแต่ 0 ขึ้นไป : "))
    d = input("โปรดป้อนข้อมูล (data) เพื่อจัดเก็บข้อมูลในตารางแฮช : ")
    if k < 0 : #ถ้าน้อยกว่า 0 ให้ทำ
        break
    ht.append(k % size, d) #mod

for n in range (size):
    if ht.size[n] is "/":
        print("index",n,", ไม่มีข้อมูลจัดเก็บ")
    else:
        print("index",n,", ข้อมูลคือ", ht.size[n])
print ("จำนวนครั้งที่เกิด Collision = ", ht.num)