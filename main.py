import matplotlib.pyplot as plt
import matplotlib.patches as patches

class CityGrid:
    def __init__(self, size):
        self.grid = [[0 for _ in range(size)] for _ in range(size)]
        self.fire_station = (0, 0)

    def set_fire(self, x, y):
        if self.is_valid_coordinate(x, y):
            self.grid[y][x] = 1

    def extinguish_fire(self, x, y):
        if self.is_valid_coordinate(x, y):
            self.grid[y][x] = 2

    def is_valid_coordinate(self, x, y):
        return 0 <= x < len(self.grid) and 0 <= y < len(self.grid)

    def select_fire_blocks(self):
        print("Please select 3 blocks where fires are located.")
        for _ in range(3):
            x = int(input("Enter x-coordinate of the block on fire (0 to 3): "))
            y = int(input("Enter y-coordinate of the block on fire (0 to 3): "))
            if not self.is_valid_coordinate(x, y) or self.grid[y][x] == 1:
                print("Invalid or already chosen block. Try again.")
                continue
            self.set_fire(x, y)

    def display(self):
        fig, ax = plt.subplots(figsize=(6, 6))

        for x in range(len(self.grid) + 1):
            ax.axhline(y=x, color='k', lw=2)
            ax.axvline(x=x, color='k', lw=2)

        for y, row in enumerate(self.grid):
            for x, status in enumerate(row):
                if status == 1:  # Fire
                    rect = patches.Rectangle((x, y), 1, 1, edgecolor='k', facecolor='red')
                    ax.add_patch(rect)
                elif status == 2:  # Extinguished
                    rect = patches.Rectangle((x, y), 1, 1, edgecolor='k', facecolor='blue')
                    ax.add_patch(rect)

        # Represent the fire station as a circle at the center of its block
        circle = patches.Circle((self.fire_station[0] + 0.5, self.fire_station[1] + 0.5), 0.3, edgecolor='k', facecolor='green')
        ax.add_patch(circle)

        plt.xlim(0, len(self.grid))
        plt.ylim(0, len(self.grid))
        ax.set_aspect('equal')
        plt.show()

# Example Usage
city = CityGrid(4)
city.select_fire_blocks()
city.display()
