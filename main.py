# AIM: Design a Python program to compute 
# the factorial of a given integer N.
# Coder:
# Date:

print("--- Factorial Finder ---\n")


# Write your code here

n = int(input("Enter Number: "))

if n<0:
    print("Factorial of",n,"is Not Defined")

else:
  fact=1
  for i in range(1,n+1):
    fact=fact*i
  print("Factorial of",n,"is",fact)
