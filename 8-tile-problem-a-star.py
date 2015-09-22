# Assignment 2
# 9 tile problem using A* Search with 'Manhattan Distance'.
# Online Compiler: www.codeskulptor.org. Uncomment line 8 & 9.


import random
import time
# import codeskulptor
# codeskulptor.set_timeout(30)


# Start time
t1 = time.time()


# Checks if the state is solvable or not. It's not necessary for an state to be solvable.
# Returns True or False for solvable or non-solvable respectively.
def isSolvable(state):
    state.remove('B')
    count = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] > state[j]:
                count += 1
    if count % 2 == 0:
        return True
    else:
        return False

    
# Generate a random initial state
# Returns the generated state
def generateInitialState():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 'B']
    random.shuffle(x)
    while isSolvable(list(x)) == False:
        random.shuffle(x)
    x = [x[i:i+3] for i in xrange(0, 9, 3)]
    x.append([])
    return x


# Compares current state and goal state. 'y' represents goal state.
# Returns True or False for equal or not equal.
def compareStates(x):
    if x[0:3] == GOAL_STATE:
        return True
    else:
        return False

    
# Determines index of 'B' in the state
# Returns index in the [i, j] format
def posB(x):
    for p in x:
        if 'B' in p:
            j = p.index('B')
            i = x.index(p)
            return [i, j]


# Sum of indices in [i, j] format
# Returns sum in [i, j] format
def sumIndex(x, y):
    p = [-1, -1]
    p[0] = x[0] + y[0]
    p[1] = x[1] + y[1]
    return p


# Generate a child from the given state 'x' by moving the 'B' as per stated in 'step'
# Returns the child state
def generateChild(x, step):
    addIndex = DICT_STEP.get(step)
    posOld = posB(x)
    posNew = sumIndex(posOld, addIndex)
    if (posNew[0] > 2) or (posNew[0] < 0) or (posNew[1] > 2) or (posNew[1] < 0):
        return False
    else:
        y = [list(p) for p in x]
        temp = y[posNew[0]][posNew[1]]
        y[posNew[0]][posNew[1]] = y[posOld[0]][posOld[1]]
        y[posOld[0]][posOld[1]] = temp
        y[3].append(step)
        return y
    

def manhattanDistance(state):
    mDistance = 0
    for i in range(3):
        for j in range(3):
            temp = POSITIONS[state[i][j]]
            mDistance += abs(temp[0] - i) + abs(temp[1] - j)
    return mDistance


# Main part of the code containing IDS algorithm
GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 'B']]
STEPS = ['U', 'R', 'D', 'L']
DICT_STEP = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
POSITIONS = {1:[0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0],
             5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 'B': [2, 2]}
achievedGoalNode = []

# randomInitialState = [[1, 2, 3], [4, 5, 6], ['B', 7, 8], []] #Depth: 2
# randomInitialState = [[1, 'B', 3], [4, 2, 5], [7, 8, 6], []] #Depth: 3
# randomInitialState = [[4, 1, 'B'], [8, 7, 3], [2, 6, 5], []] #Depth: 14
randomInitialState = [[8, 5, 'B'], [2, 3, 7], [1, 4, 6], []] #Depth: 18
# randomInitialState = generateInitialState()
print 'Initial State:'
for i in range(len(randomInitialState) - 1):
    print randomInitialState[i]
print


def aStarSearch(state):
    global achievedGoalNode
    fringeList = {}
    fringeList[manhattanDistance(state)] = [state]
    # print fringeList
    found = False
    while (not found):
        leastFValue = min(fringeList)
        print "Currently Expanding Node's F-Value:", leastFValue
        currentState = fringeList[leastFValue][0]
        if compareStates(currentState) == True:
            achievedGoalNode = currentState
            found = True
        else:
            for step in STEPS:
                childNode = generateChild(currentState, step)
                if childNode != False:
                    gValue = len(childNode[3])
                    hValue = manhattanDistance(childNode)
                    fValue = gValue + hValue
                    if fringeList.has_key(fValue):
                        fringeList[fValue].append(childNode)
                    else:
                        fringeList[fValue] = [childNode]
            if len(fringeList[leastFValue]) == 1:
                fringeList.pop(leastFValue)
            else:
                fringeList[leastFValue].pop(0)

            
aStarSearch(randomInitialState)
print
print 'Path Taken:', achievedGoalNode[3]
print 'Depth of Goal Node:', len(achievedGoalNode[3])
t2 = time.time()
print 'Time Taken:', t2 - t1
