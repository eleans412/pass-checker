from error import input_error, calculation_error

def total_weigthing():
    max_percentage = 100
    total = 0
    weight_array = []
    name_array = []

    # Get all the weightings up to 100 
    i = 0
    while total is not max_percentage:

        # Enter the name of the assignment and then enter weight
        name = input('Enter the name of the assignment: ')

        # Get the weight from the user
        weight = input("Enter weighting: ")
        print('If you have finished inputting weighting, press ENTER')

        # If the user has finished inputting and the max_percentage has not been reached
        # break from the loop
        if weight == "\n":
            break
        
        # Set the current name in name_array
        name_array[i] = name
        # Set the current weight in the weight_array
        weight_array[i] = weight
        # Iterate to the next array value and update for the while condition
        total = total + weight

        # If the total weight is greater than 100 then raise an error
        if total > max_percentage:
            raise(calculation_error)
        
        i = i + 1

    # Return the total weighting of the courses that have been inputted
    # Return the weight_array to pass into the other functions to calculate marks left
    return total, weight_array, name_array

def total_marks(weight_array, name_array):
    total = 0
    done = False

    i = 0
    while not done:
        # Get the weight from the user
        mark = input(f"Enter mark for {name_array[i]}: ")
        print('If you have finished inputting your marks, press ENTER')

        # If user finished inputting, break from the loop
        if mark == "\n":
            done = True

        # Calculate based on the percentage given in weight_array
        tmp = mark / weight_array[i]
        total = total + tmp

        i = i + 1

    return total

def remaining_weighting(mark_total, weight_array):
    pass

def remaining_marks(weight_left, mark_total, desired_mark):
    # make sure to get the desired mark - need another function for this
    pass

def desired_score():
    pass