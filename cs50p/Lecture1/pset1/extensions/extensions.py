file = input("File name: ").lower().strip()

if file.endswith('.jpeg') or file.endswith('.jpg'):
    print("image/jpeg")
elif file.endswith('.png'):
    print("image/png")
elif file.endswith('.txt'):
    print("text/plain")
elif file.endswith('.pdf'):
    print("application/pdf")
elif file.endswith('.zip'):
    print("application/zip")
elif file.endswith('.gif'):
    print("image/gif")
else:
    print("application/octet-stream")
