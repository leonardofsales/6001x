# Calcula o valar final do balanco de um cartao de credito com
# balanco inicial, taxa de juros anual e taxa de pagamento mensal
#

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterest = annualInterestRate / 12.0
previousBalance = balance

for m in range(1, 13):
    minimumMonthly = monthlyPaymentRate * previousBalance
    monthlyUnpaidBalance = previousBalance - minimumMonthly
    updatedBalanceEachMonth = monthlyUnpaidBalance + (monthlyInterest * monthlyUnpaidBalance)
    previousBalance = updatedBalanceEachMonth

result = round(updatedBalanceEachMonth, 2)
    
print ("Remaining balance: ", result)