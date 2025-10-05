input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
input = input.replace(' ','')
input = input.lower()

if input == "42" or input == "forty-two" or input == "fortytwo":
    print("Yes")
else:
    print('No')
