class Invalid(Exception):
    def _init_(self,msg):
        self.msg=msg
try:
    password=int(input("Enter Password:"))
    if (password !=1234):
        raise Invalid("Wrong Password Entered")
except Invalid as e:
    print("Error......",e)
else:
    print("Correct Password entered")
finally:
    print("Password Validation done")
