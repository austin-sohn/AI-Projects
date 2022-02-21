# Austin Sohn
# wolfgoatcabbage.py
# 3/4/22

from search import *
def goal_test(state):

    return True
def result(state, action):
    newstate = state
    return newstate
def actions(state):
    act_list = []
    return act_list
def WolfGoatCabbage():

    return 1

if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)