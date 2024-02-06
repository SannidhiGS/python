string=input("Enter a number:")
if string==string[::-1]:
    print("pallindrome")
else:
    print("not pallindrome")
for i in range(10):
    if string.count(str(i))>0:
        print(str(i),"appears",string.count(str(i)),"times")
