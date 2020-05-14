import matplotlib.pyplot as plt


def plot_data_with_fit(data, fit_curve, data_format = '', fit_format = ''):
    combined_plot = plt.plot(data[:,0], data[:,1], data_format, fit_curve[:,0], fit_curve[:,1], fit_format)  # plotting the array data

    return combined_plot