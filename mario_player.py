class MarioPlayer:
  def __init__(self, color):
    self.color = color

  def play(self, board):
    return self.minimaxDecision(board)

  def minimaxDecision(self, board):
    calc = self.maxValue(board, 0)
    value = calc[0]
    idValue = calc[1].index(value)
    moves = board.valid_moves(self.color)
    chosen_move = moves[idValue]
    return chosen_move

  def maxValue(self, board, turn):
    if self.finish_game(board) or turn == 3:
      whiteScore = (board.score())[0]
      blackScore = (board.score())[1]
      if self.color == 'o':
        return [whiteScore - blackScore, []]
      else:
        return [blackScore - whiteScore, []]
    else:
      values = []
      moves = board.valid_moves(self.color)
      for move in moves:
        board_copy = board.get_clone()
        board_copy.play(move, self.color)
        successor_value = (self.minValue(board_copy, turn+1))[0]
        values.append(successor_value)
      return [max(values), values]

  def minValue(self, board, turn):
    if self.finish_game(board) or turn == 3:
      whiteScore = (board.score())[0]
      blackScore = (board.score())[1]
      if self.color == 'o':
        return [whiteScore - blackScore, []]
      else:
        return [blackScore - whiteScore, []]
    else:
      values = []
      opponent_color = board._opponent(self.color)
      moves = board.valid_moves(opponent_color)
      for move in moves:
        board_copy = board.get_clone()
        board_copy.play(move, opponent_color)
        successor_value = (self.maxValue(board_copy, turn+1))[0]
        values.append(successor_value)
      return [min(values), values]

  def finish_game(self, board):
    if board.valid_moves('o').__len__() == 0 and board.valid_moves('@').__len__() == 0:
      return True
    else:
      return False
