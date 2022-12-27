from tkinter import *
import random,time
screen = Tk()
screen.title('Game')
screen.resizable(False,False)
screen.wm_attributes('-topmost',1)
canvas = Canvas(screen,width=500,height=400,bd=0,highlightthickness=0)
canvas.pack()
screen.update()


class Ball:
    def __init__(self,canvas,color,platform,score):
        self.platform = platform
        self.canvas = canvas
        self.score = score
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.hit_bottom = False
    def hit_paddle(self,pos):
        platform_pos = self.canvas.coords(self.platform.id)
        if pos[2] >= platform_pos[0] and pos[0] <= platform_pos[2]:
            if platform_pos[1] <= pos[3] <= platform_pos[3]:
                self.score.hit()
                return True
        return False
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            canvas.create_text(250, 200, text ='Вы проиграли!', font=('Courier', 30), fill='red')
        if self.hit_paddle(pos):
            self.y = -3


        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

class Platform:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left )
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right )
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, event):
        self.x = -2

    def turn_right(self, event):
        self.x = 2


class Score:
    def __init__(self,canvas,color,):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(450, 10, text=self.score, font=('Courier' , 15), fill=color)

    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)

score = Score(canvas, 'green')
platform = Platform(canvas,'white')
ball = Ball(canvas,'red',platform,score)
while True:
    if not ball.hit_bottom:
        ball.draw()
        platform.draw()
    else:
        time.sleep(2)
        break
    screen.update_idletasks()
    screen.update()
    time.sleep(0.01)





