# ------------------------------------------------------
#        Name: Lily Mitchell, Caro Faust, & Greta Wang
#       Peers: N/A
#  References: N/A
# ------------------------------------------------------
from graphics import *
from random import randint
from random import seed
from time import sleep

def randomShape() -> tuple[list[tuple[int, int]], int]:
    """ This function picks a random list of points representing a shape out of a list using an index, and returns the index and the list representing the shape.
    :return : (tuple[list[tuple[int, int]], int]) The list of points representing a shape and the associated shape index. 

    >>> seed(1)
    >>> randomShape()
    ([(0, 0), (0, 1), (1, 0), (2, 0)], 4)
    """
    shapes:list = [[(0,0),(1,0),(0,1),(0,2)],[(0,0),(0,1),(0,2),(1,2)],[(1,0),(1,1),(1,2),(0,2)],
               [(0,0),(1,0),(2,0),(2,1)],[(0,0),(0,1),(1,0),(2,0)],[(0,0),(1,0),(1,1),(1,2)],
               [(0,1),(1,1),(2,1),(2,0)],[(0,0),(0,1),(1,1),(2,1)],[(0,0),(0,1),(1,0),(1,1)],
               [(0,1),(1,1),(1,0),(2,1)],[(0,0),(0,1),(1,1),(0,2)],[(0,0),(1,0),(2,0),(1,1)],
               [(1,0),(1,1),(1,2),(0,1)],[(0,0),(1,0),(2,0)],[(0,0),(0,1),(0,2)],[(0,0),(1,0),(2,0),(3,0)],
               [(0,0),(0,1),(0,2),(0,3)],[(0,1),(1,1),(1,0),(2,1),(1,2)],[(0,0),(1,0),(2,0),(0,1),(2,1),(0,2),(1,2),(2,2)],
               [(0,0),(1,1)],[(1,0),(0,1)],[(0,0),(1,1),(2,2)],[(2,0),(0,2),(1,1)]]

    shape_index:int = randint(0, len(shapes) - 1)
    
    #making it slightly less likely to generate the more difficult shapes
    change_shape:int = randint(0, 4)
    if shape_index == 17: #cross
        if change_shape == 0: #1 in 5 chance that a new shape will be chosen
            shape_index = randint(0, len(shapes) - 1)
    if shape_index == 18: #donut
        if change_shape <= 1: #2 in 5 chance that a new shape will be chosen
            shape_index = randint(0, len(shapes) - 1)
    
    shape:list = shapes[shape_index]
    return (shape, shape_index)

def assignColor(shape_index:int) -> tuple[int, int, int]:
    """ This function decides the color of a shape based on its index. There are 23 shapes, and each shape has one of 7 colors depending on its position in the list.
    :param shape_index: (int) The index of the shape in the list of shapes.
    :return : (tuple[int, int, int]) A color in RGB form.

    >>> assignColor(1)
    (163, 115, 152)
    >>> assignColor(2)
    (129, 132, 196)
    >>> assignColor(10)
    (198, 199, 85)
    """
    if shape_index % 7 == 0:
        color = (219, 131, 131) #pink
    elif shape_index % 6 == 0:
        color = (236, 193, 82) #yellow
    elif shape_index % 5 == 0:
        color = (198, 199, 85) #green
    elif shape_index % 4 == 0:
        color = (144, 188, 153) #turquoise
    elif shape_index % 3 == 0:
        color = (170, 200, 204) #blue
    elif shape_index % 2 == 0:
        color = (129, 132, 196) #indigo
    else:
        color = (163, 115, 152) #purple
    return color

def shapeMaker(shape:list[tuple[int, int]], origin_point_x:int, origin_point_y:int, len_sides:int, win:GraphWin, color:tuple[int, int, int]) -> tuple[int, int, list[Rectangle]]:
    """ This function draws a chosen shape in the window using Rectangle Graphics objects, to the right of the game board. The shape has a highlighted square indicating to the user how the shape will be placed when the grid is clicked.
    :param shape: (list[tuple[int, int]]) A list of points representing the shape.
    :param origin_point_x: (int) The x-coordinate of the point on the window where the shapes will be drawn from.
    :param origin_point_y: (int) The y-coordinate of the point on the window where the shapes will be drawn from.
    :param len_sides: (int) The length of a side of the squares that make up the shapes.
    :param win: (GraphWin) The Graphics window that the shapes will be drawn to.
    :param color: (tuple[int, int, int]) The RGB color of the shape.
    :return : (tuple[int, int, list[Rectangle]]) The x and y coordinates of the highlight square based on the list of points representing the shape, and a list of the Graphics objects drawn.
    """
    square_list = [] #to contain the Graphics objects
    for (i,j) in shape:
        square = Rectangle(Point(origin_point_x + i*len_sides, origin_point_y + j*len_sides), Point(origin_point_x + (i+1)*len_sides, origin_point_y + (j+1)*len_sides))
        square.setFill(color_rgb(color[0], color[1], color[2]))
        square.draw(win)
        square_list.append(square)
    for i in range(4): #picking the highlight square
        for j in range(4):
            if (i,j) in shape:
                highlight_square = Rectangle(Point(origin_point_x + i*len_sides, origin_point_y + j*len_sides), Point(origin_point_x + (i+1)*len_sides, origin_point_y + (j+1)*len_sides))
                highlight_square.setFill(color_rgb((color[0] * 4)//5, (color[1] * 4)//5, (color[2] * 4)//5))
                highlight_square.draw(win)
                square_list.append(highlight_square)
                return (i,j, square_list) #returns after a highlight square is picked
    return(0,0, []) #not meant to ever get to this line

def shapeRemover(square_list:list[Rectangle]) -> None:
    """ This function undraws the shape to the left of the grid.
    :param square_list: (list[Rectangle]) The list of Graphics objects that will be undrawn.
    """
    for square in square_list:
        square.undraw()

def findSquare(click_x:float, click_y:float, win_width:int, win_height:int, grid_size:int, square_size:int) -> tuple[int, int]:
    """ This function takes as input the x- and y-coordinates where the user clicked and determines which square of the grid they clicked on.
    :param click_x: (float) The x-coordinate of the point where the user clicked.
    :param click_y: (float) The y-coordinate of the point where the user clicked.
    :param win_width: (int) The width of the Graphics window.
    :param win_height: (int) The height of the Graphics window.
    :param grid_size: (int) The length of the sides of the grid.
    :param square_size: (int) The length of the sides of the squares in the grid.
    :return : (tuple[int, int]) A tuple representing the square in the grid that the user clicked on, or (-1, -1) if the user clicked outside of the grid.

    >>> findSquare(360, 200, 700, 525, 315, 39)
    (0, 2)
    >>> findSquare(400, 150, 700, 525, 315, 39)
    (1, 1)
    >>> findSquare(100, 100, 700, 525, 315, 39)
    (-1, -1)
    """
    grid_start_x:int = win_width // 2 #lowest x value inside the grid
    grid_start_y:int = (win_height // 2) - (grid_size // 2) #lowest y value inside the grid
    if grid_start_x < click_x and click_x < grid_start_x + grid_size and grid_start_y < click_y and click_y < grid_start_y + grid_size: #if the user clicked in the grid
        column:int = int((click_x - grid_start_x) / square_size)
        row:int = int((click_y - grid_start_y) / square_size)
        return (column, row)
    else: #if the user clicked outside of the grid
        return (-1, -1)

def moveShape(shape:list[tuple[int, int]], highlight_square:tuple[int, int], grid:list[list[Rectangle]], grid_dim:int, click_square:tuple[int, int], color:tuple[int, int, int], is_full:dict[Rectangle, bool]) -> None:
    """ This function "moves" a shape to the grid by changing the colors of the Rectangle objects that make up the grid.
    :param shape: (list[tuple[int, int]]) A list of points representing the shape.
    :param highlight_square: (tuple[int, int]) The point that is highlighted out of the list of points representing the shape.
    :param grid: (list[list[Rectangle]]) A list of lists of Graphics objects that make up the grid.
    :param grid_dim: (int) The number of squares in a side of the grid.
    :param click_square: (tuple[int, int]) The coordinates representing the square that the user clicked on.
    :param color: (tuple[int, int, int]) The RGB color of the shape being moved to the grid.
    :param is_full: (dict[Rectangle, bool]) A dictionary containing information on whether every square in the grid is full or not.
    """
    if checkPlacementError(shape, highlight_square, grid, grid_dim, click_square, is_full) == False: #if the user clicked a square where there is space for the shape
        for (i,j) in shape:
            square = grid[click_square[0] - highlight_square[0] + i][click_square[1] - highlight_square[1] + j] #coordinates in the grid of each square of the shape
            square.setFill(color_rgb(color[0], color[1], color[2]))
            is_full[square] = True

def checkPlacementError(shape:list[tuple[int, int]], highlight_square:tuple[int, int], grid:list[list[Rectangle]], grid_dim:int, click_square:tuple[int, int], is_full:dict[Rectangle, bool]) -> bool:
    """ Returns False if a given shape can fit in a given spot on the grid, and True if it won't fit.
    :param shape: (list[tuple[int, int]]) A list of tuples representing coordinates of squares in a shape
    :param highlight_square: (tuple[int, int]) Coordinates representing the darkened square in the shape
    :param grid: (list[list[Rectangle]]) A list of lists of graphics objects which form a grid
    :param grid_dim: (int) The number of squares in one row/column of the grid
    :param click_square: (tuple[int, int]) Coordinates representing the square of the grid on which to place the darkened square in the shape
    :param is_full: (dict[Rectangle, bool]) A dictionary with each square in the grid as a key, with value True if the square is full, False if empty
    :return : (bool) False if the shape will fit, True if not
    """
    for (i,j) in shape:
        if 0 <= click_square[0] - highlight_square[0] + i and click_square[0] - highlight_square[0] + i < grid_dim and 0 <= click_square[1] - highlight_square[1] + j and click_square[1] - highlight_square[1] + j < grid_dim: #if this square of the shape will end up inside the grid
            square = grid[click_square[0] - highlight_square[0] + i][click_square[1] - highlight_square[1] + j] #square of the grid where the square of the shape will be moved
            if is_full[square] == True:
                return True #if the square of the grid is full, bad placement
        else:
            return True #if the square won't end up inside the grid, bad placement
    #if all square of the shape will be moved to empty squares on the grid:
    return False

def destroy(grid:list[list[Rectangle]], is_full:dict[Rectangle, bool], grid_dim:int, score:int, score_count:Text) -> int:
    """ Empties any full rows or columns in the grid, and updates the score accordingly.
    :param grid: (list[list[Rectangle]]) A list of lists of graphics objects which form a grid
    :param is_full: (dict[Rectangle, bool]) A dictionary with each square in the grid as a key, with value True if the square is full, False if empty
    :param grid_dim: (int) The number of squares in one row/column of the grid
    :param score: (int) The player's current score
    :param score_count: (Text) Text displaying the score
    :return : (int) The updated score
    """
    i_list:list = [] #list of numbers corresponding to full columns
    for i in range(grid_dim):
        full_count:int = 0
        for j in range(grid_dim):
            if is_full[grid[i][j]] == True:
                full_count += 1
        if full_count == grid_dim: #if all squares in column are full
            i_list.append(i)
    j_list:list = [] #list of numbers corresponding to full rows
    for j in range(grid_dim):
        full_count:int = 0
        for i in range(grid_dim):
            if is_full[grid[i][j]] == True:
                full_count += 1
        if full_count == grid_dim: #if all square in row are full
            j_list.append(j)
    #wait a moment before deleting any rows/columns
    if i_list != [] or j_list != []:
        sleep(0.25)
    #change color of full rows/columns to background color, update is_full and score
    for i in i_list:
        for j in range(grid_dim):
            grid[i][j].setFill(color_rgb(75, 89, 92))
            is_full[grid[i][j]] = False
            score += 1
            score_count.setText("Score: " + str(score))
            sleep(0.05)
    for j in j_list:
        for i in range(grid_dim):
            grid[i][j].setFill(color_rgb(75, 89, 92))
            is_full[grid[i][j]] = False
            score += 1
            score_count.setText("Score: " + str(score))
            sleep(0.05)
    return score

def gameOver(shape:list[tuple[int, int]], highlight_square:tuple[int, int], grid:list[list[Rectangle]], grid_dim:int, is_full:dict[Rectangle, bool], win_width:int, win_height:int, win:GraphWin, stars:Image) -> bool:
    """ Returns True if there is no space in the grid for the given shape, False otherwise.
    :param shape: (list[tuple[int, int]]) A list of tuples representing coordinates of squares in a shape
    :param highlight_square: (tuple[int, int]) Coordinates representing the darkened square in the shape
    :param grid: (list[list[Rectangle]]) A list of lists of graphics objects which form a grid
    :param grid_dim: (int) The number of squares in one row/column of the grid
    :param is_full: (dict[Rectangle, bool]) A dictionary with each square in the grid as a key, with value True if the square is full, False if empty
    :param win_width: (int) Width of the window, in pixels
    :param win_height: (int) Height of the window, in pixels
    :param win: (GraphWin) The window
    :param stars: (Image) A transparent image with stars
    :return : (bool) True if there is no space for the shape, False if there is space
    """
    #check placement error for each square in the grid
    for i in range(grid_dim):
        for j in range(grid_dim):
            if checkPlacementError(shape, highlight_square, grid, grid_dim, (i,j), is_full) == False:
             return False #if any square is a valid placement, then game not over
    #if game over, display game over message and falling stars
    message = Text(Point(-win_width//2, win_height//7), "GAME OVER")
    message.setFace("courier")
    message.setSize(36)
    message.setStyle("bold")
    message.setTextColor(color_rgb(219, 131, 131))
    message.draw(win)
    while message.getAnchor().getX() < 3*win_width//2:
        message.move(2, 0)
        stars.move(0,3)
        sleep(0.01)
    return True

if __name__ == "__main__":
    print(findSquare(100, 100, 700, 525, 315, 39))