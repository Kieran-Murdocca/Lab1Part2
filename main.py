# Author: Kieran Murdocca kkm5754@psu.edu
# Collaborator: Tanner Piotrowski tmp5779@psu.edu
# Collaborator: James Overmoyer jpo5322@psu.edu
temperature = float(input("Enter temperature: "))
unit = input("Enter unit in F/f or C/c: ")
if unit.upper() == "C": 
  Fahrenheit = temperature*9/5 + 32
  print(f"{temperature}{chr(176)} in Celsius is equivalent to {Fahrenheit}{chr(176)} Fahrenheit.")
elif unit.upper() == "F":
  Celsius = (temperature - 32)*5/9
  print(f"{temperature}{chr(176)} in Fahrenheit is equivalent to {Celsius}{chr(176)} Celsius.")
else:
  print(f"Invalid unit({unit}).")