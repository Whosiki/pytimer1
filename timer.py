import time
secvalue=0
tvalue=input("Input time hh:mm:ss ")
cutpos=tvalue.find(":")
htosvalue=int(tvalue[0:cutpos])*3600
tvalue=tvalue[cutpos + 1:]
cutpos=tvalue.find(":")
mtosvalue=int(tvalue[0:cutpos])*60
svalue=int(tvalue[cutpos + 1:])
timerins=htosvalue+mtosvalue+svalue
while timerins > 0:
    sec=timerins%60
    min=(timerins%3600 -sec)//60
    hr=timerins//3600
    print(f"\rRemaining time[{hr}:{min}:{sec}]",end="")
    timerins-=1
    time.sleep(1)
print("\r Time's up!!")
