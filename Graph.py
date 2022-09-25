import math

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self): #เช็คว่าว่างไหม
        return self.items == []

    def enqueue(self, item): #เพิ่มค่า
        self.items.insert(0, item)

    def dequeue(self): #ลดค่า
        return self.items.pop()

class Vertex:
    def __init__(self, data):
        self.id = data
        self.distance = math.inf
        self.color = 'white'
        self.pred = None
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0): 
        self.connectedTo[nbr] = weight

    def setColor(self, color):
        self.color = color

    def setDistance(self, d):
        self.distance = d

    def setPred(self, p):
        self.pred = p

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getPred(self):
        return self.pred

    def getDistance(self):
        return self.distance

    def getColor(self):
        return self.color

class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0

    def addVertex(self, key): #add ค่า Vertex
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex

    def getVertex(self, n): 
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertices

    def addEdge(self, f, t):
        if f not in self.vertices:
            nv = self.addVertex(f)
        if t not in self.vertices:
            nv = self.addVertex(t)
        self.vertices[f].addNeighbor(self.vertices[t])

    def getVertices(self):
        return list(self.vertices.keys())

    def __iter__(self):
        return iter(self.vertices.values())

    def bfs(self,start):
        s = self.getVertex(start)
        s.setDistance(0)
        s.setPred(None)
        q = Queue()
        q.enqueue(s)
        while not(q.isEmpty()):
            currentVertex = q.dequeue()
            for nbr in currentVertex.getConnections():
                if (nbr.getColor() == 'white'):
                    nbr.setColor('gray')
                    nbr.setDistance(currentVertex.getDistance() + 1)
                    nbr.setPred(currentVertex)
                    q.enqueue(nbr)
                    print('ระยะทางที่สั้นที่สุดจากจุดเริ่มต้นในการท่องไปในกราฟไปยังจุด ', nbr.getId(), ' = ', nbr.getDistance())
            currentVertex.setColor('black')

n = Graph()
num = int(input("โปรดระบุจำนวนจุดในกราฟ: "))
count = 0

while count < num: #จะทำต่อเมื่อnumมากกว่า count
    namevertex = input("โปรดระบุชื่อ Vertex: ")
    n.addVertex #เรียกใช้ฟังชั่น addVertex
    count = count + 1

print("โปรดระบุชื่อจุดที่เป็น source และ destination ชองเส้นเชื่อม source")
Source = input("Source = ")
Destination = input("Destination = ")
while Source is not "-" and Destination is not "-": #จะทำหากsourceและDestinationไม่ใช่ -
    n.addEdge(Source,Destination) #เรียกใช้ฟังชั่น addEdge
    print("โปรดระบุชื่อจุดที่เป็น source และ destinnation ของเส้นเชื่อม source")
    Source = input("Source = ")
    Destination = input("Destination = ")

print("โปรดระบุชื่อจุดที่เป็นจุดเริ่มต้นในการท่องไปในกราฟด้วยขั้นตอนวิธีแบบ Breadth-first Search")
beginning = input("ชื่อจุดที่เป็นจุดเริ่มต้นในการท่องไปในกราฟ = ")
n.bfs(beginning)