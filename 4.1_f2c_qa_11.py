# convert f to c via user input

F = eval(input("Input Temperature in degrees F:"))
C = (F-32) * (5/9)
Converted_Temp = f'That is equivalent to {C:.2f} degrees C'
print(Converted_Temp)
