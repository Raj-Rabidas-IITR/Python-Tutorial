special = "!@#$%^&"
password = input("Create new password:") 

#FUNCTION FOR CHECKING SPECIAL CHARACTER
def contains_special_character(password, special):
    return any(char in special for char in password)

#FOR CHECKING LETTER
def contains_letter(password):
    return any(char.isalpha for char in password)
    
    
while not (contains_special_character(password, special) and contains_letter(password)):
    print("Password must contain at least one special character and one letter.")
    password = input("Create new password:")

print("Password is valid!")
