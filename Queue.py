class Queue:
    def __init__(self,n): #สร้างqueue
        self.n = n
        self.queue = [] * n
        self.front = -1
        self.rear = -1

    def enqueue(self,item): #เพิ่มค่าเข้าqueue
        if self.rear == self.n-1:
            print("Queue เต็ม")
        else:
            if len(self.queue) == 0:
                self.queue.append(item)
                self.front = 0
                self.rear = 0
            else:
                self.rear = self.rear + 1
                self.queue.append(item)

    def dequeue(self): #ลดค่าแรกในqueue
        if self.length() == 0:
            print("Queue ว่าง")
        else:
            self.queue[self.front] = None
            self.front = self.front+1

    def length(self):
        return len(self.queue)
    
    def display(self): # แสดง
        if len(self.queue) == 0:
            print("Queue ว่าง")
        else:
            print(self.queue)

n = int(input("โปรดระบุขนาดของ Queue = "))
while n <= 0:
    n = int(input("โปรดระบุขนาดของ Queue = "))
size = Queue(n) #ขนาดของ Queue

print("โปรดระบุทางเลือกในการดำเนินการกับ queue")
print("1. รับข้อมูลจำนวนเต็มจัดเก็บใน queue")
print("2. ดึงข้อมูลจาก queue 1 ช่อง")
print("3. แสดงข้อมูลที่อยู่ใน queue ทั้งหมดออกทางจอภาพ")

choose = 1
while choose > 0 and choose < 4 : #กำหนดเงื่อนไขในการทำงาน
    choose = int(input("ทางเลือกในการดำเนินการ = ")) #รับค่าผ่านทางแป้นพิมพิ์ 
    if choose == 1:  
        x= int(input("ข้อมูลที่ต้องการจัดเก็บข้อมูลใน queue = "))
        size.enqueue(x)
        print("ข้อมูลที่ต้องการเพิ่ม : {}".format(x))
    
    elif choose == 2:
        size.dequeue()
    elif choose == 3:
        size.display()
    elif choose > 3 :
        aggregate = 0
        list_None = []
        for i in size.queue:
            if i != None: 
                aggregate += i
                list_None.append(i)
        print("ผลรวม = {}".format(aggregate))
        sum = 0
        for k in list_None:
            if k > 200:
                sum = sum + 1
        print("จำนวนตัวเลขจำนวนเต็มที่มีค่ามากกว่า 200 = {}".format(sum))
        print("จบการทำงาน")
        break

