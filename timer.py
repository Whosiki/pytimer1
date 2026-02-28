import time
secvalue=0
tvalue=input("Input time hh:mm:ss ")
cutpos1=tvalue.find(":")
htosvalue=int(tvalue[0:cutpos1])*3600
tvalue=tvalue[cutpos1 + 1:-1]
