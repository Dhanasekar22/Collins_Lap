def set_float_structure(value):
    # Convert the float to a string representation for parsing
    value_str = "{:.2f}".format(value).rstrip('0').rstrip('.')  # Remove trailing zeros and unnecessary decimal point
    integer_part, _, decimal_part = value_str.partition('.')

    # Determine the tens and ones digits
    tens = int(integer_part[:-1]) if len(integer_part) > 1 else 0  # All but the last digit
    ones = int(integer_part[-1])  # Last digit of the integer part
    tenth = int(decimal_part) if decimal_part else 0  # Decimal part as a two-digit number

    print(type(tens))

    # Print the structured output
    print("Tens_Digit_1.setValue({})".format(tens))
    print("Ones_Digit_1.setValue({})".format(ones))
    print("Tenth_Digit_1.setValue({})".format(tenth))


set_float_structure(7.50) 

# In Take off:

# 1.  HStab_Trim_Actual_Valid is TRUE
# 2. (HStab_Trim_TakeoffInhibit or HStab_Trim_MLG_WOW) is TRUE
# 3. (Green_Band_Limit_Valid is FALSE) and ((HStab_Trim_Actual_Value >= HSTAB_TRIM_IN_TAKEOFF_RANGE_MIN) and (HStab_Trim_Actual_Value <= HSTAB_TRIM_IN_TAKEOFF_RANGE_MAX))
#                                                                         or 
#     (Green_Band_Limit_Valid is TRUE) and ((HStab_Trim_Actual_Value >= Green_Band_Lower_Limit_Value) and ( HStab_Trim_Actual_Value <= Green_Band_Upper_Limit_Value))


# Out of Take Off:


# 1. HStab_Trim_Actual_Valid is TRUE

# 2. (HStab_Trim_TakeoffInhibit or HStab_Trim_MLG_WOW) is TRUE

# 3. (Green_Brand_Limit_Valid is False) AND ((Hstab_Trum_Actual_Value < HSTAB_TRIM_IN_TAKEOFF_RANGE_MIN) OR(Hstab_Trim_Actual_Value > HSTAB_TRIM_IN_TAKEOFF_RANGE_MAX)) 
# 																				OR
#    (Green_Brand_Limit_Valid is True) AND ((Hstab_Trum_Actual_Value < Green_Band_Lower_Limit_Value) OR(Hstab_Trum_Actual_Value > Green_Band_Upper_Limit_Value ))