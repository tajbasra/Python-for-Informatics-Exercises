def computepay(hours,rate):
    hours = raw_input("Enter hours: ")
    rate = raw_input("Enter rate: ")
    hours = float(hours)
    rate = float(rate)
    if hours <= 40:
        pay = hours*rate
        print "Pay: ", pay

    else:
        pay = (40*rate) + ((hours-40)*(rate*1.5))
        print "Pay:", pay

computepay(1,1)