class MarioPlayer:
  def __init__(self, color):
    self.color = color

  def play(self, board):
    return self.minimaxDecision(board)

  def minimaxDecision(self, board):
    calc = self.maxValue(board, 0, -100000, 100000)
    value = calc[0]
    idValue = calc[1].index(value)
    moves = board.valid_moves(self.color)
    chosen_move = moves[idValue]
    return chosen_move

  def maxValue(self, board, turn, alpha, beta):
    if self.finish_game(board) or turn == 5:
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
        successor_value = (self.minValue(board_copy, turn+1, alpha, beta))[0]
        values.append(successor_value)
      maxValue = [max(values), values]
      if maxValue[0] >= beta:
        return maxValue
      else:
        alpha = max([alpha, maxValue[0]])
      return maxValue

  def minValue(self, board, turn, alpha, beta):
    if self.finish_game(board) or turn == 5:
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
        successor_value = (self.maxValue(board_copy, turn+1, alpha, beta))[0]
        values.append(successor_value)
      minValue = [min(values), values]
      if minValue[0] <= alpha:
        return minValue
      else:
        beta = min([beta, minValue[0]])
      return minValue

  def finish_game(self, board):
    if board.valid_moves('o').__len__() == 0 or board.valid_moves('@').__len__() == 0:
      return True
    else:
      return False
