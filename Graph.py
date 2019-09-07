import matplotlib.pyplot as plt
import random

class Graph:
    figure = plt.figure()
    x_data = []
    y_data = []
    graph_reference = None

    def __init__(self):
        arr_size = random.randint(10, 100)

        self.y_data = self.generate_arr(self.y_data, arr_size)
        self.x_data = self.generate_arr_indexes(self.x_data, arr_size)
    
    def redraw_plot(self):
        """Redraws a matplotlib plot"""
        
        self.get_figure().canvas.draw()
        plt.pause(.001)

    def set_graph_reference(self, graph_reference):
        self.graph_reference = graph_reference

    def get_figure(self):
        return self.figure

    def generate_arr(self, arr, size):
        """Populates a list with random integers

            Parameters:
            arr (list[int]): An empty list to be populated
            size (int): Size of the list to be populated

            Returns:
            list[int]: Populated list  

        """

        for _ in range(size):
            arr.append(random.randint(1, 100))

        return arr   

    def generate_arr_indexes(self, arr, size):
        """Populates a list from 0 to parameter size

            Parameters:
            arr (list[int]): An empty list to be populated
            size (int): Size of the list to be populated

            Returns:
            list[int]: Populated list  

        """

        for i in range(size):
            arr.append(i)

        return arr    