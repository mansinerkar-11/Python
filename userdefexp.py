class InvalidUser(Exception):
    pass
user=int(input("Enter the Username:"))
try:
    if user<0:
        raise Invaliduser
except Invaliduser:
    print("Username is never zero")
try:
    if user != 123:
        raise Invaliduser
except Invalisuser:
    print("Username is not correct")
else:
    print("Username is correct")
