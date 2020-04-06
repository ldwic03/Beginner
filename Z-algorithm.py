#Z-algorithm
s=input()
def Zalgo(s):
    L=len(s)
    Z=[0]*L
    Z[0]=L
    i=1;j=0
    while i<L:
        while i+j < L and s[j]==s[i+j]:j+=1
        Z[i]=j

        if j == 0:
            i+=1
            continue
        k=1
        while k<j and k+Z[k]<j:
            Z[i+k]=Z[k]
            k+=1
        i+=k
        j-=k
    return