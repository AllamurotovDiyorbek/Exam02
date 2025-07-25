def calculate_tax(salary):
    if salary>5_000_000:
        return (salary/100*20)
    else:
        return (salary/100*13)
def calculate_net_salary(salary):
    return salary-calculate_tax(salary)
print(calculate_tax(5000000000))
print(calculate_net_salary(5000000000))