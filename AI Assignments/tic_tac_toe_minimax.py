import time
from numpy import Infinity

class Game():

    def __init__(self, ai_choice, human_choice, *args):
        self.human_choice = human_choice
        self.ai_choice = ai_choice
        if len(args) == 0:
            self.board = [0, 0, 0,
                          0, 0, 0,
                          0, 0, 0]
        else : 
            self.board = args[0]
            
    def display_board(self):
        """
        Prints the board on console
        """
        chars = {
            -1: self.human_choice,
            +1: self.ai_choice,
            0: ' '
        }
        line = '---------'
        print(f'''\n{line}\n{chars[self.board[0]]} | {chars[self.board[1]]} | {chars[self.board[2]]}\n{line}\n{chars[self.board[3]]} | {chars[self.board[4]]} | {chars[self.board[5]]}\n{line}\n{chars[self.board[6]]} | {chars[self.board[7]]} | {chars[self.board[8]]}\n{line}\n''')

    def wins(self, state, player):
        """
        Tests and returns true if a specific player wins, else returns false
        """
        win_state = [
            [state[0], state[1], state[2]],    #rows
            [state[3], state[4], state[5]],
            [state[6], state[7], state[8]],
            [state[0], state[3], state[6]],    #columns
            [state[1], state[4], state[7]],
            [state[2], state[5], state[8]],
            [state[0], state[4], state[8]],    #diagonals
            [state[2], state[4], state[6]],
        ]
        if [player, player, player] in win_state:
            return True
        else:
            return False

    def utility(self, state, player):
        """
        Returns utility of the game/board state for the AI
        """
        if player == AI :
            if self.wins(state, AI):
                return {'score': +10 }
            elif self.wins(state, HUMAN):
                return {'score': -10 }
            else:
                return {'score': 0 }
        else :
            if self.wins(state, AI):
                return {'score': -10 }
            elif self.wins(state, HUMAN):
                return {'score': +10 }
            else:
                return {'score': 0 }

    def actions(self, state):
        """
        Returns a list of empty cells on the board
        """        
        cells = []
        for index in range(len(state)):
            if state[index] == 0:
                cells.append(index)
        
        return cells

    def terminal(self, state):
        """
        Returns true if there are no empty cells on the board
        """
        return self.actions(state) == [] or self.wins(state, AI) or self.wins(state, HUMAN)

    def valid_move(self, index):
        """
        Returns true if the move is valid
        """
        return index in self.actions(game.board)


def minimax(current_board, player,type = 'normal'):
    global game, current_player, scores
    available_cells = game.actions(current_board)

    if game.terminal(current_board):
        utility = game.utility(current_board, current_player)
        if type != 'normal':
            game.display_board()
            print(f'Terminal state. Utility {utility["score"]} is passed above.')
        return utility

    moves = []
    for cell in available_cells:
        move = {'cell': cell}
        current_board[cell] = player

        if player == AI:
            move['score'] = minimax(current_board, HUMAN, type)['score']
        else:
            move['score'] = minimax(current_board, AI, type)['score']

        current_board[cell] = 0
        moves.append(move)

    scores[0:9] = ['NA'] * 9
    
    if player == current_player:    #max player
        best_score = -Infinity
    
        for move in moves:
            scores[move['cell']] = move['score']
            if move['score'] > best_score:
                best_score = move['score']
                best_move = move

    else:   #min player
        best_score = +Infinity
    
        for move in moves:
            scores[move['cell']] = move['score']
            if move['score'] < best_score:
                best_score = move['score']
                best_move = move
    
    if type != 'normal':
        print('State :')
        game.display_board()
        print(f'received {list(filter(lambda s: s != "NA",scores))} from its childen and chose value {best_move["score"]}')
    return best_move

def ai_turn(type = 'normal'):
    global game, scores, current_player
    current_player = AI

    print(f'Computer turn [{game.ai_choice}]')
    move = minimax(game.board, AI, type)

    print(f'Minimax values of the available positions :\n[{scores[0]}, {scores[1]}, {scores[2]}]\n[{scores[3]}, {scores[4]}, {scores[5]}]\n[{scores[6]}, {scores[7]}, {scores[8]}]')
    print(f'Chosen spot : {move["cell"] + 1}')

    game.board[move['cell']] = AI
    time.sleep(1)


def human_turn(type = 'normal'):
    global game, scores, current_player
    current_player = HUMAN
    move = -1

    print(f'Human turn [{game.human_choice}]')

    if type == 'normal' :
        best_move = minimax(game.board, HUMAN)
        print(f'Minimax values of the available positions :\n[{scores[0]}, {scores[1]}, {scores[2]}]\n[{scores[3]}, {scores[4]}, {scores[5]}]\n[{scores[6]}, {scores[7]}, {scores[8]}]\nBest move is position {best_move["cell"] + 1}')

    while move < 1 or move > 9:
        try:
            move = int(input('Enter position : '))
            if not game.valid_move(move - 1):
                print('Move not possible')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Game terminated by user.')
            exit()
        except (KeyError, ValueError):
            print('Incorrect choice')
    
    game.board[move - 1] = HUMAN

def main():
    global game
    human_choice = ''
    ai_choice = ''
    first = ''
    choice  = 0
    
    print("Board positions :\n[1,2,3]\n[4,5,6]\n[7,8,9]")
    print('1)Play on empty board.\n2)Play on preset board(detailed).')
    
    while choice not in [1, 2]:
        choice = int(input('Enter choice : '))

    if choice == 1: 
        while human_choice != 'O' and human_choice != 'X':
            try:
                print('')
                human_choice = input('Choose X or O : ').upper()
            except (EOFError, KeyboardInterrupt):
                print('Game terminated by user.')
                exit()
            except (KeyError, ValueError):
                print('Incorrect choice')

        if human_choice == 'X':
            ai_choice = 'O'
        else:
            ai_choice = 'X'

        game = Game(ai_choice, human_choice)

        while first != 'Y' and first != 'N':
            try:
                first = input('First to start?[y/n]: ').upper()
            except (EOFError, KeyboardInterrupt):
                print('Game terminated by user.')
                exit()
            except (KeyError, ValueError):
                print('Incorrect choice')

        while not game.terminal(game.board):
            if first == 'N':
                game.display_board()
                ai_turn()
                first = ''
            
            game.display_board()
            human_turn()

            if not game.terminal(game.board):
                game.display_board()
                ai_turn()

        if game.wins(game.board, HUMAN):
            game.display_board()
            print('YOU WIN!')
        elif game.wins(game.board, AI):
            game.display_board()
            print('YOU LOSE!')
        else:
            game.display_board()
            print('DRAW!')
        exit()
    
    else:
        game = Game('X', 'O', [1, -1, 1,
                              -1, 0, -1,
                               0, 1, 0])
        print('Initial board : ')
        game.display_board()
        print('AI will play 1st.')
        time.sleep(2)

        while not game.terminal(game.board):
            ai_turn(type = 'detailed')
            if not game.terminal(game.board):
                game.display_board()
                human_turn(type = 'detailed')

        if game.wins(game.board, HUMAN):
            game.display_board()
            print('YOU WIN!')
        elif game.wins(game.board, AI):
            game.display_board()
            print('YOU LOSE!')
        else:
            game.display_board()
            print('DRAW!')
        exit()


if __name__ == '__main__':
    #global variables
    game  = current_player = None
    HUMAN = -1
    AI = +1
    scores = ['NA'] * 9

    #main game function
    main()

