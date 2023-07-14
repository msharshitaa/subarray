def subarray(A,B,C):
    return A[B:C+1]  
A=list(map(int,input().split()))
B=int(input("index of b:"))
C=int(input("index of c:"))
print(subarray(A,B,C))
