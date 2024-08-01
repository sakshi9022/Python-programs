import time
time.sleep(2)
n=int(input("Enter the number of rows: ")) 
for i in range(1,n+1): 
    print("* "*n)  

#------------------------------------------------

time.sleep(2)
n=int(input("Enter the number of rows: ")) #n=5
for i in range(1,n+1): #i=1  , n=6
    for j in range(1,n+1): # j=1
        print(i,end=" ")
    print()

#------------------------------------------------
time.sleep(2)
n=int(input("Enter the number of rows: ")) #5
for i in range(1,n+1): #i=1
    for j in range(1,n+1): #j=2
        print(chr(64+i),end=" ")
    print()

#-------------------------------------------------
time.sleep(2)
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n+1-i,end=" ")
    print()
time.sleep(2)
