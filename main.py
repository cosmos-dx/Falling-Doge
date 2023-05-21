import turtle
import os
import random
import time

class Doge ():
    def __init__(self, master):
        self.master = master
        self.dggm = master
        self.master.register_shape("jaado\dogl.gif")
        self.master.register_shape("jaado\dogr.gif")
        self.master.register_shape("jaado\dog_hunter.gif")
        self.master.register_shape("jaado\chicken.gif")
        self.score = 0
        self.lives = 3
        self.player = turtle.Turtle()
        self.player.speed(0)
        self.player.shape("jaado\dogl.gif")
        self.player.color("white")
        self.player.penup()
        self.player.goto(0, -250)
        self.player.direction = "stop"

        self.perks = []
        self.prk()
        self.cons = []
        self.los()

        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.pen.write("Score: 0  Lives: 3", align="center", font=("Courier", 24, "normal"))
        self.master.listen()
        self.master.onkeypress(self.go_left, "Left")
        self.master.onkeypress(self.go_right, "Right")
        self.gmeloop()
        
    def prk (self,):
        for _ in range(20):
            self.perk = turtle.Turtle()
            self.perk.speed(0)
            self.perk.shape("jaado\chicken.gif")
            self.perk.color("green")
            self.perk.penup()
            self.perk.goto(-100, 250)
            self.perks.append(self.perk)

    def los(self,):
        for _ in range(8):
            self.con = turtle.Turtle()
            self.con.speed(0)
            self.con.shape("jaado\dog_hunter.gif")
            self.con.color("red")
            self.con.penup()
            self.con.goto(100, 250)
            self.cons.append(self.con)

    def go_left(self,):
        self.player.direction = "left"
        self.player.shape("jaado\dogl.gif")
    
    def go_right(self,):
        self.player.direction = "right"
        self.player.shape("jaado\dogr.gif")


    def gmeloop(self,):
        while True:
            self.master.update()
            if self.player.direction == "left":
                self.player.setx(self.player.xcor() - 1)
            
            if self.player.direction == "right":
                self.player.setx(self.player.xcor() + 1)
                
            if self.player.xcor() < -390:
                self.player.setx(-390)
                
            elif self.player.xcor() > 390:
                self.player.setx(390)
                
            for self.perk in self.perks:
                self.perk.sety(self.perk.ycor() - 1)
            
                if self.perk.ycor() < -300:
                    self.perk.goto(random.randint(-300, 300), random.randint(400, 800))

                if self.player.distance(self.perk) < 40:
                    self.score += 10
                
                    self.pen.clear()
                    self.pen.write("Score: {}  Lives: {}".format(self.score, self.lives), align="center", font=("Courier", 24, "normal"))
                
                    self.perk.goto(random.randint(-300, 300), random.randint(400, 800))

            for self.con in self.cons:    
                self.con.sety(self.con.ycor() - 1)
            
                if self.con.ycor() < -300:
                    self.con.goto(random.randint(-300, 300), random.randint(400, 800))
            
                
                if self.player.distance(self.con) < 40:
                    self.score -= 10
                    self.lives -= 1

                    self.pen.clear()
                    self.pen.write("Score: {}  Lives: {}".format(self.score, self.lives), align="center", font=("Courier", 24, "normal"))
                    
                    time.sleep(1)
                    for self.con in self.cons:
                        self.con.goto(random.randint(-300, 300), random.randint(400, 800))
                
            if self.lives == 0:
                self.pen.clear()
                self.pen.write("Game Over! Score: {}".format(self.score), align="center", font=("Courier", 24, "normal"))
                self.master.update()
                time.sleep(5)
                self.score = 0
                self.lives = 3
                self.pen.clear()
                self.pen.write("Score: {}  Lives: {}".format(self.score, self.lives), align="center", font=("Courier", 24, "normal"))
                


    
def main():
    wn = turtle.Screen()
    wn.title("Doge")
    wn.bgcolor("black")
    wn.bgpic("jaado\idk.png")
    wn.setup(width=800, height=600)
    wn.tracer(0)
    Doge(wn)
    
if __name__ == "__main__":
    main()
