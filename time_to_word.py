def word(x):
    unit = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    dec = ["", "ten", "twenty", "thirty", "forty", "fifty"]
    if x < 20:
        return unit[x]
    return dec[x/10] + " " + unit[x%10]

def minu(x):
    w = word(x)
    if x == 1: return w + " minute"
    else: return w + " minutes"

H = int(raw_input())
M = int(raw_input())

if M == 0:
    print "{} o' clock".format(word(H))
elif M == 15:
    print "quarter past {}".format(word(H))
elif M == 45:
    print "quarter to {}".format(word(H+1))
elif M == 30:
    print "half past {}".format(word(H))
elif M < 30:
    print "{} past {}".format(minu(M), word(H))
else:
    print "{} to {}".format(minu(60-M), word(H+1))
