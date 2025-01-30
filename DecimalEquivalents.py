# Program to print the decimal equivalent of 1/2 to 1/10

for i in range(2, 11):  # Loop from 2 to 10
    decimal_value = 1 / i  # Calculate the decimal equivalent
    print(f"1/{i} = {decimal_value:.5f}")  # Print the result with 5 decimal places
