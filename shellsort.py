def shell_sort(arr, n): #กำหนด shell_sort ฟังก์ชั่นในการ sort
    flag = 1 #กำหนด flag เพื่อใช้ในการทำงานของ loop
    Gap_size = n #กำหนดตัวแปร Gap_size แทนค่า จำนวนข้อมูลที่นำเข้ามา
    while flag == 1 or Gap_size > 1: #กำหนด while loop เพื่อเช็คเงื่อน หาก flag = 1 หรือ Gap_size > 1 จะทำ
        flag = 0
        Gap_size = int((Gap_size + 1) / 2) #กำหนดตัวแปร Gap_size ใหม่เพื่อใช้ในการหารข้อมูลออกเป็นสองส่วน
        for i in range(n-Gap_size): #สร้าง loop เพื่อใช้ในการจัดเรียงข้อมูล
            if arr [i + Gap_size] < arr[i]: #เงื่อนไขในการ แทนค่าของข้อมูลที่จัดเรียง
                temp = arr[i + Gap_size] #กำหนดตัวแปรที่ใช้เก็บค่าที่มีค่าน้อยกว่า เพื่อไว้ด้านหน้า
                arr[i + Gap_size] = arr[i] # เปลี่ยนค่าของข้อมูลที่มีค่ามากกว่าข้อมูลที่จัดเรียงไว้ในตำแหน่งที่น้อยกว่านั้น
                arr[i] = temp #เปลี่ยนค่าของ index นั้นเป็นค่าที่น้อยที่สุด
                flag = 0 #กำหนดให้ flag เป็น 0 เพื่อหยุดการทำงานของ Loop

size = int(input("โปรดระบุจำนวนข้อมูลที่ต้องการเรียงลำดับ : "))
None_sort= [] #กำหนด list ในการเก็บข้อมูลก่อนจะทำการจัดเรียง
sort = [] #กำหนด list ในการเก็บข้อมูลหลังจะทำการจัดเรียง

print("โปรดป้อนข้อมูลที่ต้องการเรียงลำดับ")

for i in range(size): #กำหนด loop ในการเอาค่าเข้าไปเก็บใน list
    information = str(input('ข้อมูล : '))
    sort.append(information) #เพิ่มข้อมูลเข้าไปในlist โดยappend
    None_sort.append(information) #เพิ่มข้อมูลเข้าไปในlist โดยappend
    
shell_sort(sort,size) #ใช้ function ในการเรียง

print(" ข้อมูลก่อนเรียงลำดับ คือ")
print(*None_sort) #การprint ข้อมูล โดยการเอาก้ามปูออกโดยใช้ *
print(" ข้อที่เรียงลำดับจากน้อยไปมาก คือ")
print(*sort)#การprint ข้อมูล โดยการเอาก้ามปูออกโดยใช้ *