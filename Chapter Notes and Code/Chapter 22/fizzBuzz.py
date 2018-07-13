def fizzBuzz(x):
    for i in range(0, x):
        print(i)
        if(i % 3 == 0):
            print('fizz')
        if(i % 5 == 0):
            print('Buzz')
fizzBuzz(100)

def fizzBuzz2():
    for i in range(1,100):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else :
            print(i)
fizzBuzz2()
