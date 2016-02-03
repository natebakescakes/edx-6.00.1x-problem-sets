balance = 320000
annualInterestRate = 0.2

monthly_interest_rate = annualInterestRate / 12.0
monthly_payment_lower = balance / 12
monthly_payment_higher = (balance * ((1 + monthly_interest_rate) ** 12)) / 12.0
epsilon = 0.01

while True:
    balance_new = balance
    monthly_payment = (monthly_payment_lower + monthly_payment_higher) / 2
    for month in range(0, 12):
        monthly_unpaid_balance = balance_new - monthly_payment
        balance_new = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance

    if abs(balance_new) <= epsilon:
        print('Lowest Payment: %.2f' % monthly_payment)
        break
    elif balance_new < 0: # too much monthly payment
        monthly_payment_higher = (monthly_payment_lower + monthly_payment_higher) / 2
    elif balance_new > 0: # needs more payments
        monthly_payment_lower = (monthly_payment_lower + monthly_payment_higher) / 2
