def total(bill,tip):
    tip_amt=bill*(tip/100)
    total_amt=bill+tip
    print("bill amount",bill)
    print("tip percent",tip)
    print("tip amount",tip_amt)
    print("total bill amount",total_amt)
total(2000,10)    