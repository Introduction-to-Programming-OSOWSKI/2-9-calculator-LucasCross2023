def calculator(exprestion, x, y):
    if exprestion == ("add"):
        return x + y
    elif exprestion ==  ("subtract"):
        return x - y
    elif exprestion == ("multiply"):
        return x * y
    elif exprestion == ("divide"):
        return x / y

print(calculator("multiply", 10, 3))