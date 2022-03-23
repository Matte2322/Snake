from data import *

class GameScreen:
    def __init__(self, title, tracer, bgcolor):
        self.title = title
        self.tracer = tracer
        self.bgcolor = bgcolor
    
    def determineMeasurements(self, width, length):
        return screen.setup(width, length)

    def determineTitle(self):
        return screen.title(self.title)
    
    def determineTracer(self):
        return screen.tracer(self.tracer)

    def determineBgcolor(self):
        return screen.bgcolor(self.bgcolor)
    
# stuff output the class        
GameScreene = GameScreen("Snake Game", 0, 'turquoise')
GameScreene.determineTitle()
GameScreene.determineTracer()
GameScreene.determineBgcolor()

# border
def mainBorder():
    pen.hideturtle()
    pen.pensize(4)
    pen.penup()
    pen.goto(-310, 250)
    pen.pendown()
    pen.color('black')
    pen.forward(600)
    pen.right(90)
    pen.forward(500)
    pen.right(90)
    pen.forward(600)
    pen.right(90)
    pen.forward(500)
    pen.penup()
mainBorder()

def mainLoopWin():
    while True:
        try:
            GameScreene.determineMeasurements(700, 700)
        except:
            print("Closed the window.")
            break
mainLoopWin()