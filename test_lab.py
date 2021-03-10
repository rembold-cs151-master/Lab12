"""
Tests for Marital Status Lab
"""

import pytest
import Lab

def test_can_create_lists():
    assert Lab.names == ["Liam", "Emma", "Oliver", "Sophia", "Elijah", "Charlotte", "Ben", "Mia", "Mason", "Evelyn"],\
                    "Something is off in your list of names. Did you capitalize and spell correctly?"
    
    assert Lab.ages == [43, 26, 16, 31, 39, 32, 19, 18, 24, 34],\
                    "Something is off in your list of ages. Did you mistype something or miss a number?"

    assert Lab.actual_status == [False, True, False, False, False, True, True, False, False, True],\
                    "Something is off in your list of actual statuses. Did you skip one or flip the True and Falses?"


def test_predict_status():
    inputs = [Lab.ages, [46,29,31,15]]
    sols = [[True, False, False, True, True, True, False, False, False, True], [True, True, True, False]]
    for i,s in zip(inputs, sols):
        student = Lab.predict_status(i)
        assert type(student) == list, "You are not returning a list from predict_status?"
        assert type(student[0]) == bool, "The elements of the returned list should be booleans."
        assert student == s, f"With inputs of {i}, your returned list was {student}, but {s} was expected."


def test_check_predictions(capsys):
    i1 = [Lab.names,]
    i2 = [[True, False, False, True, True, True, False, False, False, True],]
    i3 = [Lab.actual_status,]
    sol_list = [[0,0,1,0,0,1,0,1,1,1],]
    for names, predicted, actual,sols in zip(i1, i2, i3, sol_list):
        Lab.check_predictions(names, predicted, actual)
        cap = capsys.readouterr().out.splitlines()
        for i,(line,sol) in enumerate(zip(cap,sols)):
            assert line.strip()[0] == chr(9744 + sol), f"{names[i]} should have predicted {predicted[i]} and actually been {actual[i]}, which would result in a {chr(9744+sol)} symbol, but you are printing a {line.strip()[0]} symbol at the start of the line?"
