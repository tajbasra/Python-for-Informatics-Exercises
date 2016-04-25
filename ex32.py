promptone = "Enter Hours: "
prompttwo = "Enter Rate: "

try:
    Hours = raw_input(promptone)
    h = float(Hours)
    Rate = raw_input(prompttwo)
    r = float(Rate)

    if h <= 40:
        pay = h*r
        print "Pay: ", pay


    else:
        pay = (40*r) + ((h-40)*(r*1.5))
        print "Pay:", pay           
except:
    print "Error, please enter numeric value"

