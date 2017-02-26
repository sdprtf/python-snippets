##invest = 88200
##count = 63
##ret = 1800
##rate = 0.0055
##invite = (invest - ret) * rate
##gain = count * 30 + ret + invite
##m1 = invest - gain - invest / 7 + invite
##m2 = m1 - invest/7
##m3 = m2 - invest/7
##m4 = m3 - invest/7
##m5 = m4 - invest/7
##m6 = m5 - invest/7
##
##print 2*gain / ((m1+m2+m3+m4+m5+m6)/6.0)*100.0,'%'


invest = 28000
count = 70
ret = 500
rate = 0.0055
invite = (invest - ret) * rate
gain = count * 3 + ret + invite
m1 = invest - gain - invest / 4 + invite
m2 = m1 - invest / 4
m3 = m2 - invest / 4

print 4 * gain / ((m1 + m2 + m3) / 3.0) * 100.0,'%'
