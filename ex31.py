promptone = "Enter Hours: "
prompttwo = "Enter Rate: "
Hours = raw_input(promptone)
Rate = raw_input(prompttwo)
h = float(Hours)
r = float(Rate)
if h <= 40:
    pay = h*r
    print "Pay: ", pay

else:
    pay = (40*r) + ((h-40)*(r*1.5))
    print "Pay:", pay