def salary():
    number = int(input())
    hours = int(input())
    amount = float(input())
    salary = hours * amount
    print(f"NUMBER = {number}\n" + f"SALARY = U$ {salary:.2f}")


salary()
