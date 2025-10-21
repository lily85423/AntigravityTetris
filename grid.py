# ------------------------------------------------------
#        Name: Lily Mitchell, Caro Faust, & Greta Wang
#       Peers: N/A
#  References: N/A
# ------------------------------------------------------

from graphics import *
def drawGrid(win:GraphWin, win_width:int, win_height:int, grid_dim:int) -> tuple[list[list[Rectangle]], int, int]:
    """ Given parameters for window and grid size, creates a list of graphics objects making up 
    the grid. Along with returning this list, function also returns the size of a square and the grid in pixels.
    :param win: (GraphWin) The window 
    :param win_width: (int) Window width in pixels
    :param win_height: (int) Window height in pixels
    :param grid_dim: (int) Dimension of the square grid in number of squares
    :return : (tuple[list[list[Rectangle]],int,int]) Returns grid, square_size (the size of a square in pixels), 
    and grid_size (the size of the grid in pixels)
    """
    grid_size:int = int(3/5 * win_height) # pixels in a side
    square_size:int = int(grid_size / grid_dim) #num pixels in a square
    grid:list = [] 
    #Makes a list of squares (graphic objects)
    
    
    for i in range(grid_dim): #Creates a grid, row by row
        start_x = win_width / 2 + square_size * i 
        row:list = []
        for j in range(grid_dim): #Creates a row, square by square
            start_y = win_height / 2 - grid_size / 2 + square_size * j
            square = Rectangle(Point(start_x, start_y), Point(start_x + square_size, start_y + square_size))
            square.setFill(color_rgb(75, 89, 92)) #filling squares in grid with background color so they are not transparent
            row.append(square)
        grid.append(row)
    #Draws the grid square by square
    for i in range(grid_dim):
        for j in range(grid_dim):
            grid[i][j].draw(win)
    return (grid, square_size, grid_size)
            
def makeIsFull(grid:list[list[Rectangle]]) -> dict[Rectangle, bool]:
    """Creates a dictionary called is_full that stores the grid indices and whether or not each square is full.
    If a square is full it's labeled 'True'; if not, square is labeled 'False.' 
    :param grid: (list[list[Rectangle]]) A list of lists of graphics objects (squares) that combine to make a grid
    :return : (dict[Rectangle, bool]) A dictionary with each square index of the grid as a key and 'False' as each of the values.
    """
    is_full:dict = {}
    for i in range(len(grid)):
        for j in range(len(grid)):
            is_full[grid[i][j]] = False #Each index is assigned the value False
    return is_full

def makeButton(win:GraphWin, win_width:int) -> tuple[int, int, int, int, Rectangle, Text]:
    """Creates a square quit button that appears in the upper hand corner of the screen.
    :param win: (GraphWin) The window 
    :param win_width: (int) Window width in pixels
    :return : (tuple[int,int,int,int]) The start and end x and y values for the button
    """
    start_x = win_width - 50
    start_y = 20
    end_x = win_width -20
    end_y = 50
    button = Rectangle(Point(start_x, start_y), Point(end_x, end_y))
    button.setFill(color_rgb(219, 131, 131))
    button.draw(win)
    x = Text(Point(win_width - 35, 35), "X")
    x.setSize(28)
    x.setFace("courier")
    x.draw(win)
    return(start_x, start_y, end_x, end_y, button, x)

        
if __name__ == "__main__":
    pass