import numpy as np
import matplotlib.pyplot as plt
import random
from Graph import Graph

def is_sorted(arr):
    """Checks if a list is sorted

    Parameters:
    arr (list[int]): List of integers

    Returns:
    bool: Whether the list is sorted or not

   """

    for i in range(len(arr) - 1):
        if arr[i].get_height() > arr[i + 1].get_height():
            return False
    return True  

def bogo_sort(graph): 
    """Sorts a list with the bogo sort algorithm

    Parameters:
    graph (Graph) 

   """

    arr = graph.graph_reference

    while is_sorted(arr) == False:
        swap_1 = random.randint(1, len(arr) - 1)
        swap_2 = random.randint(1, len(arr) - 1)

        arr[swap_1].set_color('g')
        arr[swap_2].set_color('g')

        temp = arr[swap_1].get_height()
        arr[swap_1].set_height(arr[swap_2].get_height())
        arr[swap_2].set_height(temp)

        graph.redraw_plot()
        arr[swap_1].set_color('b')
        arr[swap_2].set_color('b')

    for i in range(len(arr)):
        arr[i].set_color('r')    

def bubble_sort(graph):
    """Sorts a list with the bubble sort algorithm

    Parameters:
    graph (Graph) 

   """

    arr = graph.graph_reference
    
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            arr[j].set_color('g')
            arr[j + 1].set_color('g')

            if arr[j].get_height() > arr[j + 1].get_height():
                temp = arr[j].get_height()
                arr[j].set_height(arr[j + 1].get_height())
                arr[j + 1].set_height(temp)

            graph.redraw_plot()
            arr[j].set_color('b')
        arr[len(arr) - i - 1].set_color('r') 

def insertion_sort(graph):
    """Sorts a list with the insertion sort algorithm

    Parameters:
    graph (Graph) 

   """

    arr = graph.graph_reference

    for i in range(1, len(arr)):
        key = arr[i].get_height()

        j = i - 1
        while j >= 0 and key < arr[j].get_height():
            arr[j + 1].set_color('g')
            arr[j + 1].set_height(arr[j].get_height())

            graph.redraw_plot()
            arr[j + 1].set_color('b')

            j -= 1
        arr[j + 1].set_height(key)

        arr[j + 1].set_color('g')  
        graph.redraw_plot()
        arr[j + 1].set_color('b')

def merge_sort(graph, arr):
    """Sorts a list with the merge sort algorithm

    Parameters:
    graph (Graph)
    arr (list[int]): List of integers  

   """

    arr_ref = graph.graph_reference

    if len(arr) > 1:
        mid = len(arr) // 2

        left_side = arr[:mid]
        right_side = arr[mid:]

        merge_sort(graph, left_side)
        merge_sort(graph, right_side)

        i = j = k = 0
        decrement_holder = None

        while i < len(left_side) and j < len(right_side):
            arr_ref[i].set_color('r')
            arr_ref[j].set_color('r')

            if left_side[i] < right_side[j]:
                arr[k] = left_side[i]
                arr_ref[k].set_height(left_side[i])
                i += 1

                decrement_holder = 'i'
                arr_ref[k].set_color('g')
            else:
                arr[k] = right_side[j]
                arr_ref[k].set_height(right_side[j])
                j += 1

                decrement_holder = 'j'
                arr_ref[k].set_color('g')
            k += 1
            graph.redraw_plot()

            if decrement_holder == 'i':
                arr_ref[i - 1].set_color('b')
                arr_ref[j].set_color('b')
            elif decrement_holder == 'j':
                arr_ref[j - 1].set_color('b')
                arr_ref[i].set_color('b')
            arr_ref[k - 1].set_color('b')

        while i < len(left_side):
            arr[k] = left_side[i]
            arr_ref[k].set_height(left_side[i])
            arr_ref[k].set_color('g')
            i += 1
            k += 1
            graph.redraw_plot()
            arr_ref[k - 1].set_color('b')

        while j < len(right_side):
            arr[k] = right_side[j]
            arr_ref[k].set_height(right_side[j])
            arr_ref[k].set_color('g')
            j += 1
            k += 1
            graph.redraw_plot()  
            arr_ref[k - 1].set_color('b')                                                                          

def main():
    print('Which sorting algorithm would you like to view: \n')
    print('1. Insertion Sort \n')
    print('2. Bubble Sort \n')
    print('3. Bogo Sort \n')
    print('4. Merge Sort \n')
    alg = input('Your choice: ')

    graph = Graph()
    ref = plt.bar(graph.x_data, graph.y_data, linewidth=1, alpha=0.4, edgecolor='b', color='b')
    graph.set_graph_reference(ref)

    plt.ylabel('Value')
    plt.xlabel('Index')

    if alg == '1':
        plt.title('Insertion Sort')
        win = graph.get_figure().canvas.manager.window
        win.after(100, insertion_sort(graph))
        plt.show()
    elif alg == '2':
        plt.title('Bubble Sort')
        win = graph.get_figure().canvas.manager.window
        win.after(100, bubble_sort(graph))
        plt.show()
    elif alg == '3':
        plt.title('Bogo Sort')
        win = graph.get_figure().canvas.manager.window
        win.after(100, bogo_sort(graph))
        plt.show()
    elif alg == '4':
        arr = []
        for i in range(len(graph.graph_reference)):
            arr.append(graph.graph_reference[i].get_height())

        plt.title('Merge Sort')
        win = graph.get_figure().canvas.manager.window
        win.after(100, merge_sort(graph, arr))
        plt.show()    
    else:
        print('Something went wrong')
        exit()            
main()    