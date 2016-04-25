str = 'X-DSPAM-Confidence: 0.8475'
number = str.find(":")
newnumber = str[number+1:]
finalnumber = newnumber.strip()
x=float(finalnumber)
print x
