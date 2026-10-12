temp = float(input("enter the temperature in celsius    "))
Kelvin = temp + 273.15
Fahrenheit = temp * 1.80 + 32.00
print(f"Output: [{Kelvin:.}, {Fahrenheit:.5e}]")
print(f"Explanation: Temperature at {temp:.5e}°C is  {Kelvin:.5e} K and {Fahrenheit:.5e}°F.")