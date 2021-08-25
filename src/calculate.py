from src.error import input_error, calculation_error


def total_weigthing():
    max_percentage = 100
    total = 0
    weight_array = []
    name_array = []
    done = False

    # Get all the weightings up to 100 
    while not done:
        if total >= 100:
            print('###################################')
            print('Weighting complete, 100% entered')
            print('###################################\n')
            done = True
            break
        # Enter the name of the assignment and then enter weight
        name = input('Enter the name of the assignment: ')

        if type(name) is not str:
            raise(input_error)

        
        # If the user has finished inputting break from the loop
        if name.upper() == "DONE":
            done = True
            # if done is entered before any weight is typed in raise an error
            if len(weight_array) == 0:
                raise(input_error)
            break

        # Get the weight from the user
        weight = input("Enter weighting: ")
        print('If you have finished inputting weighting, type "DONE"\n')
        
        if type(weight) is not str:
            raise(input_error)
        
        # Check the type of what is being input
        if weight.isdigit():

            # Set the current name in name_array
            name_array.append(name)
            # Set the current weight in the weight_array
            weight_array.append(weight)
            # Iterate to the next array value and update for the while condition
            total = total + float(weight)

    # If the total weight is greater than 100 then raise an error
    if total > max_percentage:
        raise(calculation_error)


    # Return the total weighting of the courses that have been inputted
    # Return the weight_array to pass into the other functions to calculate marks left
    return total, weight_array, name_array

def total_marks(weight_array, name_array):
    total = 0
    done = False

    i = 0
    for name in name_array:
        # Get the weight from the user
        mark = input(f"Enter mark for {name}: ")
        print('If you have finished inputting your marks, type "DONE"\n')

        if type(mark) is not str:
            raise(input_error)


        # If user finished inputting, break from the loop
        if mark.upper() == "DONE":
            done = True
            break

        # Calculate based on the percentage given in weight_array
        tmp = float(mark) / float(weight_array[i])
        total = total + tmp
        i = i + 1
    return total


def desired_score():
    score = input('Enter your desired final grade: ')
    
    if type(score) is not str:
        raise(input_error)

    # if the score is not a digit then raise an error
    if score.isdigit():
        if float(score) < 100:
            return score
        if float(score) > 100:
            # If it is greater than 100 then this cannot be
            # raise a calculation error because max grade is 100
            raise(calculation_error)
        return score
    else:
        raise(input_error)
    
    

    
def remaining_weighting(current_weight):
    
    remaining = 0
    if current_weight != 100:
        remaining = 100 - current_weight
    else:
        remaining = 0
    
    return remaining

def remaining_marks(weight_left, mark_total, desired_mark):
    # Given weighting of the last assessment and the current total mark
    # See what is needed to get the desired mark

    remaining = 0
    total_percentage = 100

    # If they don't have to get any marks at all and it'll be fine
    if float(mark_total) >= float(desired_mark):
        return remaining
    
    # (desired mark * weight left) / mark = remaining marks needed
    remaining = (float(desired_mark) * float(weight_left))
    remaining = remaining/total_percentage

    return remaining
