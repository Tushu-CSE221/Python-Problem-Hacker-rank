str=input()
if any(char.isalnum() for char in str):
    print("True")
else:
    print("False")

if any(char.isalpha() for char in str):
    print("True")
else:
    print("False")
if any(char.isdigit() for char in str):
    print("True")
else:
    print("False")

if any(char.islower() for char in str):
    print("True")
else:
    print("False")
if any(char.isupper() for char in str):
    print("True")
else:
    print("False")