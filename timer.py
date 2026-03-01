import time
secvalue=0
state=True
allowed_set = set("1234567890:")
cutpos=-1
htosvalue=0
while state:
    tvalue=input("Input time hh:mm:ss ")
    dot_counted= tvalue.count(":")
    outoforder= set(tvalue)-allowed_set
    if not outoforder and dot_counted<=2:
        state=False
if dot_counted !=0:
    if dot_counted == 2:
        cutpos=tvalue.find(":")
        htosvalue=int(tvalue[0:cutpos])*3600
    tvalue=tvalue[cutpos + 1:]
    cutpos=tvalue.find(":")
    mtosvalue=int(tvalue[0:cutpos])*60
    svalue=int(tvalue[cutpos + 1:])
    timerins=htosvalue+mtosvalue+svalue


while timerins >= 0:
    sec=timerins%60
    min=(timerins%3600 -sec)//60
    hr=timerins//3600
    print(f"\rRemaining time[{hr}:{min}:{sec}]",end="")
    timerins-=1
    time.sleep(1)
print("Time's up!!")
