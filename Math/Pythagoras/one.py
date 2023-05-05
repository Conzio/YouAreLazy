import math

i1 = input("Do you have 2 cathettas? y/n: ")

if i1.lower() != "y":
    IOne = float(input("Enter the length of cathetus a: "))
    ITwo = float(input("Enter the length of hypotenuse c: "))

    sum1 = IOne ** 2
    sum2 = ITwo ** 2
    sum3 = sum2 - sum1
    sum4 = math.sqrt(sum3)

    print(round(sum4, 5))
    print(round(sum4, 2))

else:
    IOne = float(input("Enter the length of cathetus a: "))
    ITwo = float(input("Enter the length of cathetus b: "))

    sum1 = IOne ** 2
    sum2 = ITwo ** 2
    sum3 = sum1 + sum2
    endsum = math.sqrt(sum3)

    print(round(endsum, 5))
    print(round(endsum, 2))
