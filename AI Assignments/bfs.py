LEFT_JUG_CAPACITY = 4
RIGHT_JUG_CAPACITY = 3

GOAL = [0,  2] 
RESULT = []

def empty_left(jugs): 
    return {'left' : 0, 'right' : jugs['right']}

def empty_right(jugs): 
    return {'left' : jugs['left'], 'right' : 0}

def fill_left(jugs):
    return {'left' : LEFT_JUG_CAPACITY, 'right' : jugs['left']}

def fill_right(jugs):
    return {'left' : jugs['left'], 'right' : RIGHT_JUG_CAPACITY}

def transfer_left_to_right(jugs):
    allowed_space = min(RIGHT_JUG_CAPACITY - jugs['right'],  jugs['left']) 
    return {'left' : jugs['left'] - allowed_space, 'right' : jugs['right'] + allowed_space}

def transfer_right_to_left(jugs):
    allowed_space = min(LEFT_JUG_CAPACITY - jugs['left'],  jugs['right']) 
    return {'left' : jugs['left'] + allowed_space, 'right' : jugs['right'] - allowed_space}

def possible_actions(jugs): 
    actions = {transfer_left_to_right, transfer_right_to_left, empty_left, empty_right, fill_left, fill_right}
 
    if  jugs['left']  ==  0:
        actions.remove(empty_left) 
        actions.remove(transfer_left_to_right)

    elif jugs['left'] == LEFT_JUG_CAPACITY:
        actions.remove(fill_left) 
        actions.remove(transfer_right_to_left)
 
    if  jugs['right']  ==  0:
        actions.remove(empty_right)
        try:
            actions.remove(transfer_right_to_left) 
        except KeyError: 
            pass

    elif jugs['right'] == RIGHT_JUG_CAPACITY:
        actions.remove(fill_right)
        try:
            actions.remove(transfer_left_to_right) 
        except KeyError: 
            pass

    return actions

def get_action_name(operation) -> str: 
    return {
    fill_left:  'fill  left  jug', fill_right:  'fill  right  jug', empty_left:  'empty  left  jug', empty_right:  'empty  right  jug',
    transfer_left_to_right:  'pour  left  jug  into  right  jug', transfer_right_to_left:  'pour  right  jug  into  left  jug'}[operation]

def is_goal(node):
    return list(node.jugs.values()) == GOAL

class Node:
    def __init__(self, jugs : dict, parent = None, action: str = None):
        self.jugs = jugs
        self.parent = parent
        self.action = action

def expand(node):
    for action in possible_actions(node.jugs):
        child = Node(action(node.jugs), node, get_action_name(action))
        yield child

def bfs(initial:  Node): 
    frontier = [initial]
    reached = [list(initial.jugs.values())]
    closed = []
    level =  1

    while len(frontier) != 0:
        print(f"\tStep {level}\t".center(40,  '-')) 
        print("Open List:  ", [list(item.jugs.values()) for item in frontier] )
        print("Closed List:  ", closed,  end='\n\n')
        node = frontier.pop(0)
        for child in expand(node):
            if is_goal(child):
                return child
            if list(child.jugs.values()) not in reached:
                reached.append(list(child.jugs.values()))
                frontier.append(child)
        closed.append(list(node.jugs.values()))
        level += 1
    return None


def main():
    initial = Node(jugs = {'left': 0, 'right' : 0})
    goal = bfs(initial)
    if goal:
        print("=" * 40) 
        print("Goal State : ", GOAL)
        print("The solution path is") 
        path = []
        operations = [] 
        while goal.parent:
            path.append(goal.jugs) 
            operations.append(goal.action) 
            goal = goal.parent

        path = list(reversed(path))
        operations = list(reversed(operations)) 
        print("Initial State => (0,  0)")
        for i,  _ in enumerate(path):
            print(f'Step {i + 1} {operations[i].ljust(35)} => {tuple(path[i].values())}')
    else:
        print("Could  not  reach  the  goal ",  GOAL)

if __name__ == '__main__':
    main()
