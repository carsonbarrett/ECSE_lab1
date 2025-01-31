#Question 1
def parallel(Resistors):
    
    total_inverse = sum(1 / r for r in Resistors)  # Compute the sum of reciprocals
    total_resistance = 1 / total_inverse  # Take the reciprocal to get the total resistance
    print(total_resistance)  # Print the result

parallel([10,20,30])
