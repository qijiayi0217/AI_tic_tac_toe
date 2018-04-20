import copy
import sys
import datetime
init_states={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,"next":"x"}
init_actions=['1','2','3','4','5','6','7','8','9']
choose="x"
computer="o"
moves=[]
now_state=copy.deepcopy(init_states)
now_actions=['1','2','3','4','5','6','7','8','9']
win_state=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
def playermove(now_state,now_actions):
	while 1:
		a=sys.stdin.readline()[:-1]
		if a in now_actions:
			now_actions.remove(a)
			now_state[int(a)]=choose
			now_state["next"]=computer
			break
		else:
			sys.stderr.write("Invalid position\n")

def printchecker(now_state):
	sys.stderr.write(" "+str(now_state[1])+" | "+str(now_state[2])+" | "+str(now_state[3])+" \n")
	sys.stderr.write("-----------\n")
	sys.stderr.write(" "+str(now_state[4])+" | "+str(now_state[5])+" | "+str(now_state[6])+" \n")
	sys.stderr.write("-----------\n")
	sys.stderr.write(" "+str(now_state[7])+" | "+str(now_state[8])+" | "+str(now_state[9])+" \n")

def referee(now_state):
	x=[]
	o=[]
	for i in range(1,10):
		if now_state[i]=='x':
			x.append(i)
		elif now_state[i]=='o':
			o.append(i)
	for i in range(len(x)-2):
		for j in range(i+1,len(x)-1):
			for k in range(j+1,len(x)):
				tmp=[x[i],x[j],x[k]]
				tmp.sort()
				#print(tmp)
				if tmp in win_state:
					if choose=="x":
						return "Player wins"
					else:
						return "Computer wins"
	for i in range(len(o)-2):
		for j in range(i+1,len(o)-1):
			for k in range(j+1,len(o)):
				tmp=[o[i],o[j],o[k]]
				tmp.sort()
				#print(tmp)
				if tmp in win_state:
					if choose=="x":
						return "Computer wins"
					else:
						return "Player wins"
	if (len(x)+len(o))==9:
		return "draw!"
	else:
		return 0

def computermove(now_state,now_actions):
		action,time=minimax_decision2(now_state,now_actions)
		a=action[1]
		sys.stderr.write(time)
		sys.stderr.write('Max value: '+str(action[0])+'\n')
		moves.append(a)
		sys.stderr.write('Computer takes: \n')
		sys.stdout.write(a+'\n')
		now_actions.remove(a)
		now_state[int(a)]=computer
		now_state["next"]=choose

'''

def minimax(now_state,now_actions,action):
	tmp_state=len(now_actions)*[copy.deepcopy(now_state)]
	tmp_actions=len(now_actions)*[copy.deepcopy(now_actions)]
	check=referee(now_state)
	if check=="Player wins":
		return [-1,action]
	elif check=="Computer wins":
		return [1,action]
	elif check=="draw!":
		return [0,action]
	else:
		if now_state["next"]==choose:
			tmp=[]
			for i in range(len(now_actions)):
				tmp_actions[i].remove(now_actions[i])
				tmp_state[i][int(now_actions[i])]=choose
				tmp_state[i]["next"]=computer
				tmp.append(minimax(tmp_state[i],tmp_actions[i],now_actions[i]))
			min1=2
			mid=[]
			for i in range(len(tmp)):
				if tmp[i][0]<min1:
					mid=tmp[i][:]
			return mid

		elif now_state['next']==computer:
			tmp=[]
			for i in range(len(now_actions)):
				tmp_actions[i].remove(now_actions[i])
				tmp_state[i][int(now_actions[i])]=computer
				tmp_state[i]["next"]=choose
				tmp.append(minimax(tmp_state[i],tmp_actions[i],now_actions[i]))
			max1=-2
			mid=[]
			for i in range(len(tmp)):
				if tmp[i][0]>max1:
					mid=tmp[i][:]
			return mid

def minimax2(now_state,now_actions):
	tmp_state=len(now_actions)*[copy.deepcopy(now_state)]
	tmp_actions=len(now_actions)*[copy.deepcopy(now_actions)]
	check=referee(now_state)
	if check=="Player wins":
		return -1
	elif check=="Computer wins":
		return 1
	elif check=="draw!":
		return 0
	else:
		if now_state["next"]==choose:
			tmp=[]
			for i in range(len(now_actions)):
				tmp_actions[i].remove(now_actions[i])
				tmp_state[i][int(now_actions[i])]=choose
				tmp_state[i]["next"]=computer
				tmp.append(minimax2(tmp_state[i],tmp_actions[i]))
			return max(tmp)

		elif now_state['next']==computer:
			tmp=[]
			for i in range(len(now_actions)):
				tmp_actions[i].remove(now_actions[i])
				tmp_state[i][int(now_actions[i])]=computer
				tmp_state[i]["next"]=choose
				tmp.append(minimax2(tmp_state[i],tmp_actions[i]))
			return min(tmp)

def minimax_decision1(now_state,now_actions):
	max1=-2
	action=0
	for element in now_actions:
		tmp_state=copy.deepcopy(now_state)
		tmp_actions=copy.deepcopy(now_actions)
		tmp_state['next']=choose
		tmp_state[int(element)]=computer
		tmp_actions.remove(element)
		tmp=(minimax2(tmp_state,tmp_actions),element)
		if tmp[0]>max1:
			max1=tmp[0]
			action=tmp[1]
	return action
'''
def max_value(now_state,now_actions):
	check=referee(now_state)
	if check=="Player wins":
		return -1
	elif check=="Computer wins":
		return 1
	elif check=="draw!":
		return 0
	else:
		v=-10
		for a in now_actions:
			tmp_state=copy.deepcopy(now_state)
			tmp_actions=copy.deepcopy(now_actions)
			tmp_state['next']=choose
			tmp_state[int(a)]=computer
			tmp_actions.remove(a)
			v=max(v,min_value(tmp_state,tmp_actions))
		return v

def min_value(now_state,now_actions):
	check=referee(now_state)
	if check=="Player wins":
		return -1
	elif check=="Computer wins":
		return 1
	elif check=="draw!":
		return 0
	else:
		v=10
		for a in now_actions:
			tmp_state=copy.deepcopy(now_state)
			tmp_actions=copy.deepcopy(now_actions)
			tmp_state['next']=computer
			tmp_state[int(a)]=choose
			tmp_actions.remove(a)
			v=min(v,max_value(tmp_state,tmp_actions))
		return v

def minimax_decision2(now_state,now_actions):
	begin=datetime.datetime.now()
	v=-10
	action=0
	for a in now_actions:
		tmp_state=copy.deepcopy(now_state)
		tmp_actions=copy.deepcopy(now_actions)
		tmp_state['next']=choose
		tmp_state[int(a)]=computer
		tmp_actions.remove(a)
		tmp=[min_value(tmp_state,tmp_actions),a]
		if tmp[0]>v:
			action=tmp[:]
			v=tmp[0]
	end=datetime.datetime.now()
	time='Search time: '+str(end-begin)+" s\n"
	return action,time

while 1:
	sys.stderr.write("A new game started!\n\n")
	init_states={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,"next":"x"}
	init_actions=['1','2','3','4','5','6','7','8','9']
	choose="x"
	computer="o"
	moves=[]
	now_state=copy.deepcopy(init_states)
	now_actions=['1','2','3','4','5','6','7','8','9']
	while 1:
		sys.stderr.write("Select your piece\n")
		select=sys.stdin.readline()[:-1]
		if select=='X' or select=="x":
			choose='x'
			computer='o'
			break
		elif select=='o' or select=="O":
			choose='o'
			computer='x'
			break
		else:
			sys.stderr.write("Invalid input\n")
	while 1:
		if now_state['next']==choose:
			printchecker(now_state)
			playermove(now_state,now_actions)
			check=referee(now_state)
			if check:
				sys.stderr.write(check)
				sys.stderr.write("\n")
				sys.stderr.write("Computer moves: "+', '.join(moves))
				sys.stderr.write("\n")
				printchecker(now_state)
				break
			else:
				pass
		elif now_state['next']==computer:
			computermove(now_state,now_actions)
			check=referee(now_state)
			if check:
				sys.stderr.write(check)
				sys.stderr.write("\n")
				sys.stderr.write("Computer moves: "+', '.join(moves))
				sys.stderr.write("\n")
				printchecker(now_state)
				break
			else:
				pass

















