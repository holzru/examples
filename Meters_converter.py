def meters(x):
def meters(x):
    print x
    if x >= 10**24:
        print "{}Ym".format(int(x)/10**24 if float(x)/10**24 == int(x)/10**24 else float(x)/10**24)
    elif 10**24 > x >= 10**21:
        print "{}Zm".format(int(x)/10**21 if float(x)/10**21 == int(x)/10**21 else float(x)/10**21)
    elif 10**21 > x >= 10**18:
        print "{}Em".format(int(x)/10**18 if float(x)/10**18 == int(x)/10**18 else float(x)/10**18)
    elif 10**18 > x >= 10**15:
        print "{}Pm".format(int(x)/10**15 if float(x)/10**15 == int(x)/10**15 else float(x)/10**15)
    elif 10**15 > x >= 10**12:
        print "{}Tm".format(int(x)/10**12 if float(x)/10**12 == int(x)/10**12 else float(x)/10**12)
    elif 10**12 > x >= 10**9:
        print "{}Gm".format(int(x)/10**9 if float(x)/10**9 == int(x)/10**9 else float(x)/10**9)
    elif 10**9 > x >= 10**6:
        print "{}Mm".format(int(x)/10**6 if float(x)/10**6 == int(x)/10**6 else float(x)/10**6)
    elif 10**6 > x >= 10**3:
        print "{}km".format(int(x)/10**3 if float(x)/10**3 == int(x)/10**3 else float(x)/10**3)
    else:
        print "{}m".format(x)

meters(7000000000000000000000000)
meters(1000000000000)
meters(1230000000000)
meters(1230000000)
meters(1230000)
meters(1230)
meters(123)
