# Austin Sohn
# wolfgoatcabbage.py
# 3/11/22

from search import *
class WolfGoatCabbage(Problem):
    def __init__(self, initial = frozenset({'F', 'W', 'G', 'C'}), goal = set()):
        super().__init__(initial, goal)

    def goal_test(self, state):
        return state == self.goal

    def result(self, state, action):
    # In result() you will have to return the next state as a frozenset since the search algorithms
    # require the state to be represented as a hashable data type.
        # assumes action is valid
        if action.issubset(state):
            state = state.difference(action)
        else:
            state = state.union(action)
        froze_st = frozenset(state)
        return froze_st

    def actions(self, state):
            act_list = []
            if state == {'F', 'W', 'G', 'C'}:
                act_list = [{'F', 'G'}]
            if state == {'W', 'C'}:
                act_list = [{'F'}, {'F', 'G'}]
            if state == {'F', 'W', 'C'}:
                act_list = [{'F', 'W'}, {'F', 'C'}, {'F'}]
            if state == {'C'}:
                act_list = [{'F', 'W'}, {'F', 'G'}]
            if state == {'W'}:
                act_list = [{'F', 'G'}, {'F', 'C'}]
            if state == {'F', 'G', 'C'}:
                act_list = [{'F', 'C'}, {'F', 'G'}]
            if state == {'F', 'W', 'G'}:
                act_list = [{'F', 'W'}, {'F', 'G'}]
            if state == {'G'}:
                act_list = [{'F'}, {'F', 'W'}, {'F', 'C'}]
            if state == {'F', 'G'}:
                act_list == [{'F'}, {'F', 'G'}]
            return act_list

if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
