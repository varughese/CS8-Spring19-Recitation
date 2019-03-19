import pygame
import random

# Define some colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BALL_SIZE = 25


class Ball:
    """
    Class to keep track of a ball's location and vector.
    """

    def __init__(self, color):
        # Starting position of the ball.
        # Take into account the ball size so we don't spawn on the edge.
        self.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
        self.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)

        # Speed and direction of rectangle
        self.change_x = random.randrange(-2, 3)
        self.change_y = random.randrange(-2, 3)
        # TODO: ADD AN ATTRIBUTE WITH THE COLOR
        self.color = color

    def get_color(self):
        return self.color


def main():
    """
    This is our main program.
    """
    pygame.init()

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Bouncing Ball(s)")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    ball_list = []

    #ball = Ball(RED)
    ball_list.append(Ball(RED))
    ball_list.append(Ball(YELLOW))
    ball_list.append(Ball(GREEN))

    # -------- Main Program Loop -----------
    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # --- Logic

        # Move the ball's center
        # TODO: LOOP OVER THE BALLS TO MOVE THEM
        for ball in ball_list:
            ball.x += ball.change_x
            ball.y += ball.change_y

            # Bounce the ball if needed
            if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
                ball.change_y *= -1
            if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
                ball.change_x *= -1

        # --- Drawing
        # Set the screen background
        screen.fill(WHITE)

        # Draw the ball(s)
        # TODO: LOOP OVER THE BALLS TO DRAW THEM
        for ball in ball_list:
            pygame.draw.circle(screen, ball.get_color(), [ball.x, ball.y], BALL_SIZE)

        # --- Wrap-up
        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Close everything down
    pygame.quit()


main()
