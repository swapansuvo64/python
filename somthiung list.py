playList=[]
print("Enter your 5 favorite plays\n")
for i in range(5):
    playName=input(f"play {i+1} : ")
    playList.append(playName)
print("\n Subscript value")
for i in range(len(playList)):
    print("%9d %-25s" %(i+1,playList[i]))
