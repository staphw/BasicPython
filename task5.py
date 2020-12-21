# -*- coding: utf-8 -*-

# Запросите у пользователя значения выручки и издержек фирмы. 
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). 
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). 
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

profit = int(input("Enter the profit value: "))
loss = int(input("Enter the loss value: "))

if profit > loss:
    print("The company operates with a profit. The profitability of the company is {:.2%}.".format((profit - loss) / profit))
    empl_num = int(input("Enter the number of employees: "))
    print("Profit per employee is {:.2}".format((profit - loss) / empl_num))
elif profit == loss:
    print("Profit equals loss")
else:
    print("The company operates at a loss.")