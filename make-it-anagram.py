s1=raw_input()
s2=raw_input()
str1=s1
str2=s2
for i in s1:
    for j in s2:
        if(i==j):
            str1=str1.replace(i,"")
            str2=str2.replace(j,"")
print len(str1)+len(str2)
