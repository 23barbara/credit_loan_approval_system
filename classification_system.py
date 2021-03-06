'''
the logistic regression model built with bank data
is implemented with the functions below
as a classification system
'''


# predictive function based on logistic model - returns likelyhood
def log_func(x):
    balance, credit, pay_status = x
    result = (0.6364 * balance) + (-0.05 * credit) + (0.2374 * pay_status)
    return result


def binary_classify(x): # takes int x = likelihood returns output int label
    x = round(x, 2)
    if x >= 0.50:
        return 1
    return 0


def predict(x): # makes credit predictions
    return binary_classify(log_func(x))


def print_result(x): # prints output to user
    if predict(x) == 1:
        return "Credit worthy"
    return "Not credit worthy"