class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self): 
        self.head = None
        self.tail = None
    
    def insert_beginning(self,data): #เพิ่มค่าเข้าlink list ในตำแหน่งแรกสุด
        if self.head == None:
            new_node = Node(data)
            self.next = None
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head 
            self.head = new_node

    def insert_last(self,data): #เพิ่มค่าเข้าlink list ในหลังสุด
        if self.head == None:
            new_node = Node(data)
            self.next = None
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node

    def remove_beginning(self): #เอาค่าแรกสุดใน linklist ออก
        if self.head == None:
            print("ไม่สามารถลบข้อมูลได้เพราะ Linked List ว่าง")
        else:
            self.head = self.head.next

    def remove_last(self): #เอาค่าสุดท้ายออกจากlink list
        if self.tail == None:
            print("ไม่สามารถลบข้อมูลได้เพราะ Linked List ว่าง")
        elif self.tail == self.head :
            self.head = None
            self.tail = None
        else:    
            tmp = self.head
            while tmp.next != self.tail:
                tmp = tmp.next
            self.tail = tmp
            self.tail.next = None

    def remove(self, data): #ลบค่าที่ต้องการ
        if self.head == None:
            print("ไม่สามารถลบข้อมูลได้เพราะ Linked List ว่าง")
        else:
            tmp = self.head
            prev = self.head
            if tmp.data == data:
                self.head = self.head.next
                return
            elif self.tail.data == data:
                self.remove_beginning()
                return
            if tmp.data != data:
                print("ไม่มีข้อมูลที่ต้องการลบใน Linked list")
                self.remove_last()
                return
            while tmp.data != data:
                prev = tmp
                tmp = tmp.next
            prev.next = tmp.next

    def Display(self): #แสดงค่าในlink list
        if self.head == None:
            print("ไม่สามารถแสดงข้อมูลได้เพราะ Linked List ว่าง")
        if self.head != None:
            print("Head = {} Tail = {}".format(x.head.data,x.tail.data))
            tmp = self.head
            while tmp == None:
                print("ข้อมูลที่จัดเก็บ = {}".format(tmp.data))
                tmp = tmp.next
                
x = Linked_list() #กำหนดตัวแปรแทนlink list
print("โปรดระบุทางเลือกในการดำเนินการกับ Singly linked list")
print("1. เพิ่มข้อมูลที่จุดเริ่มต้น Linked list")
print("2. เพิ่มข้อมูลที่สิ้นสุด Linked list")
print("3. ลบข้อมูลที่จุดเริ่มต้น Linked list")
print("4. ลบข้อมูลที่จุดสิ้นสุด Linked list")
print("5. ลบข้อมูลที่ระบุจาก Linked list")
print("6. แสดงข้อมูลที่จัดเก็บทั้งหมดใน Linked list ทางจอภาพ")
choose = 1
while choose > 0 and choose < 7 : #จะทำต่อเมื่อchoose มากกว่า 0 และ น้อยกว่า 7
    choose = int(input("ทางเลือกในการดำเนินการ = "))
    if choose == 1:  
        n = int(input("ข้อมูลที่ต้องการเพิ่มที่จุดเริ่มต้น Singly linked list : "))
        x.insert_beginning(n) #เรียกใช้ฟังชั่น
    elif choose == 2:
        n = int(input("ข้อมูลที่ต้องการเพิ่มที่จุดเริ่มต้น Singly linked list : "))
        x.insert_last(n) #เรียกใช้ฟังชั่น
    elif choose == 3:
        x.remove_beginning() #เรียกใช้ฟังชั่น
    elif choose == 4:
        x.remove_last() #เรียกใช้ฟังชั่น
    elif choose == 5:
        d = int(input("ข้อมูลที่ต้องการลบ Singly linked list : "))
        x.remove(d) #เรียกใช้ฟังชั่น
    elif choose == 6:
        x.Display() #เรียกใช้ฟังชั่น