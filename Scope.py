# # Builtin scope : You can use this scope anywhere.
# # print("Aditi")
# # a = 90
# # len(a)

# # Global scope : You can use this scope anywhere in the file.
# # Local scope : You can use this scope anywhere in the class.

# x=1
# def foo():
#     global x
#     x=10
#     y=11
#     print("Print X : ",x)
#     print("Print Y : ",y)


# foo()
# print("print X",x)




x=1
def foo():
    print(x)    # Error here 
    x=22
  
foo()
