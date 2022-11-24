rezultat=[[0,0,0],[0,0,0],[0,0,0]]
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[9,8,7],[6,5,4],[3,2,1]]
def suma(A,B):
    rezultat=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(A)):
        for j in range(len(B)):
            rezultat[i][j]=A[i][j]+B[i][j]
    return(rezultat)
print(suma(A,B))
def produs(A,B):
    rezultat=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                rezultat[i][j]+=A[i][k]*B[k][j]
    return rezultat
print(produs(A,B))