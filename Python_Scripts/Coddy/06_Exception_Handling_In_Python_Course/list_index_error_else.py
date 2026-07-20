data = ["John", "United States", 22, True, 98.5]

def fetch(idx):
    try:
        ele = data[idx]
    except IndexError:
        print("Incorrect Index Number")
    else:
        print(ele)
