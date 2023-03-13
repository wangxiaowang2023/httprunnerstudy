from random import randint


def game():
    a = randint(1, 9)
    b = randint(1, 9)
    answer = a + b
    print("%d+%d =" % (a, b))
    guess = int(input("你猜:"))
    if guess == answer:
        print("猜对了!")
    else:
        print("答案你:%d" % answer)


if __name__ == '__main__':
    print(game())
