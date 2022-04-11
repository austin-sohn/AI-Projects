from games import *
class GameOfNim(Game):
    def __init__(self, board):
        #GameState = namedtuple('GameState', 'to_move, utility, board, moves')
        moves = []
        for i in range (0,len(board)):
            for amt in range(1, board[i]+1):
                moves.append((i, amt))
        self.initial = GameState(to_move='MAX', utility=0, board=board, moves=moves)

    def result(self, state, moves): #assume move given is valid, return new state after move
        nboard = state.board.copy()
        nboard[moves[0]] = nboard[moves[0]] - moves[1]
        
        # moves_left = list(state.moves)
        # moves_left.remove(moves)
        # for i in range(0, len(nboard)):
        #     if(moves[0], i) in moves_left:
        #         moves_left.remove((moves[0], i))
        moves_left = []
        for i in range(0, len(nboard)):
            for amt in range(1, nboard[i] + 1):
                if nboard[i] != 0:
                    moves_left.append((i, amt))
        return GameState(to_move=('MIN' if state.to_move == 'MAX' else 'MAX'),
                         utility=self.utility(state, state.to_move),
                         board=nboard, moves=moves_left)

    def actions(self,state):  #return list of valid actions
        return state.moves

    def terminal_test(self,state): #returns true if given state is end of game
        #print(not self.actions(state))
        return not self.actions(state)

    def utility(self,state,player):
        if self.terminal_test(state):
            if player == 'MAX':
                return 1
            else:
                return -1
        return 0 

    def to_move(self, state):
        """Return the player whose move it is in this state."""
        return state.to_move

if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1])  # Creating the game instance
    #nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    print(nim.initial.board) # must be [0, 5, 3, 1]
    print(nim.initial.moves) # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2,1), (2, 2), (2, 3), (3, 1)]
    print(nim.result(nim.initial, (1,3)))
    utility = nim.play_game(alpha_beta_player, query_player) # computer moves first
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")
