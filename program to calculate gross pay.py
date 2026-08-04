h=input('enter hours')
try:
    h=int(h)
except:
    print("Error, please enter numeric input")
    quit()
r=input('enter rate')
try:
    r=int(r)
except:
    print("Error, please enter numeric input") 
    quit()  
try:
    t=input("began over time at") 
    t=int(t)
except:
    print("Error, please enter numeric input")
    quit()
try:
    o=input("enter over time value")
    o=float(o)
except:
      print("Error, please enter numeric input")  
      quit()
if h<t:
    pay=h*r
    print ("gloss pay=", pay)
else :
    pay=t*r+(h-t)*o*r
    print("gloss pay=", pay)   


