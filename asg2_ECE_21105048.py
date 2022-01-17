#                            PROGRAM1
print('             Program 1\n')

string=input("Enter the string:\n")
# a.
length=len(string)
print("A. Length of the entered string=",length,"\n")
# b.
rev=string[::-1]
print("B. Reverse of the string:-\n",rev,"\n")
# c.
new_string=string[slice(10,35,1)]
print("C. Sliced string:-\n",new_string,"\n")
# d.
str2=string.replace("a case sensitive","object oriented")
print("D. String after replacement:-\n",str2,"\n")
# e.
index=string.index("a")
print("E. Index of 'a' in the sring: ",index,"\n")
# f.
string.replace(" ","")
print("F. String after removal of WHITESPACES:-\n",string)









#                        PROGRAM2
print("\n\n                  Program 2\n")

name="Pranzal Sharma"
SID=21105048
dept="ECE"
cgpa=9.9

intro="Hey, {} Here!\nMy SID is {}\nI am from {} department and my CGPA is {}"
print(intro.format(name,SID,dept,cgpa))









#                      PROGRAM3
print("\n\n                 Program 3\n")
a=56
b=10
print("A. a&b=",a&b)
print("B. a|b=",a|b)
print("C. a^b=",a^b)
print("D.\n a after left shift by 2 bits=",a<<2,"\n b after left shift by 2 bits=",b<<2)
print("E.\n a after right shift by 2 bits=",a>>2,"\n b after right shift by 4 bits=",b>>4)









#                     PROGRAM4
print("\n\n                 Program 4\n")
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
num3=float(input("Enter the third number: "))

if num1==num2==num3:
    print("All the entered numbers are same")
if num1>=num2 and num1>=num3:
    print("The Greatest Number is: ",num1)
elif num2>=num1 and num2>=num3:
    print("The Greatest Number is: ",num2)
else:
    print("The Greatest Number is: ",num3)









#                        PROGRAM5
print("\n\n                 Program 5\n")

Str=input("Enter the String:\n")
if "name" in Str:
    print("Yes, the string includes 'name'")
else:
    print("No, the string does not include 'name'")









#                       PROGRAM6
print("\n\n                 Program 6\n")

side1=float(input("Length of first side="))
side2=float(input("Length of second side="))
side3=float(input("Length of third side="))

if side1>=side2+side3 or side2>=side1+side3 or side3>=side1+side2:
    print("No, Triangle can't be made.")
else:
    print("Yes, Triangle can be made.")
