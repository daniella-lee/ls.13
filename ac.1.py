def total_calc(bill_amount, tip_perc) :
    total=bill_amount*(1+0.01*tip_perc)
    total=round(total,2)
    print(f"pls pay ${total}")

total_calc(10003246326000232644768900,99356347676587938586)
