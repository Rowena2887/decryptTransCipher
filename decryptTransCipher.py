# Transposition Cipher Decryption

import math

def main():
	myMessage = 'Cenoonommstmme oo snnio. s s c'
	myKey = 8
	
	plaintext = decryptMessage(myKey, myMessage)
	
	print(plaintext)

# The transposition decrypt function will simulate the "columns" and "rows" of the grid that the plaintext is written on by using a list of strings.
def decryptMessage(key, message):
	# The number of "columns" in the transposition grid:
	numOfColumns = int(math.ceil(len(message) / float(key)))
	# The number of "rows" in the grid:
	numOfRows = key
	# The number of "shaded boxes" in the last "column" of the grid:
	numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
	
	# Creating strings based on the number of columns in teh grid:
	plaintext = [''] * numOfColumns
	
	# Keeping track of the grid pointer.
	column = 0
	row = 0
	
	# Placing the letters accordingly on the grid.
	for symbol in message:
		plaintext[column] += symbol
		column += 1 # Point to the next column.
		
		# If there are no more columns or we are at a shaded box, go back to the first column and move on to the next row:
		if(column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
			column = 0
			row += 1
			
	return ''.join(plaintext)

main()
