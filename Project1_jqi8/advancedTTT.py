import copy
import sys
import datetime
import pdb
import numpy as np

state=[{1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}, {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}, {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}, {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}, {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}, {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}, {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}, {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}, {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}]+[{"next":'x','nextpos':['1','2','3','4','5','6','7','8','9'],'full':[]}]
action=[['1','2','3','4','5','6','7','8','9'],['1','2','3','4','5','6','7','8','9'],['1','2','3','4','5','6','7','8','9'],['1','2','3','4','5','6','7','8','9'],['1','2','3','4','5','6','7','8','9'],['1','2','3','4','5','6','7','8','9'],['1','2','3','4','5','6','7','8','9'],['1','2','3','4','5','6','7','8','9'],['1','2','3','4','5','6','7','8','9']]
choose='x'
computer='o'
nstate=copy.deepcopy(state)
naction=copy.deepcopy(action)
win_state=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
#print(len(action))
def playermove(nstate,naction):
	while 1:
		sys.stderr.write('Player turn to move, your piece is '+choose+'\n')
		a=sys.stdin.readline()[:-1]
		if len(a)!=2:
			print('2 numbers')
			continue
		if a[0] in nstate[9]["nextpos"]:
			if a[1] in naction[int(a[0])-1]:
				naction[int(a[0])-1].remove(a[1])
				nstate[int(a[0])-1][int(a[1])]=choose
				nstate[9]["next"]=computer
				if a[1] in nstate[9]["full"]:
					nstate[9]['nextpos']=['1','2','3','4','5','6','7','8','9']
					for j in range(len(nstate[9]['full'])):
						nstate[9]['nextpos'].remove(nstate[9]['full'][j])
				else:
					nstate[9]["nextpos"]=list(a[1])
				#print(nstate)
				#print(naction)
				break
			else:
				sys.stderr.write('invalid\n')
		else:
				sys.stderr.write('invalid\n')

def computermove(nstate,naction):
	while 1:
		a=absearch(nstate,naction)

		#a=sys.stdin.readline()[:-1]
		if len(a)!=2:
			sys.stderr.write('Input 2 numbers')
			continue
		if a[0] in nstate[9]["nextpos"]:
			if a[1] in naction[int(a[0])-1]:
				naction[int(a[0])-1].remove(a[1])
				nstate[int(a[0])-1][int(a[1])]=computer
				nstate[9]["next"]=choose
				if a[1] in nstate[9]["full"]:
					nstate[9]['nextpos']=['1','2','3','4','5','6','7','8','9']
					for j in range(len(nstate[9]['full'])):
						nstate[9]['nextpos'].remove(nstate[9]['full'][j])
				else:
					nstate[9]["nextpos"]=list(a[1])
				#print(nstate)
				#print(naction)
				sys.stderr.write("Computer take "+a+'\n')
				sys.stdout.write(a+'\n')
				break
			else:
				sys.stderr.write('invalid\n')
		else:
				sys.stderr.write('invalid\n')

def displaychecker(nstate):
	for i in range(3):
		sys.stderr.write(' '+str(nstate[i][1])+' | '+str(nstate[i][2])+' | '+str(nstate[i][3])+' ')
		if i!=2:
			sys.stderr.write('   ')
		else:
			sys.stderr.write('\n')
	for i in range(39):
		sys.stderr.write('-')
	sys.stderr.write('\n')
	for i in range(3):
		sys.stderr.write(' '+str(nstate[i][4])+' | '+str(nstate[i][5])+' | '+str(nstate[i][6])+' ')
		if i!=2:
			sys.stderr.write('   ')
		else:
			sys.stderr.write('\n')
	for i in range(39):
		sys.stderr.write('-')
	sys.stderr.write('\n')
	for i in range(3):
		sys.stderr.write(' '+str(nstate[i][7])+' | '+str(nstate[i][8])+' | '+str(nstate[i][9])+' ')
		if i!=2:
			sys.stderr.write('   ')
		else:
			sys.stderr.write('\n')
	sys.stderr.write('\n\n\n')
	for i in range(3):
		sys.stderr.write(' '+str(nstate[i+3][1])+' | '+str(nstate[i+3][2])+' | '+str(nstate[i+3][3])+' ')
		if i!=2:
			sys.stderr.write('   ')
		else:
			sys.stderr.write('\n')
	for i in range(39):
		sys.stderr.write('-')
	sys.stderr.write('\n')
	for i in range(3):
		sys.stderr.write(' '+str(nstate[i+3][4])+' | '+str(nstate[i+3][5])+' | '+str(nstate[i+3][6])+' ')
		if i!=2:
			sys.stderr.write('   ')
		else:
			sys.stderr.write('\n')
	for i in range(39):
		sys.stderr.write('-')
	sys.stderr.write('\n')
	for i in range(3):
		sys.stderr.write(' '+str(nstate[i+3][7])+' | '+str(nstate[i+3][8])+' | '+str(nstate[i+3][9])+' ')
		if i!=2:
			sys.stderr.write('   ')
		else:
			sys.stderr.write('\n')
	sys.stderr.write('\n\n\n')
	for i in range(3):
		sys.stderr.write(' '+str(nstate[i+6][1])+' | '+str(nstate[i+6][2])+' | '+str(nstate[i+6][3])+' ')
		if i!=2:
			sys.stderr.write('   ')
		else:
			sys.stderr.write('\n')
	for i in range(39):
		sys.stderr.write('-')
	sys.stderr.write('\n')
	for i in range(3):
		sys.stderr.write(' '+str(nstate[i+6][4])+' | '+str(nstate[i+6][5])+' | '+str(nstate[i+6][6])+' ')
		if i!=2:
			sys.stderr.write('   ')
		else:
			sys.stderr.write('\n')
	for i in range(39):
		sys.stderr.write('-')
	sys.stderr.write('\n')
	for i in range(3):
		sys.stderr.write(' '+str(nstate[i+6][7])+' | '+str(nstate[i+6][8])+' | '+str(nstate[i+6][9])+' ')
		if i!=2:
			sys.stderr.write('   ')
		else:
			sys.stderr.write('\n')
	sys.stderr.write('\n\n\n\n\n\n\n')

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

def headreferee(nstate):
	count=0
	for i in range(9):
		check=referee(nstate[i])
		if check=='draw!':
			if str(i+1) not in nstate[9]['full']:
				nstate[9]['full'].append(str(i+1))
			count+=1
			if count==9:
				return check
		elif check:
			return check
	return 0

def max_value(nstate,a,b,naction,limit):
	#print(1)
	check=headreferee(nstate)
	if check=="Computer wins":
		return heuristic()
	elif check=="Player wins":
		return heuristic()
	elif check=="draw!":
		return heuristic()
	else:
		if limit:
			v=-999999
			actions=getaction(nstate,naction)
			for key in actions:
				for i in range(len(actions[key])):
					#print(key)
					#print(actions[key][i])
					tstate=copy.deepcopy(nstate)
					taction=copy.deepcopy(naction)
					taction[int(key)-1].remove(actions[key][i])
					tstate[int(key)-1][actions[key][i]]=computer
					tstate[9]["next"]=choose
					tstate[9]["nextpos"]=list(actions[key][i])
					v=max(v,min_value(tstate,a,b,taction,limit-1))
					if v>=b:
						#print(v)
						return v
					a=max(a,v)
		else:
			#print(heuristic(nstate))
			return heuristic(nstate)
		#print(v)
		#print(v)
		return v

def heuristic(nstate):
	sum1=0
	for i in range(9):
		board=[0,0,0,0,0,0,0,0,0]
		for key in nstate[i]:
			if nstate[i][key]==choose:
				board[int(key)-1]=-1
			elif nstate[i][key]==computer:
				board[int(key)-1]=1
		test=np.array(board).reshape(3,3)
		#row
		for j in range(3):
			sum2=0
			for k in range(3):
				sum2+=test[j][k]
			if sum2==2:
				sum1+=2
			elif sum2==3:
				sum1+=100
			elif sum2==-2:
				sum1+=-2
			elif sum2==-3:
				sum1-=100
		#column
		for j in range(3):
			sum2=0
			for k in range(3):
				sum2+=test[k][j]
			if sum2==2:
				sum1+=2
			elif sum2==3:
				sum1+=100
			elif sum2==-2:
				sum1+=-2
			elif sum2==-3:
				sum1-=100
		#dia

		sum2=test[0][0]+test[1][1]+test[2][2]
		if sum2==2:
			sum1+=2
		elif sum2==3:
			sum1+=100
		elif sum2==-2:
			sum1+=-2
		elif sum2==-3:
			sum1-=100
		sum2=test[2][0]+test[1][1]+test[0][2]
		if sum2==2:
			sum1+=2
		elif sum2==3:
			sum1+=100
		elif sum2==-2:
			sum1+=-2
		elif sum2==-3:
			sum1-=100
	return sum1

def min_value(nstate,a,b,naction,limit):
	#print(0)
	check=headreferee(nstate)
	if check=="Computer wins":
		return heuristic()
	elif check=="Player wins":
		return heuristic()
	elif check=="draw!":
		return heuristic()
	else:
		if limit:
			v=999999
			actions=getaction(nstate,naction)
			for key in actions:
				for i in range(len(actions[key])):
					#print(key)
					#print(actions[key][i])
					tstate=copy.deepcopy(nstate)
					taction=copy.deepcopy(naction)
					taction[int(key)-1].remove(actions[key][i])
					tstate[int(key)-1][actions[key][i]]=choose
					tstate[9]["next"]=computer
					tstate[9]["nextpos"]=list(actions[key][i])
					v=min(v,max_value(tstate,a,b,taction,limit-1))
					if v<=a:
						#print(v)
						return v
					b=min(b,v)
		else:
			return heuristic(nstate)
		#print(v)
		return v

def absearch(nstate,naction):
	check=headreferee(nstate)
	if check=="Computer wins":
		v=500
	elif check=="Player wins":
		v=-500
	elif check=="draw!":
		v=0
	else:
		v=-999999
		act=0
		actions=getaction(nstate,naction)
		for key in actions:
			for i in range(len(actions[key])):
				tstate=copy.deepcopy(nstate)
				taction=copy.deepcopy(naction)
				taction[int(key)-1].remove(actions[key][i])
				tstate[int(key)-1][actions[key][i]]=computer
				tstate[9]["next"]=choose
				tstate[9]["nextpos"]=list(actions[key][i])
				tmp=min_value(tstate,-999999,999999,taction,5)
				#print(tmp)
				if v<=tmp:
					v=tmp
					act=key+str(actions[key][i])
		return act

		
def getaction(nstate,naction):
	result={}
	for i in range(len(nstate[9]['nextpos'])):
		result[nstate[9]['nextpos'][i]]=naction[int(nstate[9]['nextpos'][i])-1]
	return result

while 1:
	sys.stderr.write("A new game started!\n\n")
	state=[{1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}, {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}, {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}, {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}, {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}, {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}, {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}, {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}, {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}]+[{"next":'x','nextpos':['1','2','3','4','5','6','7','8','9'],'full':[]}]
	action=[['1','2','3','4','5','6','7','8','9'],['1','2','3','4','5','6','7','8','9'],['1','2','3','4','5','6','7','8','9'],['1','2','3','4','5','6','7','8','9'],['1','2','3','4','5','6','7','8','9'],['1','2','3','4','5','6','7','8','9'],['1','2','3','4','5','6','7','8','9'],['1','2','3','4','5','6','7','8','9'],['1','2','3','4','5','6','7','8','9']]
	choose='x'
	computer='o'
	nstate=copy.deepcopy(state)
	naction=copy.deepcopy(action)
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
		if nstate[9]['next']==choose:
			displaychecker(nstate)
			#print(heuristic(nstate))
			playermove(nstate,naction)
			check=headreferee(nstate)
			if check:
				sys.stderr.write(check+'\n')
				displaychecker(nstate)
				break
		else:
			begin=datetime.datetime.now()
			computermove(nstate,naction)
			end=datetime.datetime.now()
			sys.stderr.write("Runtime: "+str(end-begin)+" s\n")
			check=headreferee(nstate)
			if check:
				sys.stderr.write(check+'\n')
				displaychecker(nstate)
				break

