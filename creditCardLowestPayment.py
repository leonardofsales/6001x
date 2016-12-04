# Calcula o pagamento minimo mensal para quintar o balanco de um cartao de crédito em 12 meses

balance = 3926
annualInterestRate = 0.2

monthlyInterest = annualInterestRate / 12.0
testBalance = balance
minimumMonthly = 0

while (testBalance >= 0):
    previousBalance = balance
    minimumMonthly += 10
    for m in range (1, 13):
        monthlyUnpaidBalance = previousBalance - minimumMonthly
        updatedBalanceEachMonth = monthlyUnpaidBalance + (monthlyInterest * monthlyUnpaidBalance)
        previousBalance = updatedBalanceEachMonth
        if updatedBalanceEachMonth <= 0:
            testBalance = updatedBalanceEachMonth
            break
            
result = minimumMonthly
    
print ("Lowest Payment: " + str(result))