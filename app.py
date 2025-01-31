#Question 1
def parallel(Resistors):
    
    total_inverse = sum(1 / r for r in Resistors)  # Compute the sum of reciprocals
    total_resistance = 1 / total_inverse  # Take the reciprocal to get the total resistance
    print('%.3f' %total_resistance, "ohms")  # Print the result

parallel([100,25,30])


#Question 2
def potential_divider(voltage, resistance):

    total_resistors= sum(resistance)

    for r in resistance:
        voltage_drop = voltage * (r / total_resistors)
        print('%.2f' % voltage_drop, "v")

potential_divider(9, [3000, 1000])

#Question 3
def temperature_check(temp, unit):
    if unit == "C":
        if temp < 35:
            print("The patient is hypothermic.")
        elif temp > 38:
            print("The patient is hyperthermic.")
        else:
            print("The patient has normal body temperatire.")
    elif unit == "F":
        if temp < 95:
            print("The patient is hypothermic.")
        elif temp > 100.4:
            print("The patient is hyperthermic.")
        else:
            print("The patient has normal body temperature.")

temperature_check(37, "C" )