#Write a program that prints the numbers from 1 to 20. But for multiples of three print
#“Fizz” instead of the number and for the multiples of five print “Buzz”.
#For numbers which are multiples of both three and five print “FizzBuzz”.

for i in range(1,101):
    if i%15 ==0:
        print("fizzBuzz")
        print(i)
    elif i%5 ==0:
        print("Buzz")
        print(i)
    else:
        print("Fizz")
        print(i)
