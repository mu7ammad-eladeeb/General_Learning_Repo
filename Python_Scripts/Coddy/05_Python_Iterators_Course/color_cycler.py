# Cyclic Iterator Challenge
# Create a ColorCycler class that implements a cyclic iterator for a list of colors.

class ColorCycler:
    def __init__(self, colors):
        # Initialize the iterator with a list of colors and an index tracker at 0.
        self.colors = colors
        self.index = 0

    def __iter__(self):
        # Return the iterator object itself to fulfill the iterator protocol.
        return self

    def __next__(self):
        # Retrieve the color at the current index.
        # Check if the index has reached the length of the list; if so, reset to 0 to create cyclic behavior.
        if self.index >= len(self.colors):
            self.index = 0
        
        color = self.colors[self.index]
        # Increment the index for the next call.
        self.index += 1
        return color

# Execution: Take user input, split the color string into a list, and initialize the ColorCycler.
colors = input().split(',')
num_colors = int(input())

cycler = ColorCycler(colors)
# Note: You can use itertools.cycle(colors) instead.
# Use a loop to call next() the specified number of times and print each result on a new line.
for _ in range(num_colors):
    print(next(cycler))
