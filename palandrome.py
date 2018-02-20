x = input("Enter a string")
print x
if x[0] in  x[len(x)-1] and x[1] in x[len(x)-2]:
   print "Given string %s is palandrome"%x
else:
  print "Given string %s is not palandrome"%x
