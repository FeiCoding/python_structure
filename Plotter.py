import matplotlib.pyplot as plt
from IPython.display import HTML, display
import tabulate


class Plotter:
    def __init__(self):
        self.table_plot = [[]]
        
    def diagram_plot(self, time, name, operation_name):
        fig, ax = plt.subplots()
        print(time)
        index = range(len(name))
        
        print(index)
        ax.bar(index, time)
        ax.set_xticks(range(len(name)))
        ax.set_xticklabels(name)
        ax.set_xlabel('Data Structure Name', weight='semibold')
        ax.set_ylabel('Time (Millisecond)', weight='semibold')
        ax.set_title(operation_name + " of Different Data Structure", fontsize=15)
        for a,b in zip(index, time):
            plt.text(a - 0.3, b + 0.0003, str(b))
        plt.show()
    
    def table_plot(self, time, name, operation_name):
        table_plot = [['Name', operation_name]]
        for i in range(len(name)):
            table_plot.append([name[i], time[i]])
        display(HTML(tabulate.tabulate(table_plot, tablefmt='html')))

