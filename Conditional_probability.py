import random

random.seed(0)

totals = {20:0,30:0,40:0,50:0,60:0,70:0}
purchases = {20:0,30:0,40:0,50:0,60:0,70:0}

totalPurchases = 0

for _ in range(100000):
    agedecade = random.choice([20,30,40,50,60,70])
    purchase_probablity = float(agedecade)/100.0
    totals[agedecade] +=1
    if (random.random() < purchase_probablity):
        totalPurchases +=1
        purchases[agedecade]+=1




print totals
print '\n'
print purchases
print 'totalPurchases : '+ str(totalPurchases)

#lets find probablity

#PEF where E is purchases and F is  age decade

PEF =  float(purchases[30])/float(totals[30])

print 'probablity of purchase in 30s : P(purchase | 30s) : ', str(PEF)

PF = float(totals[30])/100000.0

print "p(30's) : ",PF