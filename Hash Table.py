class H_table:  
    def __init__(self, size): #ฟังชั่น
        self.size = [None]*size #กำหนดค่าให้ตารางแฮชทุกช่องเป็น None ก่อน  

    def append(self,key,data): #ฟังชั่น
        key = keys%size #ฟังชั่นที่ 1
        if self.size[key] is None:#จะทำต่อเมื่อ size[k] = None
            self.size[key] = data
            print ("Address = ",key)
        else:
            self.num = 0 # ตัวนับ
            while True:
                self.num += 1 # ตัวนับ
                k = (key + self.num)%size #ฟังชั่นที่ 2
                if self.size[k] is None: #จะทำต่อเมื่อ size[k] = None
                    self.size[k] = data
                    print("Address = ",k)
                    break
                else:
                    continue                                      
            
size = int(input("โปรดป้อนขนาดตารางแฮช: "))
ht = H_table(size)

while size + 1 : 
    keys = int(input("โปรดป้อนค่าคีย์ (key) ที่มีค่าตั้งแต่ 0 ขึ้นไป: ")) #ค่า key
    data = input("โปรดป้อนข้อมูล (data) เพื่อจัดเก็บข้อมูลในตารางแฮช: ") #ค่า data
    if keys < 0: #ถ้า key น้อยกว่า 0 ให้ทำ
        break
    else:
        ht.append(keys, data) # ใช้ฟังชั้น append
        
for n in range(size): 
    if ht.size[n] is None:
        print("Address = ", n," ไม่มีข้อมูลที่จัดเก็บ ")
    else:
        print("Address = ", n," ข้อมูลที่จัดเก็บคือ ", ht.size[n])