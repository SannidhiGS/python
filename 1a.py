m1=int(input("enter marks for test1:"))
m2=int(input("enter marks for test2:"))
m3=int(input("enter marks for test3:"))
if m1<=m2 and m1<=m3:
    avgmarks=(m2+m3)/2
elif m2<=m1 and m2<=m3:
    avgmarks=(m1+m2)/2
elif m3<=m1 and m3<=m2:
    avgmarks=(m1+m2)/2
print("the average marks of two test out of three test is",avgmarks)
             
