import time
secvalue=0
state=True
allowed_set = set("1234567890:")
cutpos=-1
htosvalue=0
typecheck=True
while state:
    tvalue=input("Input time hh:mm:ss ")
    dot_counted= tvalue.count(":")
    outoforder= set(tvalue)-allowed_set
    if not outoforder and dot_counted<=2 and len(tvalue)>=1:
        state=False
if dot_counted == 2:
    checkfornoth=True
    count=0
    tvalue=tvalue.split(":")
    while checkfornoth:
        if len(tvalue[count])==0:
            tvalue[count]=0
        count+=1
        if count==len(tvalue):
            checkfornoth=False
    timerins = int(tvalue[0])*3600 + int(tvalue[1])*60 + int(tvalue[3])
elif dot_counted == 1:
    checkfornoth = True
    count = 0
    tvalue = tvalue.split(":")
    while checkfornoth:
        if len(tvalue[count]) == 0:
            tvalue[count] = 0
        count += 1
        if count == len(tvalue):
            checkfornoth = False
    timerins = int(tvalue[0])*60 + int(tvalue[1])
else:
    while typecheck:
        ttype=input("What type? hour[1] minute[2] second[3]")
        checkfortype=set(ttype) - set("123")
        if not checkfortype and len(ttype)==1:
            typecheck=False
    if ttype==1:
        timerins=int(tvalue)*3600
    elif ttype==2:
        timerins=int(tvalue)*60
    else:
        timerins=int(tvalue)


while timerins >= 0:
    sec=timerins%60
    min=(timerins%3600 -sec)//60
    hr=timerins//3600
    print(f"\rRemaining time[{hr}:{min}:{sec}]",end="")
    timerins-=1
    time.sleep(1)
print("Time's up!!")
