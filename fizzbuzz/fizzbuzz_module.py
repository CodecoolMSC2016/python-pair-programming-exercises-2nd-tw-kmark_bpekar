def fizzbuzz(number):
    if ((number % 3) == 0) and ((number % 5) == 0):
       return "FizzBuzz"
       
    elif number % 5 == 0:
        return "Buzz"

    elif number % 3 == 0:
        return "Fizz"

    return number 


def main():
    for i in range(0,101):
        print(fizzbuzz(i)) 

if __name__ == '__main__':
    main()

