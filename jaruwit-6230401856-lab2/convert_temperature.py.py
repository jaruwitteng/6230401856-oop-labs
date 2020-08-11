correct_answer = False
while not correct_answer:
    try:
        fahrenheit = int(input("Enter temperature in Fahrenheit :"))
        celcius = (5 / 9) * (fahrenheit - 32)
        print("Temperature", fahrenheit, "in Fahrenheit is", ("{:.2f}".format(celcius)), "in Celcius")
    except ValueError:
        print("Please enter valid intergers for Fahrenheit")
    else:
        correct_answer = True
