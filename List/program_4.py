def fizzBuzz(n):
    three_table = list(map(lambda i: i*3, range(1, n+1)))
    five_table = list(map(lambda i: i*5, range(1, n+1)))

    for i in range(1, n+1):
        if i in three_table and i in five_table:
            print("FizzBuzz")
        elif i in three_table:
            print("Fizz")
        elif i in five_table:
            print("Buzz")
        else:
            print(i)


if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)