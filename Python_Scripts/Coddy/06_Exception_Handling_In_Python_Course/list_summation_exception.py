def summation(my_list):
    try:
        sum1 = 0
        for ele in my_list:
            sum1 = sum1 + ele
    except TypeError as obj:
        print(obj)
    else:
        print(sum1)
