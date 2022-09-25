def BubbleSort(array):

  for i in range(len(array)): #ลูปที่ใช้ในการอ่านค่า
    
    for j in range(0, len(array) - i - 1): 
      
      # การเปรียบเทียบข้อมูลที่อยู่ในตำแหน่งที่ j กับ j+1 ถ้าข้อมูลที่อยู่ในตำแหน่งที่ j มากกว่าข้อมูลที่อยู่ในตำแหน่งที่ j+1 จะทำการสลับ
      if array[j] > array[j + 1]:
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


number = int(input("โปรดระบุจำนวนข้อมูลที่ต้องการเรียงลำดับ : "))
size = [] #กำหนด list ในการเก็บข้อมูลหลังจะทำการจัดเรียง
before = []

for i in range(number): #กำหนด loop ในการนำค่าเข้าไปเก็บใน list
    data = int(input("ข้อมูล : "))
    size.append(data) 
    before.append(data)

BubbleSort(size) #ใช้ function ในการจัดเรียง
print(" ข้อมูลก่อนเรียงลำดับ คือ")
print(*before) #การprint ข้อมูล โดยการเอาวงเล็บก้ามปูออกโดยใช้ * 
print(" ข้อที่เรียงลำดับจากน้อยไปมาก คือ")
print(*size) #การprint ข้อมูล โดยการเอาวงเล็บก้ามปูออกโดยใช้ * 