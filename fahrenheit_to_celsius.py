#ToImprove: limit decimals to 2 decimals!

#declaring the input variable fahrenheit
fahrenheit = float(input("Enter the Temperature in F:"))

#declaring the celsius variable
celsius = (fahrenheit  -32) * 5/9
#round(celsius)
#not yet successfully limiting to 2 decimals
print(str(fahrenheit) + "degrees fahrenheit is equal to " + str(int(celsius)) + " degrees celsius.")



