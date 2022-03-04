# Austin Sohn
# wolfgoatcabbage.py
# 3/4/22

from search import *
class WolfGoatCabbage(Problem):
    def __init__(self, initial = frozenset({'F', 'W', 'G', 'C'}), goal = set()):
        super().__init__(initial, goal)

    def goal_test(self, state):
        goal = False
        if state == self.goal:
            goal = True
        return goal

    def result(self, state, action):
    # In result() you will have to return the next state as a frozenset since the search algorithms
    # require the state to be represented as a hashable data type.
        print(state)
        print(action)
        # assumes action is valid
        if action.issubset(state):
            state = state.difference(action)
        else:
            state = state.union(action)
        #froze_st = frozenset(state)
        #return froze_st
        return state

    def actions(self, state):
        act_list = []
        if state == {'F', 'W', 'G', 'C'}:
            act_list = [{'F', 'G'}]
        elif state == {'W', 'C'}:
            act_list = [{'F'}, {'F', 'G'}]
        elif state == {'F', 'W', 'C'}:
            act_list = [{'F', 'W'}, {'F', 'C'}]
        elif state == {'C'} or state == {'W'}:
            act_list = [{'F'}, {'F', 'G'}]
        elif state == {'G'}:
            act_list = [{'F'}, {'F', 'C'}, {'F', 'W'}]
        elif state == {'F', 'G', 'C'}:
            act_list = [{'F', 'C'}]
        elif state == {'F', 'W', 'G'}:
            act_list = [{'F', 'W'}]
        elif state == {'F', 'G'}:
            act_list == [{'F', 'G'}]
        return act_list

if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    # solution = breadth_first_graph_search(wgc).solution()
    # print(solution)
