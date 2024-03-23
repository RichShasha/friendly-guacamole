class Graph:
    edges = {}
    t = 0
    visited = []
    exitOreder = {}
    def __init__(self, edges):
        self.edges = edges
    def IDK(self):
        self.exitOrder = {}
        self.t = 0
        self.visited = []
        for k in self.edges:
            self.DFS1(k)
        print(self.exitOrder)
    def DFS1(self, v):
        if not v in self.visited:
            self.visited+=v
            self.t+=1
            for node in self.edges[v]:
                self.DFS1(node)
            self.t+=1
            self.exitOrder[v] = self.t 
            

class main:
    def __init__(self) -> None:
        edges = {
            'a':['g', 'b', 'f'],
            'b':[],
            'c':['d'],
            'd':['f', 'c'],
            'e':['d'],
            'f':['e'],
            'g':['e', 'j'],
            'h':['i', 'g'],
            'i':['h','j'],
            'j':['k', 'l'],
            'k':['m'],
            'l':['m'],
            'm':['j']
        }
        a = Graph(edges)
        a.IDK()

if __name__ == "__main__":
    main()