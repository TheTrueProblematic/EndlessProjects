
# Conway's Game of Life
# Hello there! Let's embark on the solar-sailing journey across the starlit sea that is the Game of Life, invented by British mathematician John Horton Conway in 1970.

import copy
import time

# Let's define our very own neighbourhood! Erm... it's a neighbour for the cells in our grid
NEIGHBOURS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def get_neighbours(cell):
    """
    What's a cell without its neighbours? This calculates and returns a list of neighbours for a cell.
    """
    return [(cell[0] + dx, cell[1] + dy) for dx, dy in NEIGHBOURS]

def get_new_generation(live_cells):
    """
    It's the circle of life and it moves us all. Or some of us. Depends on the rules.
    For a position to be a live cell in the new generation,
    - it should be a live cell with 2 or 3 live neighbours or,
    - it should be a dead cell with 3 live neighbours
    """
    new_gen_candidates = live_cells.union(*map(set, map(get_neighbours, live_cells)))
    new_live_cells = set()
    for cell in new_gen_candidates:
        live_neighbour_count = len(live_cells.intersection(get_neighbours(cell)))
        if live_neighbour_count == 3 or (live_neighbour_count == 2 and cell in live_cells):
            new_live_cells.add(cell)
    return new_live_cells

def pretty_print(live_cells, generation):
    """
    Because we do love a nicely formatted grid!
    """
    min_x = min(cell[0] for cell in live_cells) if live_cells else 0
    max_x = max(cell[0] for cell in live_cells) if live_cells else 0
    min_y = min(cell[1] for cell in live_cells) if live_cells else 0
    max_y = max(cell[1] for cell in live_cells) if live_cells else 0
    
    print(f'Generation: {generation}, Live cells: {len(live_cells)}')
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            print('*' if (x, y) in live_cells else ' ', end='')
        print()
    print()

if __name__ == "__main__":
    live_cells = set()
    initial_config = [
        # let's setup a "Glider", it's a pattern of cells that moves across the grid
        [2, 1], [3, 2], [1, 3], [2, 3], [3, 3]
    ]

    # let's give life to our initial configuration
    for cell in initial_config:
        live_cells.add(tuple(cell))

    generation = 0
    while True:
        pretty_print(live_cells, generation)
        live_cells = get_new_generation(live_cells)
        generation += 1
        time.sleep(1)  # let's pause a bit before moving to the next generation

