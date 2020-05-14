from numpy import std, mean


def univariate_statistics(data):
    statistics = (std(data[:,1]), mean(data[:,1]), min(data[:,0]), max(data[:,0]), min(data[:,1]), max(data[:,1]))  # define stats
    return statistics
