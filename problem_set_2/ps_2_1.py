balance = 5000
annualInterestRate = 0.12
monthlyPaymentRate = 0.02

for month in range(0, 12):
    unpaid = (1 - monthlyPaymentRate) * balance
    
    print ('Month: %d' % (month + 1))
    print ('Minimum monthly payment: %f' % round(monthlyPaymentRate * balance, 2))
    print ('Remaining balance: %f' % round(balance, 2))
    
    balance = unpaid * (1 + annualInterestRate / 12.0)