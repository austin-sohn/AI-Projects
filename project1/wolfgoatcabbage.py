# Austin Sohn
# wolfgoatcabbage.py
# 3/4/22

from search import *
class WolfGoatCabbage():
    def __init__(self, initial, goal = {'F', 'G', 'W', 'C'}):
        super().__init__(initial, goal)

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
        froze_state = frozenset(state)
        return froze_state

    def actions(self, state):
        pot_act = {'F', 'G', 'W', 'C'}
        if 'F' in state:
            pot_act.remove('F')
        if 'G' in state:
            pot_act.remove('G')
        if 'W' in state:
            pot_act.remove('W')
        if 'C' in state:
            pot_act.remove('C')
        return pot_act

if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    """
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
    """
