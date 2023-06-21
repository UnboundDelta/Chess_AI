import chess
board = chess.Board()

# Play some moves
board.push_san("e4")
board.push_san("e5")
board.push_san("Bc4")
board.push_san("Bc5")
board.push_san("Qf3")
board.push_san("Ne7")
board.push_san("Qxf7")

result = board.result()
print(type(result))
