
totalbill = float(input("Enter the total bill amount: "))
amountpaid = float(input("Enter the amount paid: "))


if amountpaid >= totalbill:
    dueamount = 0  
    print("No due. Customer has paid in full.")
else:
    dueamount = totalbill - amountpaid
    print("Due amount:", dueamount)
