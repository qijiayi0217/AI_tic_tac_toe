import random

def referee(board):
	for key in board:
		for i in (1,2,3,4):
			if (key+i) in board and (key+i+i) in board:
				if board[key]==board[key+i] and board[key+i+i]==board[key]:
					if (key,key+i,key+i+i)==(1,3,5) or (key,key+i,key+i+i)==(2,4,6) or (key,key+i,key+i+i)==(2,3,4) or (key,key+i,key+i+i)==(3,4,5) or (key,key+i,key+i+i)==(4,6,8) or (key,key+i,key+i+i)==(5,6,7) or (key,key+i,key+i+i)==(6,7,8):
						pass
					else:
						return board[key]
	if len(board)==9:
		return 3
	return None





def check(board):
	check=referee(board)
	if check:
		if check==3:
			print("Tie!")
			return 1
		else:
			print(check+" wins!")
			return 1
	else:
		return 0

def input1(board):
	test=1
	while test:
		a=input("Please input: ")
		if a in input_space:
			test=0
	loc=int(a)
	for i in range(len(input_space)):
		if input_space[i]==a:
			del input_space[i]
			break
	board[loc]="player"

board={}
input_space=['1','2','3','4','5','6','7','8','9']
init=random.randint(0,1)
#print init
while 1:
	if init==1:
		input1(board)
		test=check(board)
		if test:
			break
		c_input=random.randint(0,len(input_space)-1)
		c_input=input_space[c_input]
		loc=int(c_input)
		board[loc]="computer"
		print("computer get: " + c_input)
		for i in range(len(input_space)):
			if input_space[i]==c_input:
				del input_space[i]
				break
		test=check(board)
		if test:
			break
	else:
		c_input=random.randint(0,len(input_space)-1)
		c_input=input_space[c_input]
		loc=int(c_input)
		board[loc]="computer"
		print("computer get: " + c_input)
		for i in range(len(input_space)):
			if input_space[i]==c_input:
				del input_space[i]
				break
		test=check(board)
		if test:
			break
		input1(board)
		test=check(board)
		if test:
			break





