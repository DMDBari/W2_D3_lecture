# Our football team has finished the championship.

# Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.

# For example: ["3:1", "2:2", "0:1", ...]

# Points are awarded for each match as follows:

# if x > y: 3 points (win)
# if x < y: 0 points (loss)
# if x = y: 1 point (tie)
# We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.

# Notes:

# our team always plays 10 matches in the championship


# input: list of 10 strings in the format "x:y"
# Output: our team's total points (need a way to track our points)
# we might use the "".split(":") and cas as ints to get scores
# we compare scores with if, elif, else
# add either 3 (win), 1 (tie), noting if loss
# print/return our total score


def solution(list_matches):
    total_points = 0
    for match in list_matches:
        x_y = []
        x_y = match.split(":")
        if int(x_y[0]) > int(x_y[1]):
            total_points += 3
        elif int(x_y[0]) == int(x_y[1]):
            total_points += 1
    return total_points