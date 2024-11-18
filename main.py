from environment import Environment
from grid_ui import GridUI

def main():
    # Create a 20x20 environment
    environment = Environment(grid_size=(20, 20))

    # Add some obstacles for testing
    environment.add_obstacle(5, 5)
    environment.add_obstacle(10, 10)
    environment.add_obstacle(15, 15)

    # Initialize the Grid UI and start the program
    ui = GridUI(environment)
    ui.run()

if __name__ == "__main__":
    main()
