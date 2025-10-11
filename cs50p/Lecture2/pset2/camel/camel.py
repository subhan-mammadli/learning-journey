camelCase = input("camelCase: ")
snake_case = camelCase
for c in snake_case:
    if c.isupper() and c is not snake_case[0]:
        snake_case = snake_case.replace(c, f"_{c}")

snake_case = snake_case.lower()


print(f"snake_case: {snake_case}")
