def fizzbuzz(var):
    var = int(var)  # Convert input string to integer
    if var % 3 == 0 and var % 5 == 0:
        return "FizzBuzz"
    elif var % 3 == 0:
        return "Fizz"
    elif var % 5 == 0:
        return "Buzz"
    else:
        return var

if __name__ == "__main__":
    x = input("Enter an integer number: ")  # Prompt the user to input a number
    print(fizzbuzz(x))
