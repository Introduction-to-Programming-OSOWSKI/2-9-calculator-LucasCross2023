def calculate(exprestion, x, y):
    if exprestion == ("add"):
        return x + y
    elif exprestion ==  ("subtract"):
        return x - y
    elif exprestion == ("multiply"):
        return x * y
    elif exprestion == ("divide"):
        return x / y

print(calculate("add", 2, 2))