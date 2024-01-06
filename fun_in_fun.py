#function in function
def fullName(firstName,lastName):
    fullN=firstName+" "+lastName
    return fullN
def welcome(name):
    print(f"hello, welcome {name}")
x=fullName("vikram","adhithya")
welcome(x)
welcome(fullName("d","j"))
