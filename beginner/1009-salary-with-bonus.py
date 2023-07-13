def salary_with_bonus():
    name = input()
    salary = float(input())
    sales = float(input())
    salary_with_bonus = salary + sales / 100 * 15
    print(f"TOTAL = R$ {salary_with_bonus:.2f}")


salary_with_bonus()
