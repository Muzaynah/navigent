import pygame

class GridUI:
    def __init__(self, environment):
        """
        Initialize the Grid UI.
        :param environment: Instance of the Environment class.
        """
        self.environment = environment
        self.cell_size = 30  # Size of each cell in pixels
        self.width = environment.grid_size[1] * self.cell_size
        self.height = environment.grid_size[0] * self.cell_size

        # Initialize the pygame window
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Navigent Grid")

    def run(self):
        """
        Start the main loop for the UI.
        """
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw_grid()
            pygame.display.flip()
            clock.tick(30)  # Limit to 30 FPS

        pygame.quit()

    def draw_grid(self):
        """
        Draw the environment grid on the screen.
        """
        self.screen.fill((255, 255, 255))  # Background color: White

        for row in range(self.environment.grid_size[0]):
            for col in range(self.environment.grid_size[1]):
                # Determine the color for each cell
                color = (200, 200, 200)  # Default color: Light gray
                if self.environment.grid[row][col] == 1:  # Obstacle
                    color = (0, 0, 0)  # Black for obstacles

                # Draw the cell
                pygame.draw.rect(
                    self.screen,
                    color,
                    pygame.Rect(
                        col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size
                    )
                )

                # Draw the grid line (optional for better visibility)
                pygame.draw.rect(
                    self.screen,
                    (50, 50, 50),  # Dark gray for grid lines
                    pygame.Rect(
                        col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size
                    ),
                    1  # Line thickness
                )
