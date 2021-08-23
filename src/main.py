'''
Takes in the weightings for courses or activity that the user inputs

Calculates the total remaining grade or percentage needed to attain the desired mark
'''

from calculate import total_weigthing, total_marks, remaining_weighting, remaining_marks, desired_score


def main():

    # Print greeting message
    print('====================================================')
    print('           Welcome to pass calculator!')
    print('====================================================\n')

    # Call to input weighting
    res = total_weigthing()
    
    # Extract current weight and weight array
    current_weight = res[0]
    all_weights = res[1]
    names = res[2]

    # Calculate current total marks
    total_marks(all_weights, names)

    # Calculate remining weighting
    weight_left = remaining_weighting(all_weights)

    # Get desired final mark
    desired_mark = desired_score()

    # Calculate remaining marks
    mark_left = remaining_marks(weight_left, current_weight, desired_mark)

    # Print out the remaining marks

    # Print final message
    print('====================================================')
    print('        Thank you for using pass calculator!')
    print('====================================================\n')


if __name__ == "__main__":
    main()