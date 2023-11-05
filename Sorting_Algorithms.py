import tkinter as tk
import time

# Sorting Algorithm Implementations
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Global variables
algorithms = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort
}

# Benchmarking function
def benchmark_sorting(sorting_func, arr):
    start_time = time.time()
    sorting_func(arr)
    end_time = time.time()
    return end_time - start_time

# Global variables
algorithms = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort
}

# Function to perform sorting and measure execution time
def perform_sorting():
    global algorithms
    input_data = [int(x) for x in input_entry.get().split(",")]
    execution_times = {}
    
    for algorithm_name, sorting_algorithm in algorithms.items():
        arr_copy = input_data.copy()
        start_time = time.time()
        sorting_algorithm(arr_copy)
        end_time = time.time()
        execution_times[algorithm_name] = (arr_copy, end_time - start_time)
        
    sorted_algorithms = sorted(execution_times, key=lambda x: execution_times[x][1])
    fastest_algorithm = sorted_algorithms[0]
    output_label.config(text=f"Sorted List: {execution_times[fastest_algorithm][0]}\nFastest Algorithm: {fastest_algorithm} (Execution Time: {execution_times[fastest_algorithm][1]:.8f} seconds)")
    
# Main Function
def main():
    global input_entry, output_label  # Accessing the global variables
    window = tk.Tk()
    window.title("Sorting Algorithm Benchmarking Tool")
    
    input_label = tk.Label(window, text="Enter Numbers to Sort (separated by commas):")
    input_label.pack()
    
    input_entry = tk.Entry(window)
    input_entry.pack()
    
    sort_button = tk.Button(window, text="Sort", command=perform_sorting)
    sort_button.pack()
    
    output_label = tk.Label(window, text="")
    output_label.pack()
    
    window.mainloop()
    
if __name__ == "__main__":
    main()