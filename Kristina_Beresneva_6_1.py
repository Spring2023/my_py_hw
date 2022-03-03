from platform import python_version, processor

while True:
    s = input("What do you want to know? ")
    if s == "python version":
        print("Python version is:", python_version())
    elif s == "processor":
        print("Processor is:", processor())
    else:
        if s == "exit":
            break
