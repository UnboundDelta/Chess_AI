import pygame
import chess

class Game1:
    
    def __init__(self):
        # Create a new chess board
        self.board = chess.Board()
        
        # Initialize your own chess board
        self.my_board = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
        
        # Sounds
        self.move_sound = pygame.mixer.Sound('move.wav')
        self.capture_sound = pygame.mixer.Sound('capture.wav')
        
        # Load images of the chess pieces
        self.pieces = {
            'P': pygame.image.load("white_pawn.png"),
            'N': pygame.image.load("white_knight.png"),
            'B': pygame.image.load("white_bishop.png"),
            'R': pygame.image.load("white_rook.png"),
            'Q': pygame.image.load("white_queen.png"),
            'K': pygame.image.load("white_king.png"),
            'p': pygame.image.load("black_pawn.png"),
            'n': pygame.image.load("black_knight.png"),
            'b': pygame.image.load("black_bishop.png"),
            'r': pygame.image.load("black_rook.png"),
            'q': pygame.image.load("black_queen.png"),
            'k': pygame.image.load("black_king.png"),
        }
        
        # Tracking the empty squares
        self.vague_Squares = 32
        self.sum = 0
        
    def draw_board(self, screen):
        for i in range(64):
            x = i % 8
            y = i // 8
            color = (234, 235, 200) if (x + y) % 2 == 0 else (119, 154, 88)
            pygame.draw.rect(screen, color, (x * 75, y * 75, 75, 75))
            
    def draw_pieces(self, screen):
        for i in range(64):
            x = i % 8
            y = i // 8
            piece = self.board.piece_at(i)
            if piece:
                img = self.pieces[piece.symbol()]
                screen.blit(img, (x * 75, (7 - y) * 75))
                
    def update_my_board(self):
        self.sum = 0
        for i in range(64):
            x = i % 8
            y = i // 8
            piece = self.board.piece_at(i)
            if piece:
                self.my_board[y][x] = piece.symbol().upper()
            else:
                self.my_board[y][x] = '.'
                self.sum += 1
                
    def play_sound(self, captured = False):
        if captured:
            pygame.mixer.Sound.play(self.capture_sound)
        else:
            pygame.mixer.Sound.play(self.move_sound)

    def is_captured(self):
        if self.vague_Squares == self.sum:
            return False
        elif self.vague_Squares < self.sum:
            self.vague_Squares = self.sum
            return True