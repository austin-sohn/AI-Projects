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
        if state == {'F', 'W', 'G', 'C'}:
            state.remove('F','G')
        if state == {'W', 'C'}:
            state.add('F')
        if state == {'F', 'W', 'C'}:
            state.remove('F', 'W')
        if state == {'C'}:
            state.add('F', 'G')
        if state == {'F', 'G', 'C'}:
            state.remove('F', 'C')
        if state == {'G'}:
            state.add('F')
        if state == {'F', 'G'}:
            state.remove('F', 'G')
        froze = frozenset(state)
        return froze

    def actions(self, state):
        print(state)
        act_list = []
        if state == {'F', 'W', 'G', 'C'}:
            act_list = [{'F', 'W'}, {'F', 'G'}, {'F', 'C'}]
        if state == {'W', 'C'}:
            act_list = [{'F'}, {'F', 'G'}]
        if state == {'F', 'W', 'C'}:
            act_list = [{'F', 'W'}, {'F', 'C'}]
        if state == {'F', 'G', 'C'} or state == {'F', 'W', 'G'}:
            act_list = [{'F', 'W'}]
        if state == {'G'}:
            act_list = [{'F'}]
        if state == {'F', 'G'}:
            act_list == [{'F', 'G'}]
        return act_list

if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    # wgc.actions(wgc.state)
    # print(wgc.result)
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    # solution = breadth_first_graph_search(wgc).solution()
    # print(solution)
