#Rotate Matrix by 90 Degrees Clockwise

def rotate(mat):

    for r in range(len(mat)):
        for c in range(r, len(mat[r])):
            mat[r][c],mat[c][r]=mat[c][r],mat[r][c]
            
    for r in mat:
        left=0
        right=len(r)-1
        while right>left:
            r[left],r[right]=r[right],r[left]
            right+=1
            left+=1

    return mat
 
mat=[]
n=int(input())
for i in range(n):
    lis=list(map(int, input().split()))
    mat.append(lis)
print(rotate(mat))