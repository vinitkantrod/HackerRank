no = raw_input()
no = int(no)
mat = []
for i in range(no):
    mat.append(raw_input()[:no])
for i,j in zip(range(no),range(no)):
    if(i==0 or i==(no-1) or j==0 or j==(no-1)):
        continue
    else:
        for i,j in zip(range(1,no-1),range(1,no-1)):
            if((mat[i][j] > mat[i-1][j]) or (mat[i][j] > mat[i][j-1]) or (mat[i][j] > mat[i+1][j]) or (mat[i][j] > mat[i][j+1])):
                mat[i][j].replace(mat[i][j],'X')
print mat
