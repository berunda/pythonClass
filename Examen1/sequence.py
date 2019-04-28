from graphics import *
import math 
import time
import random

def displayWin(win):
	message = Text(Point(2,2), 'You Won!!')
	fill = Rectangle(Point(-1,-1), Point(5,5))
	fill.setFill('cyan')
	fill.draw(win)
	message.draw(win)
	time.sleep(3)

def main():
	win = setWindow()
	squares, texts, emptyIndex = populateSquaresAndTexts(win)
	scoreValue = initScore(win)
	movesLeft = 100
	errorMsg = initErrorMsg(win)
	answer = getValues()
	didWin = False

	while movesLeft > 0 and not didWin:
		if getStrings(texts) == answer:
			didWin = True
			displayWin(win)
		else:
			coords = win.getMouse()
			selectedIndex = getPosition(coords, squares)
			if isMoveValid(selectedIndex, emptyIndex):
				errorMsg.setText('')
				movesLeft -=1
				scoreValue.setText(str(movesLeft))
				move(squares,texts, selectedIndex, emptyIndex)
				emptyIndex = selectedIndex
			else:
				movesLeft -= 10
				if movesLeft > 0:
					scoreValue.setText(str(movesLeft))
					errorMsg.setText('Invalid Move')
				else:
					displayEnd(win)
					time.sleep(2)

def populateSquaresAndTexts(win):
	squares = []
	texts = []
	textValues = getShuffledTexts()
	count = 0
	emptyIndex = 0
	for i in range(3,-1,-1):
		for j in range(4):
			sqr = Rectangle(Point(j,i), Point(j+1,i+1))
			sqr.draw(win)
			squares.append(sqr)
			string = textValues[count]
			if textValues[count] == '':
				sqr.setFill('gray')
				emptyIndex = count
			text = Text(Point(j+0.5,i+0.5), string)
			text.draw(win)
			texts.append(text)
			count += 1

	return squares, texts, emptyIndex

def getPosition(point, squares):
	p1 = math.floor(point.getX())
	p2 = math.floor(point.getY())
	for i in range(16):
		point = squares[i].getP1()
		if (point.getX() == p1 and point.getY() == p2):
			return i
	return -1

def getValidMoves():
	return [
		[1,4],[0,2,5],[1,3,6],[2,7],
		[0,5,8],[1,4,6,9],[2,5,7,10],[3,6,11],
		[4,9,12],[5,8,10,13],[6,9,11,14],[7,10,15],
		[8,13],[9,12,14],[10,13,15],[11,14]
	]

def isMoveValid(squareIndex, emptyIndex):
	validMoves = getValidMoves()
	validMoves = validMoves[squareIndex]
	return emptyIndex in validMoves

def displayEnd(win):
	message = Text(Point(2,2), 'Sorry, You Died')
	fill = Rectangle(Point(-1,-1), Point(5,5))
	fill.setFill('cyan')
	fill.draw(win)
	message.draw(win)

def getValues():
	return ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','']

def getShuffledTexts():
	values = getValues()
	random.shuffle(values)
	return values

def getStrings(texts):
	strings = []
	for text in texts:
		strings.append(text.getText())
	return strings

def shuffle(texts):
	values = getValues()
	random.shuffle(values)
	i = 0
	emptyIndex = -1
	for text in text:
		text.setText(values[i])
		i += 1
		if values[i] == '':
			emptyIndex = i
	return emptyIndex

def setWindow():
	win = GraphWin('15 sequence game', 400,400)
	win.setBackground('white')
	win.setCoords(-1,-1,5,5)
	return win

def initScore(win):
	scoreText =  Text(Point(0,4.5), 'Score: ')
	scoreText.draw(win)
	scoreValue = Text(Point(0.6,4.5),'100')
	scoreValue.draw(win)
	return scoreValue

def initErrorMsg(win):
	errorMsg = Text(Point(2,4.5), '')
	errorMsg.setTextColor('red')
	errorMsg.draw(win)
	return errorMsg

def move(squares,texts, selectedIndex, emptyIndex):
	selectedSquare = squares[selectedIndex]
	selectedText = texts[selectedIndex]
	selectedString = selectedText.getText()
	selectedSquare.setFill('gray')
	selectedText.setText('')
	emptySquare = squares[emptyIndex]
	emptySquare.setFill('white')
	emptyText = texts[emptyIndex]
	emptyText.setText(selectedString)


# def populateSquaresAndTexts(win):
# 	squares = []
# 	texts = []
# 	count = 1
# 	for i in range(3,-1,-1):
# 		for j in range(4):
# 			sqr = Rectangle(Point(j,i), Point(j+1,i+1))
# 			sqr.draw(win)
# 			squares.append(sqr)
# 			string = str(count)
# 			if count == 16:
# 				string = ''
# 				sqr.setFill('gray')
# 			text = Text(Point(j+0.5,i+0.5), string)
# 			text.draw(win)
# 			texts.append(text)
# 			count += 1

# 	return squares, texts
main()