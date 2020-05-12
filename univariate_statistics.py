from two_column_text_read import data

from numpy import std, mean, column_stack
if len(data[0]) >= 1:
    if len(data[1]) >= 1:
        if len(data[0]) == len(data[1]):
            labels = ('StdDev(Y):', 'Mean(Y):', 'X-min:', 'X-max:', 'Y-min', 'Y-max')  # label printed stats
            stats = (std(data[1]), mean(data[1]), min(data[0]), max(data[0]), min(data[1]), max(data[1]))  # define stats
            fit_stats = column_stack((labels, stats))  # group labels with defined stats
            print(fit_stats)
else:
    print('Data has inappropriate dimensions')  # error checking



