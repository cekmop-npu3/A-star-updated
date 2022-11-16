class AStar:
    def __init__(self, matrix, start_pos, end_pos):
        self.matrix = matrix
        self.stp = start_pos
        self.ep = end_pos
        self.open_list = dict()
        self.close_list = dict()
        self._calc(self.stp, [0, 0, 0, self.stp])

    def _calc(self, point, prop):
        self.close_list[point] = prop
        for x in range(point[0] - 1, point[0] + 2):
            for y in range(point[1] - 1, point[1] + 2):
                if (x, y) not in self.close_list and self.matrix[y][x] != '1':
                    Hcost = sorted([abs(x-self.ep[0]), abs(y-self.ep[1])])[0]*14 + abs(abs(x-self.ep[0]) - abs(y-self.ep[1]))*10
                    if (x, y) in self.open_list.keys():
                        if prop[1] + (14 if abs(x - point[0]) - abs(y - point[1]) == 0 else 10) <= self.open_list.get((x, y))[1]:
                            Gcost, point1 = prop[1] + (14 if abs(x - point[0]) - abs(y - point[1]) == 0 else 10), point
                        else:
                            Gcost, point1 = self.open_list.get((x, y))[1], self.open_list.get((x, y))[3]
                    else:
                        Gcost, point1 = prop[1] + (14 if abs(x - point[0]) - abs(y - point[1]) == 0 else 10), point
                    self.open_list[(x, y)] = [Hcost, Gcost, Hcost + Gcost, point1]

        try:
            pointed = sorted(list(self.open_list.items()), key=lambda x: x[1][2])[0]
            if pointed[0] != self.ep:
                del self.open_list[pointed[0]]
                self._calc(*pointed)
            else:
                self.close_list[pointed[0]] = pointed[1]
                self._path(self.close_list, self.ep)
        except IndexError: print('No way')

    def _path(self, path, key):
        print(key)
        if path.get(key)[3]!=self.stp:
            new_key = path.get(key)[3]
            del path[key]
            self._path(path, new_key)

a_star = AStar(matrix, '(start_pos)', '(end_pos)')