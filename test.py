nstate={1:1,2:2,3:'x',4:'o',5:5,6:6,7:7,8:8,9:9}
board=[0,0,0,0,0,0,0,0,0]
for key in nstate:
	if nstate[key]=='x':
		board[key-1]=-1
	elif nstate[key]=='o':
		board[key-1]=1
print board