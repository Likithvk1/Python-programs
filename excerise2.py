import time
timestamp=time.strftime("%H:%M:%S")
print(timestamp)
recentime=int(time.strftime("%H"))
print(recentime)

# timestamp=int(time.strftime("%M"))
# print(timestamp)
# timestamp=int(time.strftime("%S"))
# print(timestamp)
if(4>recentime<12):
    print("Good morning Sir")
elif(4<recentime>12):
    print("Good afternoon Sir")
else:
    print("Good Evinig Sir")


