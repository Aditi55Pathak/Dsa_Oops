# In Python We use pass by object reference.

# We can not change int, float, String,tuple in python, as they are immutable.


def change(x):
    x = x + 1


a = 10
change(a)
print(a)

# We can  change list,dictionary,set in python, as they are mutable.


def changeHere(x):
    x.append("I am Aditi")


l = ["a", 89, 90.98]
changeHere(l)
print(l)
