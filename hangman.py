#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys

def checkIfInTheList(inputW, letterArr):
	if inputW.lower() in letterArr:
		return True
	else:
		print '#######################################'
		print "SORRY! You Do Not Have '%s' For Now" % (inputW)
		print '#######################################\n'
		return False

def printGuess(guessArr, wlen):
	print 'The word right now is ' 
	for num in range(0, wlen):
		print guessArr[num],

def printlist(letterArr):
	print '\nYour choices are' 
	print sorted(letterArr)

def checkGuess(wordArr, wlen, word, letterArr, die):
	for count in range (0, wlen):
			#print count
			#print word
			#print wordArr[count]
		if wordArr[count].lower() == word.lower():
			return count
	return 'notFound'

def replaceGuess(Arr, count, inputW, guess):
	#print hex(id(guessArr))
	if guess:
		Arr[count] = inputW
	else:
		Arr[count] = '#'

def ifWin(guessArr, wlen):
	for count in range (0, wlen):
		if guessArr[count] == '#':
			return False
	return 'win'

def main():
	print '\n################################'
	print " Welcome to Leo's Hangman World\n"
	words = sys.argv[1]
	try: lives = sys.argv[2]
	except: lives = '5'
	wlen = len(words)
	money = 0
	#print 'Your Life remaining ： ' + lives
	#print 'Your Current Money is ' + str(money)
	print 'The length of the word is ' + str(wlen)
	wordArr = [] 
	guessArr = []
	letterArr = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
	bonusArr = ['a','e','i','o','u']
	purchase = False
	Pvowel = ''
	bonusAvail = True
	for startp in range(0, wlen):
		guessArr.append('#')
		wordArr.append(words[startp])

	#printGuess(guessArr, wlen)

	play = True
	while play:
		print 'Your Life remaining ： ' + lives
		print 'Your Current Money is ' + str(money)
		printGuess(guessArr, wlen)
		if money >= 100 and bonusAvail:
			while True:
				inputB = raw_input("\n\nWould you like to pay $100 for a vowel letter, Please Type 'y' or 'n'\n")
				if inputB.lower() == 'n':
					break
				elif money < 100: 
					print 'Sorry You Do Not Have Enough Money'
					break
				elif inputB.lower() == 'y':
					while True:
						vowels = raw_input("Please pick a vowel letter from " +  str(bonusArr) +'\n')
						if ((vowels.lower() == 'a') or (vowels.lower() == 'e') or (vowels.lower() == 'i') or (vowels.lower() == 'o') or (vowels.lower() == 'u')) and (bonusArr.count(vowels.lower()) > 0):
							Pvowel = vowels.lower()
							letterArr.append(Pvowel)
							bonusArr.remove(Pvowel)
							if len(bonusArr) == 0:
								bonusAvail = False
							money = money - 100
							print 'Purchase Success, Your money has reduced to ' + str(money)
							break
						else:
							print "Incorrect Vowel Letter !\n"
					break
				else:
					print "Please Type either 'y' for Yes, or 'n' for No"

		
		printlist(letterArr)
		inputW = raw_input('\nPlease Give Me A Guess\n')
		#print 'input is ' + inputW
		die = 1
		removeWord = ''
		countw = wordArr.count(inputW)
		inList = checkIfInTheList(inputW, letterArr)
		if inList:
			while True:
					count = checkGuess(wordArr, wlen, inputW, letterArr, die)
					if not (count == 'notFound'):
						replaceGuess(guessArr, count, wordArr[count], True)
						replaceGuess(wordArr, count, wordArr[count], False)
						die = 0
					else:
						letterArr.remove(inputW.lower())	
						break
		else: 
			die = 2
		if die == 1:
			lives = str(int(lives) - 1)
			print 'Guessed Wrong! %d %s' % (countw, inputW) 
		if die == 0:
			money = money + 100
			print 'Good Job! %d %s' % (countw, inputW) 
		purchase = True
		finish = ifWin(guessArr, wlen)
		if int(lives) == 0:
			print '\nSORRY ! Please pay 2 bucks to retry'
			print '#########################################\n'
			break
		if (finish == 'win'):
			print '\n\nCongratulations ! You have survived'
			print '#########################################\n'
			break
		#print 'hi'			

if __name__ == '__main__':
	main()