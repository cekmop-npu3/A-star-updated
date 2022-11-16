# A-star-pathfinding-algorithm
Program for finding the shortest path

---

## Steps before start

1. Clone [repository](https://github.com/cekmop-npu3/A-star-updated):

```
git clone https://github.com/cekmop-npu3/A-star-updated/blob/main/pathfind.py
```

2. Insert the matrix in your code. Here is the example:

```
matrix = [['1', '1', '1', '1', '1', '1','1','1','1','1'],
          ['1', '0', '0', '0', '0', '0','0','0','0','1'],
          ['1', '0', '0', '0', '0', '0','0','0','0','1'],
          ['1', '0', '0', '0', '0', '1','0','0','0','1'],
          ['1', '0', '0', '0', '0', '1','0','0','0','1'],
          ['1', '0', '1', '1', '1', '1','0','0','0','1'],
          ['1', '0', '0', '0', '0', '0','0','0','0','1'],
          ['1', '0', '0', '0', '0', '0','0','0','0','1'],
          ['1', '0', '0', '0', '0', '0','0','0','0','1'],
          ['1', '1', '1', '1', '1', '1','1','1','1','1']
]
```

3. Before running the program you should put start and end points in the instance of AStar class:

```commandline
a_star = AStar(matrix, (1, 1), (8, 3))
```

4. Run [pathfind.py](https://github.com/cekmop-npu3/A-star-updated/blob/main/pathfind.py):

```
python pathfind.py
```

---

# Notes and sources

Special thanks to [Kyle Stone](https://www.youtube.com/watch?v=T8mgXpW1_vc) for good explanation of how it works
