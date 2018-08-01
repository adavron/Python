def calculateSalary():
    hours = float(raw_input("Enter hours: "))
    rate = float(raw_input("Enter rate "))

    if hours <= 40:
        pay = hours * rate
    else:
        #hours > 40
        pay = hours * (rate * 1.5)

    return pay

print(calculateSalary())