# 原始版本作者：Gao Minquan@Kaikeba
# Date：2021.6.28
# 要求：给定两个杯子的容量(X,Y)和要求得到的水量goal，求操作
# 思想：遍历所有可能的操作，直至得到goal。遍历方法：每一步允许的操作称作子路径，每个子路径下又有新一层子路径，
# 类似树形结构，逐层遍历该树即可。

# 导入ic方便调试
from icecream import ic

# 定义操作，只要输入初始水量(x,y)和杯子容量(X,Y)，就返回相应的6种操作
def successors(x, y, X, Y):
    return {
        (0, y): '倒空x',
        (x, 0): '倒空y',
        (x + y - Y, Y) if x + y >= Y else (0, x + y): 'x倒入y中',
        (X, x + y - X) if y + x >= X else (x + y, 0): 'y倒入x中',
        (X, y): '装满x',
        (x, Y): '装满y'
    }

# 根据给定的杯子容量、目标水量和初始水量，计算解决方案
def search_solution(capacity1, capacity2, goal, start=(0, 0)):
    paths = [ [('init', start)] ]

    explored = set() # 用于存放两杯水的历史状态

    while paths:
        path = paths.pop(0) # 把第一条子路径拿出来
        frontier = path[-1]
        (x,y) = frontier[-1]

        for state, action in successors(x, y, capacity1, capacity2).items():
            # ic(frontier, state, action)
            if state in explored: continue # 若操作完的状态存在于历史状态中，则不进行该步操作

            new_path = path + [ (action, state) ] # 记录操作步骤

            if goal in state:
                return new_path
            else:
                paths.append(new_path)

            explored.add(state)
            # ic(explored)
    return None


if __name__ == '__main__':
    path = search_solution(90, 40, 70, (0, 0))

    for p in path:
        print('--=>')
        print(p)

