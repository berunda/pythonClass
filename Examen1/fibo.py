from graphics import *
import math

def main():
  print('Welcome to the spiral program')
  h = int(input('Enter the desired screen height: '))
  w = (math.sqrt(5) + 1)/2 * h
  win = GraphWin('Fibonacci Spiral', w, h)

  r1 = h
  r2 = w-h 
  r3 = r1-r2
  r4 = r2-r3
  r5 = r3-r4
  r6 = r4-r5 

  c1 = Point(r1,r1)
  c2 = Point(r1,r2)
  c3 = Point(r1+r2-r3, r2)
  c4 = Point(r1+r2-r3, r2+r3-r4) 
  c5 = Point(r1+r2-r3-r4+r5, r2+r3-r4) 
  c6 = Point(r1+r2-r3-r4+r5, r2+r3-r4-r5+r6)

  p1 = Point(0,0)
  p2 = Point(w,0)
  p3 = Point(w,h)
  p4 = Point(h,h)
  p5 = Point(h,w-h)
  p6 = c3

  fib1 = Fibbo(win,r1,c1,p1)
  fib1.draw()
  fib2 = Fibbo(win,r2,c2,p2)
  fib2.draw()
  fib3 = Fibbo(win,r3,c3,p3)
  fib3.draw()
  fib4 = Fibbo(win,r4,c4,p4)
  fib4.draw()
  fib5 = Fibbo(win,r5,c5,p5)
  fib5.draw()
  fib6 = Fibbo(win,r6,c6,p6)
  fib6.draw()
  input()

class Fibbo:
  def __init__(self, win, r, c, p):
    self.win = win
    self.r = r
    self.c = c 
    self.p = p
    self.circ = Circle(self.c, self.r)
    self.rect = Rectangle(self.c, self.p)

  def draw(self):
    self.rect.setWidth(3)
    self.rect.draw(self.win)
    self.circ.setWidth(3)
    self.circ.draw(self.win)

  # def undraw(self):
  def drawRect(self):
    self.rect.setWidth(3)
    self.rect.draw(self.win)

  def drawCirc(self):
    self.circ.setWidth(3)
    self.circ.draw(self.win)

main()