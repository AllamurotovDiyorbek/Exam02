def deposit(balance:int, amount:int):
    if amount > 0:
        balance+=amount
        return balance
    else:
        return "amount katta bo`lsin 0 dan"
def withdraw(balance:int, amount:int):
    if 0<amount<=balance:
        balance-=amount
        return balance
    else:
        return "amount katta bo`lsin noldan va balansga teng yoki kichik bolsin"
def check_balance(balance:int):
    return balance
print(deposit(1000,300))