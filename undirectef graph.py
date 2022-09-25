class Graph: #ชื่อ คลาส
    def __init__(self,vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w): # self.graph เป็นการจัดเก็บข้อมูลเส้นเชื่อมด้วย list ของเส้นเชื่อมที่มี 3 ค่า คือ u,v,w โดย u คือ source, v คือ destination, w คือ weight
        self.graph.append([u, v, w]) #เมื่อมีการเพิ่มเส้นเชื่อมจะมีการเพิ่มข้อมูลใน List

    def find_set(self, parent, i):
        if i != parent[i]:
            parent[i] = self.find_set(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        x = self.find_set(parent, x)
        y = self.find_set(parent, y)
        if rank[x] < rank[y]:
            parent[x] = y 
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] = rank[x] + 1
#Kruskal
    def kruskal(self):
        A = []
        self.graph = sorted(self.graph, key= lambda item: item[2])
        parent = []
        rank =[]
        for vertex in range(self.V):
            parent.append(vertex)
            rank.append(0)
        i = 0
        e = 0
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find_set(parent,u)
            y = self.find_set(parent, v)
            if x != y:
                e = e + 1
                A.append([u, v, w])
                self.union(parent, rank, x, y)
        return A # return ค่า A

num = int(input("โปรดระบุค่าตัวแปร n (จำนวนจุดในกราฟแบบไม่มีทิศทาง (undirectef graph)) : "))
x = Graph(num)
edge = int(input("โปรดระบุจำนวนเส้นเชื่อม (Edge) ในกราฟแบบไม่มีทิศทาง : "))
print("โปรดระบุชื่อจุดที่เป็น Source ชื่อจุดที่เป็น Destination และค่าน้ำหนัก (Weight) ของเส้นเชื่อมในกราฟ")
for g in range(edge):
    u = int(input("Source = "))
    v = int(input("Destination = "))
    w = int(input("Weight = "))
    x.addEdge(u, v, w) #ใช้ฟังชั้น addedge 
k = x.kruskal() # ใช้ฟังชั่น kruskal 
s = 0
for u,v,w in k:
    s += w
    print("เส้นเชื่อมระหว่างจุด {} กับจุด {} มีค่าน้ำหนัก = {}".format(u, v, w))
print("Weight รวมของ Minimum spanning tree คือ {}".format(s))