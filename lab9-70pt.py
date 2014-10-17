############################################
#                                          # 
#                   70pt                   #
#                                          #
############################################

# Create a celcius to fahrenheit calculator.
# Multiply by 9, then divide by 5, then add 32 to calculate your answer.

# TODO:
# Ask user for Celcius temperature to convert
# Accept user input 
# Calculate fahrenheit
# Output answer

Celsius = float(input('Enter degree Celsius:  '))

Fahrenheit = (Celsius * 1.8) + 32 
print('%0.1f degree Celsius is eaqual to %0.1f degree Fahrenheit'  %(Celsius,Fahrenheit))