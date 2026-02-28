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
print(timerins)
