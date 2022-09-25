Mystack = int(input("โปรดระบุขนาดของ stack เป็นจำนวนเต็มที่มีค่ามากกว่า 0 : "))
while Mystack <= 0:
    Mystack = int(input("โปรดระบุขนาดของ stack เป็นจำนวนเต็มที่มีค่ามากกว่า 0 : "))
stack_size = [] * Mystack

def isEmpty(): #ฟังชั่น is empty เพื่อเช็คว่าstack ว่างไหม
    if len(stack_size) == 0:
        return 1
    else:
        return 0

def isFull():#ฟังชั่น isfullเพื่อเช็คว่าstackเต็มไหม
    if len(stack_size) == Mystack:
        return 1
    else:
        return 0

def push() :#ฟังชั่น push เพื่อเพิ่มค่า
    if isFull() == 0:
        stack_size.append(int(input("ข้อมูลที่ต้องการจัดเก็บใน stack = ")))
    else:
        print ("ไม่สามารถจัดเก็บข้อมูลใน stack ได้เพราะ stack เต็ม")

def pop():#ฟังชั่น pop เพื่อดึงข้อมูลล่าสุดออก
    if isEmpty() == 1:
        print("ไม่สามารถดึงข้อมูลออกจาก stack เพราะไม่มีข้อมูลจัดเก็บใน stack")
    return stack_size.pop()

def top():#ฟังชั่นtop แสดงค่าสูงสุดของ stack
    if isEmpty() == 1:
        print("ไม่สามารถแสดงค่า Top of Stack เพราะไม่มีข้อมูลจัดเก็บใน stack")
    else :
        print("Top of stack =",(stack_size[-1]))

def display():#ฟังชั่น display เพื่อแสดงค่าของstack
    if isEmpty() == 1 :
        print("ไม่สามารถจัดเก็บข้อมูลใน stack ได้เพราะไม่มีข้อมูลใน stack")
    else :
        sum = 0 #คิดค่าเฉลี่ย
        for x in stack_size:
            sum = sum + x #คิดค่าเฉลี่ย
            average = sum / len(stack_size) #คิดค่าเฉลี่ย
        print("ทางเลือกการดำเนินการ = 4")
        print("ข้อมูลที่จัดเก็บทั้งหมด = ",(stack_size))
        print("ค่ามากที่สุด = ",(max(stack_size)))
        print("ค่าน้อยที่สุด = ",(min(stack_size)))
        print("ค่าเฉลี่ยของข้อมูลที่จุดเก็บใน Stack = ",(average))

print("1. PUSH")
print("2. POP")
print("3. Top of Stack")
print("4. Display ข้อมูลที่จัดเก็บใน stack, ค่ามากที่สุด, ค่าน้อยที่สุด และค่าเฉลี่ยของข้อมูลที่จัดเก็บใน Stack")

choose = 1
while choose > 0 and choose < 5:
    choose = int(input("โปรดระบุทางเลือกสำหรับดำเนินการ stack : "))
    if choose == 1:
        push()

    elif choose == 2:
        pop()

    elif choose == 3:
        top()

    elif choose == 4:
        display()
        break