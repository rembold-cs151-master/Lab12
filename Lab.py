# File: Lab.py

"""
Program to construct several lists and then compare them
against one another to check the accuracy of a finding.
"""

# You have some lists to define here initially
# Define them in the same order as in the guide
names = []
ages = []


# Then your predict_status function:
def predict_status( ):
    """
    Predicts the marital status depending on the age of the individual.

    Input:
        ages (list of ints): list of the individual ages

    Output:
        (list of booleans): list of True of False depending on if individual
                            is predicted to be married (True) or not (False)
    """
    pass




# Then another list to define
actual_status = []


# Your check_results function
def check_predictions( ):
    """
    Compares marital status predictions to actual status and outputs a nice
    tables summarizing the results.

    Input:
        names (list of str): a list of all the individual names
        predicted (list of bool): a list of the predicted marital statuses
        actual (list of bool): a list of the actual marital statuses

    Output:
        None, just printing to the screen
    """
    pass


if __name__ == "__main__":
    print(names)
    print(ages)
    
    # Uncomment the below after Part 2 finished
    # predicted = predict_status(ages)
    # print(predicted)

    # Uncomment the below after Part 3 finished
    # print(actual_status)

    # Uncomment the below afetr Part 4 finished
    # check_predictions(names, predicted, actual_status)




