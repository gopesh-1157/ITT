ip=input("enter ip address:")
a=ip.split(".")
v=0
if len(a)==4:
   for i in range(len(a)):
      if int(a[i])>=0 and int(a[i])<=255:
         v=1

      else:
         v=0
         break
if v==0:
   print("invald")
else:
   print("valid")
