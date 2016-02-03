balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

total_paid = 0

for month in range(0, 12): # 12 months or 1 year
    print ('Month: %d' % (month + 1))

    total_paid += (monthlyPaymentRate * balance)
    print ('Minimum monthly payment: %.2f' % (monthlyPaymentRate * balance))

    unpaid = (1 - monthlyPaymentRate) * balance
    balance = unpaid * (1 + annualInterestRate / 12.0)

    print ('Remaining balance: %.2f' % balance)

print ('Total paid: %.2f' % total_paid)
print ('Remaining balance: %.2f' % balance)
