import chess
import pygame
from game1 import Game1

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Create a window
screen = pygame.display.set_mode((600, 600))


# Variables to track the selected piece and its position
selected_piece = None
selected_pos = None


class Main:
    
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        pygame.mixer.init()
        
        # Create a window
        self.screen = pygame.display.set_mode((600, 600))
        
        # Set the title
        pygame.display.set_caption('Chess')
        
        # Using the game class
        self.game = Game1()
        
        # Variables to track the selected piece and its position
        self.selected_piece = None
        self.selected_pos = None
        
    def mainloop(self):
        
        screen = self.screen
        game = self.game
        selected_piece = self.selected_piece
        selected_pos = self.selected_pos
        
            
        while True:
            
            game.draw_board(screen)
            game.draw_pieces(screen)
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    pygame.mixer.quit()
                    quit()
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the position of the mouse click
                    pos = pygame.mouse.get_pos()
                    # Convert the position to a square on the board
                    x = pos[0] // 75
                    y = 7 - pos[1] // 75
                    # Check if a piece is already selected
                    if selected_piece:
                        # Get the current square
                        curr_pos = x + y * 8
                        # Get the destination square
                        dest_pos = selected_pos
                        # Check if the move is legal
                        move = chess.Move(dest_pos, curr_pos)
                        if game.board.is_legal(move):
                            game.board.push(move)
                            game.update_my_board()
                            # Make sounds
                            if game.is_captured():
                                game.play_sound(True)
                            else:
                                game.play_sound()
                                
                        # Deselect the piece
                        selected_piece = None
                        selected_pos = None
                    else:
                        # Check if there is a piece on the square
                        piece = game.board.piece_at(x + y * 8)
                        if piece:
                            # Select the piece
                            selected_piece = piece
                            selected_pos = x + y * 8
                
                elif event.type == pygame.KEYDOWN:
                    # Undo a Move
                    if event.key == pygame.K_z:
                        try:
                            game.board.pop()
                            game.update_my_board()
                            game.vague_Squares = game.sum
                        except:
                            pass
                    
                    # Resetting a Board 
                    elif event.key == pygame.K_r:
                        try:
                            game.board.reset()
                            game.update_my_board()
                        except:
                            pass
                            
                            
            game.draw_board(screen)
            game.draw_pieces(screen)
            
            if selected_piece:
                x = selected_pos % 8
                y = selected_pos // 8
                pygame.draw.rect(screen, (0, 255, 0), (x * 75, (7-y) * 75, 75, 75), 5)
                    
            pygame.display.update()
            
main = Main()
main.mainloop()
            
            