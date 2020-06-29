
import numpy as np
from scipy.ndimage.measurements import label

# Give option to user to play again or end game 
def replay():
	while True:
		again = input("Would you like to play again? (Please answer yes or no) \n")
		if again.lower() == "yes":
			main()
			break
		elif again.lower() == 'no':
			print ("Thank you for playing. Bye!")
			return
		else:
			print ("Invalid input, please try again")

# Process guesses and respond accordingly (compare user guesses to actual lengths)
def computesimilarity(riverlen, guessarr):
	auxarr = np.zeros(len(riverlen), dtype="bool")
	similar = 0
	for i in range(len(guessarr)):
		curr = guessarr[i]
		for k in range(len(riverlen)):
			if riverlen[k] == curr:
				if auxarr[k]:
					continue
				else:
					auxarr[k] = True
					similar += 1
					break
	ratio = (float(similar)/float(len(riverlen))) * 100
	print ("similarity score: ", ratio, "%")
	if similar == len(riverlen):
		print ("You are the winner")
	elif ratio >= 60:
		print ("You got second position")
	else:
		print ("Invest more money on Almonds, then come back")

# Get guesses from the user (number of guesses = number of unique rivers)
def getguesses(riverlen):
	guessarr = np.empty(len(riverlen), dtype="int")
	for i in range(len(riverlen)):
		while True:
			try:
				guess = int(input("Guess " + str(i+1) + ": " + "Guess the size of River \n"))
				guessarr[i] = guess
				break
			except ValueError:
				print ("Invalid input, please try again \n")
	guessarr.sort()
	return guessarr

# Identify all the unique connected components (clusters of 1) from the input matrix and populate a length array accordingly
def getriverlength(arr):
	cc, rivers = label(arr)
	riverlen = np.empty(rivers, dtype="int")
	for i in range(rivers):
		flattened = (cc == i+1).flatten()
		lencount = 0
		for k in flattened:
			if k:
				lencount += 1
		riverlen[i] = lencount
	riverlen.sort(axis=0)
	return riverlen

# Helper function to help with custom user generated input matrices
def matrixhelper(row, col):
	st = "Please enter elements for row " + str(row+1) + " seperated by a space (example --> 1 0 1 0 0) \n"
	while True:
		try:
			r = raw_input(st).split()
		except:
			print ("invalid input, please try again")
		if len(r) > col:
			print ("Please try again, too many elements input for the row (row capacity exceeded \n")
		elif len(r) < col:
			print ("Please try again, too few elements input for the row (row capacity not met \n")
		else:
			return np.array(r)

# Get the initial array either by default option or by allowing user to define his/her own matrix
def getarray():
	while True:
		choice = int(input("Input 1 for default matrix ; Input 2 for custom matrix: \n"))
		if choice == 1:
			return np.array([[1, 0, 0, 1, 0],[1,0,1,0,0],[0,0,1,0,1],[1,0,1,0,1],[1,0,1,1,0]])
		if choice == 2:
			while True:
				try:
					first, second = input("Please enter size of matrix seperated by a space (example --> 2 3) \n").split()
					break
				except ValueError:
					print ("Invalid input, please try again \n")
			a = np.zeros(shape=(int(first),int(second)))
			
			for i in range(int(first)):
				r = matrixhelper(i, int(second))
				a[i] = r

			return a
		else:
			print ("Invalid input, please try again \n")

# main function 
def main():
	initialmatrix = getarray()
	riverlengtharray = getriverlength(initialmatrix)
	guesses = getguesses(riverlengtharray)
	computesimilarity(riverlengtharray, guesses)
	replay()

main()
