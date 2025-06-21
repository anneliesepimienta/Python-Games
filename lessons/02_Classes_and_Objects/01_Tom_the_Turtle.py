""" Turtle in Pygame
github.com refused to connect.
github.com refused to connect.
We really miss the turtle module from Python's
import pygame
 standard library. It was a great
way to introduce programming, so let's make something similar in PyGame, using
objects. 

""" 
import math
import pygame
pygame.init()


#variables
TOMTHETURTLE_SPEED = 5

clock = pygame.time.Clock()



    

class Turtle:
    def __init__(self, screen, x: int, y: int):
        self.x = x
        self.y = y
        self.screen = screen
        self.angle = 0  # Angle in degrees, starting facing right

    def forward(self, distance):
        # Calculate new position based on current angle
        radian_angle = math.radians(self.angle)

        start_x = self.x  # Save the starting position
        start_y = self.y

        # Calculate the new position displacement
        dx = math.cos(radian_angle) * distance
        dy = math.sin(radian_angle) * distance

        # Update the turtle's position
        self.x += dx
        self.y -= dy

        # Draw line to the new position
        pygame.draw.line(self.screen, black, (start_x, start_y), (self.x, self.y), 2)

    def left(self, angle):
        # Turn left by adjusting the angle counterclockwise
        self.angle = (self.angle + angle) % 360

running = True 
keys = pygame.key.get_pressed()   
    
class NewTurtle(Turtle):  
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)
        self.color = "black"
        self.pen_up_or_down = True

    def forward(self, distance):
        # Calculate new position based on current angle
        radian_angle = math.radians(self.angle)

        start_x = self.x  # Save the starting position
        start_y = self.y

        # Calculate the new position displacement
        dx = math.cos(radian_angle) * distance
        dy = math.sin(radian_angle) * distance

        # Update the turtle's position
        self.x += dx
        self.y -= dy

        # Draw line to the new position
        if self.pen_up_or_down:
            pygame.draw.line(self.screen, self.color, (start_x, start_y), (self.x, self.y), 2)

    def right(self, angle):
        self.angle = (self.angle - angle) % 360

    def set_color(self, color):
        self.color = color

    def pen_up_down(self):
        self.pen_up_or_down =not (self.pen_up_or_down)


        

def event_loop(player):
    """Wait until user closes the window"""
    last_switch = pygame.time.get_ticks()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
                    player.right(1)
        if keys[pygame.K_LEFT]:
                    player.left(1)
        if keys[pygame.K_UP]:
                    player.forward(1)
        if keys[pygame.K_SPACE] and pygame.time.get_ticks() - last_switch > 10:
             player.pen_up_down()
             print(player.pen_up_or_down)
             last_switch = pygame.time.get_ticks()
        
        pygame.display.flip()

# Main loop

# Initialize Pygame
pygame.init()



# Screen dimensions and setup
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Turtle Style Drawing")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

screen.fill(white)
turtle = NewTurtle(screen, screen.get_width() // 2, screen.get_height() // 2)  # Start at the center of the screen

# Draw a square using turtle-style commands
for _ in range(4):
    turtle.forward(10)  # Move forward by 100 pixels

# Display the drawing
pygame.display.flip()

# Wait to quit
event_loop(turtle)

# Quit Pygame
pygame.quit()
