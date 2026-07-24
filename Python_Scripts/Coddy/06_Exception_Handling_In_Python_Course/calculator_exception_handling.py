def calculator(n1, n2):
    try:
        div = n1 / n2
    except Exception as obj:
        print(obj)
    else:
        print(div)
