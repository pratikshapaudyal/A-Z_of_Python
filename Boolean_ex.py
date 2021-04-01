
def CheckBool(input_value: bool):
    if input_value == True:
        print(f"Input value is {bool(input_value)} of type: {type(input_value)}")
    elif input_value ==False:
        print(f"Input value is {bool(input_value)} of type: {type(input_value)}")
    elif not input_value:
        print(f"Input value is {bool(input_value)} and not a Boolean and is of type: {type(input_value)}")


x = True 
y = False
u = ""

CheckBool(y)