amount_due = 50
print(f"Amount Due: {amount_due}")
accepted_coins = [25, 10, 5]
while True:
    insert_coin = int(input("Insert Coin: "))
    if insert_coin in accepted_coins:
        amount_due = amount_due - insert_coin
    if amount_due <= 0:
        print(f"Change Owed: {abs(amount_due)}")
        break
    print(f"Amount Due: {amount_due}")


