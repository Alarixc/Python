s={8,7,12,"Harry",[1,2]} #Not possible as code crashes right here when it sees a list in the set
s=list(s)
s[4][0]=6
s[4][1]=8
print(s)

