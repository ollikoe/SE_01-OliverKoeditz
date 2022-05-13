from operator import mod


playing_field = [1,1,1,0,1,0,0,0,0]

viable_inputs = [1,2,3,4,5,6,7,8,9]
viable_array_inputs = [0,1,2,3,4,5,6,7,8]

def switch_onoff(fieldno):
    if playing_field[fieldno] == 0:
        playing_field[fieldno] = 1
    else:
        playing_field[fieldno] = 0

# Asking the user to type in a number. Breaks if number is viable
def get_input():
    while True:
        user_input = input("Please insert the number of the light you want to switch (1-9):")
        try:
            if user_input in viable_inputs or int(user_input) in viable_inputs:
                return user_input
        except:
            ValueError

# looks which fields around the input are valid
def which_fields_to_switch(input_number):
    list = []

    number1 = input_number + 1
    number2 = input_number + 3
    number3 = input_number - 1
    number4 = input_number - 3

    # right
    if number1 in viable_array_inputs and (input_number + 1) / 3 != 0:
        list.append (input_number + 1)

    # top
    if number2 in viable_array_inputs and (input_number + 1) < 6:
        list.append (input_number + 3)

    # left
    if number3 in viable_array_inputs and (input_number + 1) % 3 != 1:
        list.append (input_number - 1)

    # bottom
    if number4 in viable_array_inputs and (input_number + 1) > 2:
        list.append (input_number - 3)

    return list


# returns true if all fields are 0
def winning():
    lights_turned_off = 0
    for i in playing_field:
        if i == 0:
            lights_turned_off += 1

    if lights_turned_off == 9:
        return True
    else: return False

def display_field():
    # 1 and 0 -> ● and ○
    field = []
    for i in playing_field:
        if i == 0:
            field.append("○")
        else: field.append("●")

    # create strings for output
    row1 = "|" + str(field[0]) + "|" + str(field[1]) + "|" + str(field[2]) + "|"
    
    row2 = "|" + str(field[3]) + "|" + str(field[4]) + "|" + str(field[5]) + "|"
  
    row3 = "|" + str(field[6]) + "|" + str(field[7]) + "|" + str(field[8]) + "|"
  
    #output

    print("_______")

    print(row1)
    print(row2)
    print(row3)

    print("_______")



# get all the fields that need to be switched and save them
while True:
    display_field()
    user_input = int(get_input())-1
    fields_to_switch = which_fields_to_switch(int(user_input))

    #print(fields_to_switch)

    #for every field in that list: switch it
    for i in fields_to_switch:
        #print(i)
        switch_onoff(i)
    switch_onoff(user_input)

    if winning() == True:
        break

print("You won!")





"""
_______
|○|○|○|
|○|○|○|
|○|○|○|
-------

●○

"""