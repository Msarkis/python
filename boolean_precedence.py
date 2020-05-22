"""
1. not
2. and
3. or
"""
bool_output = True or not False and False
# True or True and False
print(bool_output)

bool_output_1 = 10==10 or not 10>10 and 10 > 10
print(bool_output_1)

bool_output_2 = (10==10 or not 10>10) and 10 > 10
#True or True -> True and False -> False
print(bool_output_2)

bool_output3 = (10==10) or (not 10>10 and 10 > 10)
print(bool_output3)