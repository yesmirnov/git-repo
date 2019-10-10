revenue = int(input("Введите выручку в рублях: "))
expenses = int(input("Введите расходы для получения выручки в рублях: "))
employees = int(input("Введите число сотрудников: "))
# определение показателей работы фирмы
if revenue > expenses:
    profit = revenue - expenses
    profitability = profit / revenue
    profitability_per_person = profitability / employees
    print("Фирма работает прибыльно c общей рентабельностью: ", profitability, "\nc рентабельностью на сотрудника: ",
          profitability_per_person)
elif revenue == expenses:
    print("Фирма работает без прибыли!")
else:
    print("Фирма работает убыточно!")


