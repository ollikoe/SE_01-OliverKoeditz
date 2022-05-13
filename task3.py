# change value here
x = 5

playing_field = []
viable_inputs = []
viable_array_inputs = []



class colors:
    green = "\033[92m"
    red = "\033[91m"
    blue = "\033[94m"
    end = "\033[0m"

for i in range(x*x):
    # just to test, if winning works (if size of array is smaller, this might not make sense)
    if i in [1,2,3,7]:
        playing_field.append(1)
    else:
        playing_field.append(0)

    viable_inputs.append(i+1)
    viable_array_inputs.append(i)


def switch_onoff(fieldno):
    # red -> green
    if playing_field[fieldno] == 0:
        playing_field[fieldno] = 1

    # green -> blue
    elif playing_field[fieldno] == 1:
        playing_field[fieldno] = 2

    # blue -> off
    elif playing_field[fieldno] == 2:
        playing_field[fieldno] = 3

    # off -> red

    elif playing_field[fieldno] == 3:
        playing_field[fieldno] = 0

# Asking the user to type in a number. Breaks if number is viable
def get_input():
    while True:
        user_input = input("Please insert the number of the light you want to switch (1-" + str(x*x) + "):")
        try:
            if user_input in viable_inputs or int(user_input) in viable_inputs:
                return user_input
        except:
            ValueError

# looks which fields around the input are valid
def which_fields_to_switch(input_number):
    list = []

    number1 = input_number + 1
    number2 = input_number + x
    number3 = input_number - 1
    number4 = input_number - x

    # right
    if number1 in viable_array_inputs and (input_number + 1) / x != 0:
        list.append (input_number + 1)

    # top
    if number2 in viable_array_inputs and (input_number + 1) < x*x-x:
        list.append (input_number + x)

    # left
    if number3 in viable_array_inputs and (input_number + 1) % x != 1:
        list.append (input_number - 1)

    # bottom
    if number4 in viable_array_inputs and (input_number + 1) > x:
        list.append (input_number - x)

    return list


# returns true if all fields are 0
def winning():
    lights_turned_off = 0
    for i in playing_field:
        if i == 3:
            lights_turned_off += 1

    if lights_turned_off == x*x:
        return True
    else: return False

def display_field():
    # 1 and 0 -> ● and ○
    field = []

    # 0 red
    # 1 green
    # 2 blue
    # 3 off

    for i in playing_field:
        if i == 0:
            field.append(colors.red + "●" + colors.end)

        if i == 1:
            field.append(colors.green + "●" + colors.end)

        if i == 2:
            field.append(colors.blue + "●" + colors.end)

        if i == 3:
            field.append("○")
       
  
    #output


   
    #print("_______")

    
    
    for i in range(x):
        string = ""
        for j in range(x):        
            string += "|" + field[x*i+j]
        string += "|"
        print(string)
        
        

    #print("_______")


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

display_field()
print("You won!")



