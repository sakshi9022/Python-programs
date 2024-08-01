container=[2,1,4,5,5,4,4,1,1]
count =0 # count =1
even =0 #even =1
odd =0  #odd=
for i in container:#i=0;2,1:1,@:4,3:5,4:5
    if i==4:
        count = count+1
    elif i==2:
        even= even+1
    elif i==5:
        odd =odd+1
print(count-even)#
print(count-odd)#

container = [2,1,4,5,5,4,4,1,1]
count =0  # count = 3
even =0   # even = 1
odd =0    # odd = 2
for i in container: #i=0:2, 1:1, 2:4, 3:5, 4:5
    if i==4:
        count = count+1
    elif i==2:
        even= even+1
    elif i==5:
        odd= odd+1
print(count-even)#2
print(count-odd) #1