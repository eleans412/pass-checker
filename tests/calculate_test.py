import pytest
from calculate import total_weigthing, total_marks, remaining_weighting, remaining_marks, desired_score
from src.error import input_error, calculation_error

# Test one weight
def test_one_weight():
    pass

# Test one mark
def test_one_mark():
    pass

# Test mutitple weightings
def test_multiple_weight():
    pass

# Test mutitple marks
def test_multiple_marks():
    pass


# Test calculations work with integer weightings
def test_int_weightings():
    # Set up weights with 
        # 30
        # 15
        # 15
        
    # 40 should be the resulting weight left - assert this
    # assert == 40.00
    pass

# Test calculations for float weightings
def test_float_weightings():
    # Set up weights with 
        # 30.63
        # 15.95
        # 15.00
        
    # 38.42 should be the resulting weight left - assert this
    # assert == 38.42
    pass

# Test passing mark result
def test_pass_mark_simple():
    # Set up weights with 
        # 20
        # 15
        # 15
    
    # 50 should be the resulting weight left - assert this
    # assert == 50.00

    # Set up marks for each respectively as
    # 70
    # 65
    # 95

    # Should show current grade is 76.0
    # assert == 76.0

    # Set desired grade to be 50

    # Grade needed to get 50 should be 24.0
    # assert == 24.0
    pass

def test_pass_mark_floats():
    # Set up weights with 
        # 20
        # 15
        # 15
    
    # 50 should be the resulting weight left - assert this
    # assert == 50.00

    # Set up marks for each respectively as
    # 76
    # 63
    # 94

    # Should show current grade is 77.5
    # assert == 77.5

    # Set desired grade to be 50

    # Grade needed to get 50 should be 22.5
    # assert == 22.5
    pass

# Test for invalid inputs
def test_invalid_input():
    # with pytest raises(input_error):
        # asjkkffakllksf
    pass

# Test calculation error in weighting
def test_calculate_error():

    #with pytest raises(calculation_error):
        # 600
    pass