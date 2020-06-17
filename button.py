''' Module includes class Button '''
import pygame

class Button:
    ''' Graphical button. '''
    # pylint: disable=invalid-name
    # Pola x i y.
    def __init__(self, color, coordinates, dimensions, text=''):
        self.color = color
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.width = dimensions[0]
        self.height = dimensions[1]
        self.text = text

    def draw(self, screen, outline=None):
        ''' Call this method to draw the button on the screen '''
        if outline:
            pygame.draw.rect(screen, outline, (self.x - 2, self.y - 2,
                                               self.width + 4, self.height + 4), 0)

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('freesansbold.ttf', 24)
            text = font.render(self.text, 1, (0, 0, 0))
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                               self.y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self, mouse_x, mouse_y):
        ''' Pos is the mouse position or a tuple of (x,y) coordinates'''
        if self.x < mouse_x < self.x + self.width:
            if self.y < mouse_y < self.y + self.height:
                return True
        return False
