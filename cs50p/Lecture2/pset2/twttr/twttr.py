input = input("Input: ")
output = input
wovels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for c in output:
    if c in wovels:
        output = output.replace(c, '')

print(f"Output: {output}")
