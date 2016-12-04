# Calcula o pagamento minimo mensal para quintar o balanco de um cartao de credito em 12 meses
# (Balance x (1 + Monthly interest rate)12) / 12.0

balance = 7000
annualInterestRate = 0.2

monthlyInterest = annualInterestRate / 12.0

lowBound = balance / 12.0
highBound = (balance * (1 + monthlyInterest)** 12) / 12.0
minimumMonthly = round((lowBound + highBound) / 2.0, 2)
epsilon = 0.01
updatedBalanceEachMonth = balance

while True:
    for m in range (1, 13):
        monthlyUnpaidBalance = updatedBalanceEachMonth - minimumMonthly
        updatedBalanceEachMonth = round((monthlyUnpaidBalance + (monthlyInterest * monthlyUnpaidBalance)), 2)
        
    if abs(updatedBalanceEachMonth) < epsilon:
        print("Lowest Payment:", round(minimumMonthly, 2))
        break
    else:
        if updatedBalanceEachMonth < 0:
            highBound = minimumMonthly
        elif updatedBalanceEachMonth > 0:
            lowBound = minimumMonthly
        minimumMonthly = (lowBound + highBound) / 2
        updatedBalanceEachMonth = balance