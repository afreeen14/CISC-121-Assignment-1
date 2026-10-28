#1.Cyclic Rotation
def cyclic_rotation(A, K):
    for i in range(K):  #Repeats the rotation k times
        if len(A) > 0:
            last = A.pop()
            A.insert(0, last)  #inserts the last element to the front
    return A  #returns the rotated array

#2.Odd occurences in array
def odd_occurences(A):
    count={}
    for i in A:  #counts how many times each number appears
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for j in count:  #Finds the number which appears odd no.of times
        if count[j]%2!=0:
            return j
        
#3.Frog jump
def frog_jump(X,Y,D):  #where X=starting position, Y=position frog wants to reach and D=distance
    distance=Y-X
    jumps=distance//D
    if distance %D!=0:
        jumps+=1      #Adds one jump if there is a remaining distance
    return jumps

#4.Perm Missing Element
def perm_miss_elem(A):
    numbers=set(A)
    for i in range(1,len(A)+2):  #checks each possible number
        if i not in numbers:  #finds the missing number
            return i

#5.Perm check
def perm_check(A):
    numbers=set(A)
    for i in range(1,len(A)+1):
        if i not in numbers:
            return 0
    return 1
