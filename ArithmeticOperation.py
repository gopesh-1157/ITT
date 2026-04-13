a=int(input("enter number1:"))
b=int(input("enter number2:"))
print("""menu
      1.addition
      2.subtraction
      3.multiplication
      4.divison""")
c=int(input("enter your choice:"))
if c==1:
   print("sum of two numbers:",a+b)
elif c==2:
   print("difference of two numbers:",a-b)
elif(c==3):
   print("mul of two numbers:",a*b)
elif(c==4):
   print("division of two numbers",a/b)
else:
   print("invalid choice")
