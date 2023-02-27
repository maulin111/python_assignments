numbers = [0, 1, 2, 3, 4, 25, 98, 101, 5, 6, 7, 8, 9, 10, 20, 30, 45]
for num in numbers:
    if num <= 30:
        if num % 2 == 0:
            print(num)
            print("The number is even")
        else:
            print(num)
            print("The number is odd")
