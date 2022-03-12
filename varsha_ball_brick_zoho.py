def setWaG(n):  #set wall and ground
    l=[[0]*n for i in range(n-2)]
    l.insert(0,['W']*n)
    l.append(['G']*n)
    for i in range(1,n):
        l[i][0],l[i][n-1]='W','W'
    l[n-1][n//2]='o'
    return l

def checker(l,n):
    for i in range(1,n-1):
        for j in range(1,n-1):
            if l[i][j]!=0:
                return False
    return True

def baseAdder(base_len,n):
    if base_len==n-2:
        return base_len
    return base_len+1

def baseChecker(l,bp,base,base_len):
    base=[bp]
    for i in range(base_len-1):
        if i%2==0:
            base.append(base[-1]+1)
        else:
            base.insert(0,base[0]-1)
    return base

def baseSetter(l,n,bp,base,base_len):
    for i in range(1,n-1):
        if i==bp:
            l[n-1][i]='o'
            continue
        if i in base:
            l[n-1][i]='_'
        else:
            l[n-1][i]='G'

def clearRow(l,n,r):
    for i in range(1,n-1):
        l[r][i]=0

def clearSurr(l,i,j):
    l[i][j]=0
    try:
        if l[i][j-1]!='W':
            l[i][j-1]=0
    except:
        pass
    try:
        if l[i-1][j-1]!='W':
            l[i-1][j-1]=0
    except:
        pass
    try:
        if l[i+1][j-1]!='W' and l[i+1][j-1]!='G':
            l[i+1][j-1]=0
    except:
        pass
    try:
        if l[i-1][j]!='W':
            l[i-1][j]=0
    except:
        pass
    try:
        if l[i+1][j]!='W' and l[i+1][j]!='G':
            l[i+1][j]=0
    except:
        pass
    try:
        if l[i-1][j+1]!='W':
            l[i-1][j+1]=0
    except:
        pass
    try:
        if l[i][j+1]!='W':
            l[i][j+1]=0
    except:
        pass
    try:
        if l[i+1][j+1]!='W' and l[i+1][j+1]!='G':
            l[i+1][j+1]=0
    except:
        pass
        
def travelSt(l,n,bp,base_len,base):
    i,j=n-2,bp
    while l[i][j]==0:
        i-=1
    if l[i][j]=='W':
        return base_len,base
    if l[i][j]=='B':
        l[i][j]=0
        base_len=baseAdder(base_len,n)
        base=baseChecker(l,bp,base,base_len)
    elif l[i][j]=='DE':
        clearRow(l,n,i)
    elif l[i][j]=='DS':
        clearSurr(l,i,j)
    else:
        l[i][j]-=1
    return base_len,base

def travelLd(l,n,c,bp,base_len,base):
    i,j=n-2,bp-1
    while l[i][j]==0:
        i-=1
        j-=1
    if l[i][j]=='W':
        j+=1
        while l[i][j]==0:
            j+=1
        if l[i][j]=='W':
            return c-1,bp,base_len,base
        if l[i][j]=='B':
            l[i][j]=0
            base_len=baseAdder(base_len,n)
            base=baseChecker(l,bp,base,base_len)
        elif l[i][j]=='DE':
            clearRow(l,n,i)
        elif l[i][j]=='DS':
            clearSurr(l,i,j)
        else:
            l[i][j]-=1
        if j in base:
            return c,j,base_len,base
        else:
            base=baseChecker(l,j,base,base_len)
            return c-1,j,base_len,base
    elif l[i][j]=='B':
        l[i][j]=0
        base_len=baseAdder(base_len,n)
        base=baseChecker(l,bp,base,base_len)
    elif l[i][j]=='DE':
        clearRow(l,n,i)
    elif l[i][j]=='DS':
        clearSurr(l,i,j)
    else:
        l[i][j]-=1
    if j in base:
        return c,j,base_len,base
    else:
        base=baseChecker(l,j,base,base_len)
        return c-1,j,base_len,base
    
def travelRd(l,n,c,bp,base_len,base):
    i,j=n-2,bp+1
    while l[i][j]==0:
        i-=1
        j+=1
    if l[i][j]=='W':
        j-=1
        while l[i][j]==0:
            j-=1
        if l[i][j]=='W':
            return c-1,bp,base_len,base
        if l[i][j]=='B':
            l[i][j]
            base_len=baseAdder(base_len,n)
            base=baseChecker(l,bp,base,base_len)
        elif l[i][j]=='DE':
            clearRow(l,n,i)
        elif l[i][j]=='DS':
            clearSurr(l,i,j)
        else:
            l[i][j]-=1
        if j in base:
            return c,j,base_len,base
        else:
            base=baseChecker(l,j,base,base_len)
            return c-1,j,base_len,base
    elif l[i][j]=='B':
        l[i][j]=0
        base_len=baseAdder(base_len,n)
        base=baseChecker(l,bp,base,base_len)
    elif l[i][j]=='DE':
        clearRow(l,n,i)
    elif l[i][j]=='DS':
        clearSurr(l,i,j)
    else:
        l[i][j]-=1
    if j in base:
        return c,j,base_len,base
    else:
        base=baseChecker(l,j,base,base_len)
        return c-1,j,base_len,base

def printer(l,n):
    for i in l:
        for j in i:
            print(str(j).center(2),end=' ')
        print()

n=int(input("Enter size of the NxN matrix : "))
l=setWaG(n)
base_len,base=1,[]
ch='Y'
while ch=='Y':
    i,j,k=input("Enter the brick's position and the brick type :").split()
    if int(i)==0 or int(j)==0 or int(j)==n-1:
        pass
    else:
        try:
            l[int(i)][int(j)]=int(k)
        except:
            l[int(i)][int(j)]=k
    ch=input("Do you want to continue(Y or N)?")
c=int(input("Enter ball Count :"))
#c is ball count
fg,bp=0,n//2
base.append(bp)
while c!=0:
    printer(l,n)
    print("Ball count :",c)
    if checker(l,n):
        fg=1
        break
    dir=input("Enter the direction in which the ball need to traverse :")
    if dir=='ST':
        base_len,base=travelSt(l,n,bp,base_len,base)
    elif dir=='LD':
        c,bp,base_len,base=travelLd(l,n,c,bp,base_len,base)
    elif dir=='RD':
        c,bp,base_len,base=travelRd(l,n,c,bp,base_len,base)
    elif dir=='e':
        break
    else:
        print("Invalid Input")
    baseSetter(l,n,bp,base,base_len)
if fg==1 or checker(l,n):
    print("You Win HURRAY..!!")
else:
    print("Game Over, You lost")
#printer(l,n)
#print("Ball count :",c)
    
