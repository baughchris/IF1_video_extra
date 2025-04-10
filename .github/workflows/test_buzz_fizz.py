    #Creating Fizz Buzz Criteria
#Fizz Buzz

for i in range(1, 101):
    #FizzBuzz
    if i % 5 == 0 and i % 3 == 0: 
        print("FizzBuzz")

    #Fizz
    elif i % 3 == 0:
        print("Fizz")

    #Buzz
    elif i % 5 == 0:
        print("Buzz")

    #None Of The Above
    else:
        print(i)