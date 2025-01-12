from graphics import *
import random
from pprint import pprint

def main():

    # Drawing variables
    window_width = 500
    window_height = 500
    padding = 100
    tile_size = 10

    # Loop to run program
    running = True

    # Cells
    cells = []

    # Initialise nonogram
    highlighted_cells = 80
    board = create_2d_list(tile_size, tile_size, False)
    player_board = create_2d_list(tile_size, tile_size, False)

    # Randomly assign True to highlighted cells for puzzle
    for i in range(highlighted_cells):
        x = random.randint(0,tile_size - 1)
        y = random.randint(0,tile_size - 1)
        board[x][y] = True  

    # Make window
    win = GraphWin("Nonogram", window_width, window_height)
    win.setBackground("beige")
       
    # Count highlighted cells and draw correct numbers at end of rows and columns
    columns = []
    rows = []

    # Count columns
    for x in range(tile_size):
        started = False
        count = 0
        entries = []

        for y in range(tile_size):
            if board[x][y]:
                started = True
                count += 1
            
            if not board[x][y] and started:
                entries.append(count)
                count = 0
                started = False
        
        if (started) or (not started and len(entries) == 0):
            entries.append(count)

        columns.append(entries)
    

    # Count rows
    for y in range(tile_size):
        started = False
        count = 0
        entries = []
        for x in range(tile_size):
            if board[x][y]:
                started = True
                count += 1
            
            if not board[x][y] and started:
                entries.append(count)
                count = 0
                started = False
        
        if (started) or (not started and len(entries) == 0):
            entries.append(count)

        rows.append(entries)
    
    # Draw correct numbers
    # Rows
    for i in range(tile_size):
        for index, entry in enumerate(rows[i]):
            box_height = (window_height - padding) / tile_size
            y = padding + (i * box_height) + box_height/2
            text = Text(Point(10 + 20 * index, y), str(entry))
            text.setStyle("bold")
            text.draw(win)
        
        for index, entry in enumerate(columns[i]):
            box_width = (window_width - padding) / tile_size
            x = padding + (i * box_width) + box_width/2
            text = Text(Point(x, 10 + 25 * index), str(entry))
            text.setStyle("bold")
            text.draw(win)

    # Get reference cells and put into list
    for x in range(tile_size):
        row = []
        for y in range(tile_size):
            square_x = padding + (x * ((window_width - padding) / tile_size))
            square_y = padding + (y * ((window_height - padding) / tile_size))
            square_size = (window_height - padding) / tile_size
            square = Rectangle(Point(square_x, square_y), Point(square_x + square_size, square_y + square_size))

            # ** Show correct squares for testing **
            if board[x][y]:
                square.setFill("green")

            square.draw(win)
            row.append(square)

        cells.append(row)

    # Draw grid lines
    for i in range(tile_size):
        
        # Vertical lines
        x = padding + (i * ((window_width - padding) / tile_size))
        vertical_line = Line(Point(x, 0), Point(x, window_height))
        vertical_line.setOutline('maroon')
        vertical_line.draw(win)

        # Horizontal lines
        y = padding + (i * ((window_height - padding) / tile_size))
        horizontal_line = Line(Point(0, y), Point(window_width, y))
        horizontal_line.setOutline('maroon')
        horizontal_line.draw(win)

    # Main loop
    while running:

        # Get mouse click point - Pauses to view result
        mouse = win.getMouse() 

        # Get cell positions
        x = int((mouse.x - padding)/((window_width - padding) / tile_size))
        y = int((mouse.y - padding)/((window_height - padding) / tile_size))
                
        # Draw square in clicked square and update highlighted variable of object
        if x >= 0 and y >= 0:
            if cells[x][y].config['fill'] == "black":
                cells[x][y].setFill("red")
                player_board[x][y] = False
            elif cells[x][y].config['fill'] == "red":
                cells[x][y].setFill("")
            else:
                cells[x][y].setFill("black")
                player_board[x][y] = True
        
        # Check if have won
        if player_board == board:
            
            # Win message
            input("You win! - press 'Enter' to close\n")

            # Close window when done
            win.close()    

def create_2d_list(width, height, default):
    li = []
    
    for x in range(width):
        row = []
        for y in range(height):
            row.append(default)
        
        li.append(row)
    
    return li

main()
