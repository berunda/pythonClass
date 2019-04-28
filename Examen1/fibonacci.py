from graphics import *
import math

def main():
  print('Welcome to the spiral program')
  h = int(input('Enter the desired screen height: '))
  w = (math.sqrt(5) + 1)/2 * h
  win = GraphWin('Fibonacci Spiral', w, h)
  win.setCoords(0, 0, 13, 8)

  # step1
  circ = Circle(Point(8,0), 8)
  rect = Rectangle(Point(0,8), Point(8,0))
  draw(rect,circ,win)

  # step2
  rect = Rectangle(Point(8,3), Point(13,8))
  circ = Circle(Point(8,3), 5)
  draw(rect,circ,win)

  # step 3
  rect = Rectangle(Point(10,3), Point(13,0))
  circ = Circle(Point(10,3), 3)
  draw(rect,circ,win)

  # step 4
  rect = Rectangle(Point(8,2), Point(10,0))
  circ = Circle(Point(10,2),2)
  draw(rect,circ,win)

  # step 5
  rect = Rectangle(Point(8,3), Point(9,2))
  circ = Circle(Point(9,2),1)
  draw(rect,circ,win)
  input()

def draw(rect,circ,win):
  rect.setWidth(3)
  rect.draw(win)
  circ.setWidth(3)
  circ.draw(win)

main()
