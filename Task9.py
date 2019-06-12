def count():
    count = 0
    a = (int(i) for i in input("Write ten numbers: ").split())
    for i in a:
        count += i
    print(count)
count()
