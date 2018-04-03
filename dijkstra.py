import sys

class Graph():
    def __init__(self):
        self.num_e = 0
        self.ve = {}

    def add(self, v1, v2, e):
        if v1 in self.ve:
            self.ve[v1].append((v2, e))
        else:
            self.ve[v1] = [(v2, e)]

        self.num_e += 1

    def get_neighbors(self, v):
        return self.ve[v]

    def get_dist(self, u, v):
        for edge in self.ve[u]:
            if edge[0] == v:
                return edge[1]

    def __str__(self):
        return str(self.ve)

def build_graph(fname):
    g = Graph()
    with open(fname) as f:
        n = f.readline()
        data = f.readlines();
        
        for line in data:
            v1 = line.split()[0]
            v2 = line.split()[1]
            e = int(line.split()[2])
            g.add(v1, v2, e)
    return g

class Vertices():
    def __init__(self):
        self.table = {}

    def add(self, v):
        self.table[v] = {'prev': '', 'dist': 99999}

    def remove(self, v):
        self.table.pop(v)

    def update_prev(self, v, new_prev):
        self.table[v]['prev'] = new_prev

    def update_dist(self, v, new_dist):
        self.table[v]['dist'] = new_dist

    def get_min(self):
        return min(self.table.items(), key=lambda x: x[1]['dist'])

    def get(self, v):
        return self.table[v]
    
    def empty(self):
        return len(self.table) == 0

    def contains(self, v):
        return v in self.table


def dijsktra(g, s):
    visited = []
    vertices = Vertices()
    for key in g.ve.keys():
        vertices.add(key)

    vertices.update_dist(s, 0)

    while not vertices.empty():
        v = vertices.get_min()
        vertices.remove(v[0])
        visited.append(v)

        for neighbor in g.get_neighbors(v[0]):
            if vertices.contains(neighbor[0]):
                total_dist = v[1]['dist'] + g.get_dist(v[0], neighbor[0])
                if total_dist < vertices.get(neighbor[0])['dist']:
                    vertices.table[neighbor[0]]['dist'] = total_dist
                    vertices.table[neighbor[0]]['prev'] = v[0]
    
    return visited

def main(fname):
    g = build_graph(fname)
    print(g)
    result = dijsktra(g, '1')
    print(result)

if __name__ == '__main__':
    main(sys.argv[1])









