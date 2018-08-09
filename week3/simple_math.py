from random import randint

def Maximum (num1):
    num1 = 1,2,3,4,5
    return Maximum(num1)

def Minimum(num2):
    num2 = 1,2,3,4,5
    return Minimum(num2)

def Range(num3):
    num3 = 1,2,3,4,5
    return Maximum(num1) - Minimum(num2)

def Average(num4):
    num4 = 1,2,3,4,5
    return Average(num4)

def main():
    numbers = []

    for i in range(30):
        numbers.append(randint(1,100))

print "The maximum value in numbers is {0}".format(Maximum(num1))
print "The minimum value in numbers is {0}".format(Minimum(num2))
print "The range of numbers is {0}".format(Range(num3))
print "The average of numbers is {0}".format(Average(num4))

main()
