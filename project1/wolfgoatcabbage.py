# Austin Sohn
# wolfgoatcabbage.py
# 3/4/22

from search import *
class WolfGoatCabbage():
    def __init__(self, initial = {'F', 'G', 'W', 'C'}, goal = {}):
        self.initial = initial
        self.goal = goal
        self.state = initial

    def goal_test(self, state):
        goal = False
        if state == self.goal:
            goal = True
        else:
            goal = False
        return goal

    def result(self, state, action):
    # In result() you will have to return the next state as a frozenset since the search algorithms
    # require the state to be represented as a hashable data type.
        if state == {'F', 'G', 'W', 'C'}:
            state.remove('W','C')
        if state == {'G', 'F'}:
            state.remove('G')
        froze = frozenset(state)
        return froze

    def actions(self, state):
        print(state)
        act_list = []
        return act_list

if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    wgc.actions(wgc.state)
    """
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
    """
