#def sum(arg1 = 1, arg2): # SyntaxError: non-default argument follows default argument
def sum(arg1, arg2 = 1):
   # arg2 default value = 1.
   total = arg1 + arg2
   print("Inside the function : ", total)
   return total

# Now you can call sum function
sum(3, 4)
sum(5); # Using default value for arg2.
sum(arg1 = 6)
#sum(arg2 = 7); # TypeError: sum() missing 1 required positional argument: 'arg1'
total = sum(8, 9)
print("Outside the function : ", total)

