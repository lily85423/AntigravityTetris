# ------------------------------------------------------
#        Name: Lily Mitchell, Caro Faust, & Greta Wang
#       Peers: N/A
#  References: N/A
# ------------------------------------------------------
from graphics import *
import grid
import shapemaker
from time import sleep

def startScreen(win:GraphWin, win_width:int, win_height:int) -> Point:
    """Displays the start screen in a given window, including a "how to play" button. Waits for click, then undraws the screen and returns clicked point.
    :param win: (GraphWin) The window
    :param win_width: (int) Window width in pixels
    :param win_height: (int) Window height in pixels
    :return : (Point) The point where the user clicked
    """
    hello = Image(Point(win_width/2, win_height/2), "images/Antigravity Tetris start screen.png")
    hello.draw(win)
    button = Rectangle(Point((3/8)*win_width, (23/32)*win_height), Point((5/8)*win_width, (26/32)*win_height))
    button.setFill(color_rgb(144, 188, 153))
    button.setOutline(color_rgb(144, 188, 153))
    button.draw(win)
    message = Text(Point((1/2)*win_width, (49/64)*win_height), "how to play")
    message.setFace("courier")
    message.setTextColor(color_rgb( 75, 89, 92))
    message.setSize(18)
    message.draw(win)
    click = win.getMouse()
    message.undraw()
    button.undraw()
    hello.undraw()
    return click

def howToPlay(win:GraphWin, win_width:int, win_height:int) -> None:
    """Displays an image with instuctions for playing the game. Waits for click, then undraws.
    :param win: (GraphWin) The window
    :param win_width: (int) Window width in pixels
    :param win_height: (int) Window height in pixels
    """
    image = Image(Point(win_width/2, win_height/2), "images/Antigravity Tetris how to play 2.png")
    image.draw(win)
    text1 = Text(Point((1/4)*win_width, (1/4)*win_height), "place the shapes by \nclicking where you want \nto put the darkened square")
    text1.setTextColor(color_rgb(170, 200, 204))
    text1.setSize(14)
    text1.setFace("courier")
    text1.draw(win)
    text2 = Text(Point((1/4)*win_width, (5/8)*win_height), "if you fill a row or column, \nit'll empty to make more space")
    text2.setTextColor(color_rgb(170, 200, 204))
    text2.setSize(14)
    text2.setFace("courier")
    text2.draw(win)
    text3 = Text(Point((1/4)*win_width, (3/4)*win_height), "game is over when you have \nno space for the next shape")
    text3.setTextColor(color_rgb(170, 200, 204))
    text3.setSize(14)
    text3.setFace("courier")
    text3.draw(win)
    text4 = Text(Point((3/4)*win_width, (1/8)*win_height), "click here anytime \nto quit")
    text4.setTextColor(color_rgb(170, 200, 204))
    text4.setSize(14)
    text4.setFace("courier")
    text4.draw(win)
    text5 = Text(Point((1/2)*win_width, (15/16)*win_height), "click anywhere to return to start")
    text5.setTextColor(color_rgb(170, 200, 204))
    text5.setSize(24)
    text5.setFace("courier")
    text5.draw(win)
    win.getMouse()
    text1.undraw()
    text2.undraw()
    text3.undraw()
    text4.undraw()
    text5.undraw()
    image.undraw()

def endScreen(win:GraphWin, win_width:int, win_height:int, score:int) -> Point:
    """Displays the end screen in a given window. Waits for click, then undraws the screen and returns clicked point.
    :param win: (GraphWin) The window
    :param win_width: (int) Window width in pixels
    :param win_height: (int) Window height in pixels
    :return : (Point) The point where the user clicked
    """
    goodbye = Image(Point(win_width/2, win_height/2), "images/Antigravity Tetris end screen.png")
    goodbye.draw(win)
    score_message = Text(Point((1/2)*win_width, win_height - 20), "Final score: " + str(score))
    score_message.setTextColor(color_rgb(170, 200, 204))
    score_message.setFace("courier")
    score_message.setSize(24)
    score_message.draw(win)
    click = win.getMouse()
    score_message.undraw()
    goodbye.undraw()
    return click

def main() -> None:
    """Makes a window in which it runs the game.
    """
    #Draw window
    win_width:int = 700
    win_height:int = int((3/4) * win_width)
    grid_dim:int = 8 #number of squares in one side of the grid
    win = GraphWin("Antigravity Tetris", win_width, win_height) 
    win.setBackground(color_rgb( 75, 89, 92))
    
    repeat:bool = True
    #Until user has closed the game
    while repeat == True:

        #Start screen
        start_click:Point = startScreen(win, win_width, win_height)
        start_click_x:float = start_click.getX()
        start_click_y:float = start_click.getY()
        #Display instructions if user clicks "how to play" button
        while (3/8)*win_width < start_click_x and start_click_x < (5/8)*win_width and (23/32)*win_height < start_click_y and start_click_y < (26/32)*win_height:
            howToPlay(win, win_width, win_height) #Waits for click before continuing
            start_click:Point = startScreen(win, win_width, win_height)
            start_click_x:float = start_click.getX()
            start_click_y:float = start_click.getY()

        #Add stars to background
        stars = Image(Point(win_width/2, win_height/2), "images/Antigravity Tetris stars.png") 
        stars.draw(win)

        #Set up the grid
        drawGrid_output:tuple = grid.drawGrid(win, win_width, win_height, grid_dim)
        big_grid:list =  drawGrid_output[0] #A list of the squares in the grid
        square_size:int =  drawGrid_output[1] #Number of pixels in one square
        grid_size:int =  drawGrid_output[2] #Number of pixels in one grid side
        is_full:dict = grid.makeIsFull(big_grid) #A dictionary with each square of the grid as a key and 'False' as each of the values.
        button:tuple = grid.makeButton(win, win_width) #Draws the quit button 

        #Start score count
        score:int = 0
        score_count = Text(Point((1/8)*win_width, win_height - 20), ("Score: " + str(score)))
        score_count.setTextColor(color_rgb(170, 200, 204))
        score_count.setFace("courier")
        score_count.setSize(24)
        score_count.draw(win)

        #Determining and drawing the first shape
        shape_info:tuple = shapemaker.randomShape() #Contains chosen_shape and shape_index
        chosen_shape:list = shape_info[0] #A list of (i,j) points representing how the shape will be constructed
        shape_index:int = shape_info[1] #The index of the shape in the list of possible shapes; necessary for choosing color
        color:tuple = shapemaker.assignColor(shape_index) 
        #Placing the shape in the window and designating a highlighted square
        shapemaker_output:tuple = shapemaker.shapeMaker(chosen_shape, int(win_width/5), int(win_height/3), square_size, win, color)
        highlight_square:tuple = (shapemaker_output[0], shapemaker_output[1])
        square_list:list = shapemaker_output[2] #Contains the graphics objects
       
        #Gameplay
        game_over:bool = False 
        while game_over == False: #While the user has not quit or run out of space
            click_point = win.getMouse()
            click_x:float = click_point.getX()
            click_y:float = click_point.getY()
            #Determines which square of the grid the user clicked in 
            click_square:tuple = shapemaker.findSquare(click_x, click_y, win_width, win_height, grid_size, square_size)
            #If they click outside the grid or click somewhere on the grid that the shape cannot fit
            if click_square == (-1, -1) or shapemaker.checkPlacementError(chosen_shape, highlight_square, big_grid, grid_dim, click_square, is_full) == True:
                #If they click the quit button
                if button[0] < click_x and click_x < button[2] and button[1] < click_y and click_y < button[3]:
                    game_over = True
            else:
                #If they click in a valid spot:
                shapemaker.moveShape(chosen_shape, highlight_square, big_grid, grid_dim, click_square, color, is_full)

                #Update score:
                for i in range(len(chosen_shape)):
                    score += 1
                    score_count.setText("Score: " + str(score))
                    sleep(0.05)

                #Undraws the graphic on the left side of the window
                shapemaker.shapeRemover(square_list)
                #Empties any full rows/columns and updates score accordingly
                score = shapemaker.destroy(big_grid, is_full, grid_dim, score, score_count)
                #Presenting the next shape
                shape_info:tuple = shapemaker.randomShape()
                chosen_shape:list = shape_info[0]
                shape_index:int = shape_info[1]
                color:tuple = shapemaker.assignColor(shape_index)
                shapemaker_output:tuple = shapemaker.shapeMaker(chosen_shape, int(win_width/5), int(win_height/3), square_size, win, color)
                highlight_square:tuple = (shapemaker_output[0], shapemaker_output[1])
                square_list:list = shapemaker_output[2]
                #Checks to see if there is space to put that shape
                game_over = shapemaker.gameOver(chosen_shape, highlight_square, big_grid, grid_dim, is_full, win_width, win_height, win, stars)
        shapemaker.shapeRemover(square_list)
        for i in range(grid_dim):
            for j in range(grid_dim):
                big_grid[i][j].undraw()
        stars.undraw()
        score_count.undraw()

        #End screen, wait for click
        end_click:Point = endScreen(win, win_width, win_height, score)
        end_click_x:float = end_click.getX()
        end_click_y:float = end_click.getY()
        #If user clicks button to close game
        if button[0] < end_click_x and end_click_x < button[2] and button[1] < end_click_y and end_click_y < button[3]:
            repeat = False
        #Undraw button
        button[4].undraw()
        button[5].undraw()


if __name__ == "__main__":
    main()