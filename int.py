class Account:
    name=""
    course=""
    subjects=""
    def __init__(self,account_no,account_name):
        self.account_no=account_no
        self.account_name=account_name
        

acc1=Account(12345,"test")
acc2=Account(123456,"test")
print(acc1.account_name)
print(acc2.account_no)
