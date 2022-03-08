from matplotlib import pyplot as plt

def line_graph(functions):
    """Plots a line graph"""

    plt.figure(figsize=(20, 11))
    data = []
    title = ""
    for function in functions:
        value = function()
        data.append(value)
    for values in data:
        plt.plot(values[0], values[1], marker=".", label=values[2])
        title += values[2] + ", "
        
    plt.title(f"India's total COVID-19 {title} Jan 2021 - Aug 2021")
    plt.xlabel("Months")
    plt.ylabel("Cases")
    plt.grid()
    plt.legend()
    plt.show()


 
