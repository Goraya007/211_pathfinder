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

    def display(self):
        fig, ax = plt.subplots(figsize=(6, 6))

        # Draw grid
        for x in range(len(self.grid) + 1):
            ax.axhline(y=x, color='k', lw=2)
            ax.axvline(x=x, color='k', lw=2)

        # Draw blocks with fires and extinguished fires
        for y, row in enumerate(self.grid):
            for x, status in enumerate(row):
                if status == 1:  # Fire
                    rect = patches.Rectangle((x, y), 1, 1, edgecolor='k', facecolor='red')
                    ax.add_patch(rect)
                elif status == 2:  # Extinguished
                    rect = patches.Rectangle((x, y), 1, 1, edgecolor='k', facecolor='blue')
                    ax.add_patch(rect)

        # Highlight fire station
        rect = patches.Rectangle(self.fire_station, 1, 1, edgecolor='k', facecolor='green')
        ax.add_patch(rect)

        plt.xlim(0, len(self.grid))
        plt.ylim(0, len(self.grid))
        ax.set_aspect('equal')
        plt.gca().invert_yaxis()  # Invert y-axis to match matrix representation
        plt.show()


# Example Usage
city = CityGrid(4)
city.set_fire(2, 2)
city.display()
city.extinguish_fire(2, 2)
city.display()
