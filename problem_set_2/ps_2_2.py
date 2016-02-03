balance = 320000
annualInterestRate = 0.2

monthly_interest_rate = annualInterestRate / 12.0
monthly_payment = 0

while True:
    balance_new = balance
    monthly_payment += 10
    for month in range(0, 12):
        monthly_unpaid_balance = balance_new - monthly_payment
        balance_new = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance

    if balance_new < 0:
        print('Lowest Payment: %d' % monthly_payment)
        break
