import tkinter as tk
import time
from random import shuffle

width = 1500
delay = 1./2000

root = tk.Tk()
root.wm_title("Insertion Sort Visualization")
root.wm_geometry(f"{width}x{width//2}")
root.wm_resizable(width=False, height=False)

canvas = tk.Canvas(root, height=width//2, width=width, background='black')
canvas.pack()
canvas.create_text(width//2, width//4, fill='white', font=("Arial", 10, "bold"), text="S - slection sort\nI - insertion sort\nB - bubble sort")

def insertion(x, obj, list_acceses, comparisons, info, delay):
    for j in range(1, len(x)):
        key = x[j]
        i = j - 1
        while i >= 0 and x[i] > key:
            start = time.time()
            canvas.itemconfig(obj[i+1], fill='red') 
            x[i+1], x[i] = x[i], x[i+1]
            list_acceses += 3
            comparisons += 1
            canvas.itemconfig(info, text=f"  {comparisons} comparisons, {list_acceses} list accesses, {delay} second delay")
            swap_rects(obj, i, i+1)        
            i = i - 1 
            time.sleep(max(delay - (time.time() - start), 0))
            canvas.update() 
        canvas.itemconfig(obj[i+1], fill='white')            
        x[i+1] = key
    turn_all_green(obj, delay) 

def selection(x, obj, list_acceses, comparisons, info, delay):
    for i in range(len(x)): 
        min_idx = i 
        for j in range(i+1, len(x)):
            start = time.time()
            canvas.itemconfig(obj[j], fill='red') 
            canvas.update()
            if x[min_idx] > x[j]: 
                min_idx = j
                canvas.itemconfig(obj[j], fill='white') 
                canvas.update()
            else:
                canvas.itemconfig(obj[j], fill='white') 
                canvas.update()
            list_acceses += 2
            comparisons += 1
        canvas.itemconfig(info, text=f"  {comparisons} comparisons, {list_acceses} list accesses, {delay} second delay")

        time.sleep(max(delay - (time.time() - start), 0))
        x[i], x[min_idx] = x[min_idx], x[i]
        swap_rects(obj, i, min_idx) 
        canvas.update()
    turn_all_green(obj, delay) 

def bubble(x, obj, list_acceses, comparisons, info, delay):
    for i in range(len(x)):
        start = time.time()
        for j in range(0, len(x)-i-1):
            canvas.itemconfig(obj[j], fill='red') 
            canvas.update()
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
                list_acceses += 4
                swap_rects(obj, j, j+1)  
                canvas.itemconfig(obj[j+1], fill='white') 
            else:
                list_acceses += 2 
                canvas.itemconfig(obj[j], fill='white') 
            comparisons += 1  
            canvas.update() 


        canvas.itemconfig(info, text=f"  {comparisons} comparisons, {list_acceses} list accesses, {delay} second delay")
        canvas.itemconfig(obj[j], fill='white') 
        canvas.update() 

        time.sleep(max(delay - (time.time() - start), 0))
    turn_all_green(obj, delay) 

def swap_rects(l, i, j):
    x1, _, _, _ = canvas.coords(l[i])
    x2, _, _, _ = canvas.coords(l[j])
    canvas.move(l[j], x1 - x2, 0)
    canvas.move(l[i], x2 - x1, 0)
    l[i], l[j] = l[j], l[i]

def turn_all_green(obj, delay):
    for i in obj:
        canvas.update()
        start = time.time()
        canvas.itemconfig(i, fill='green')
        time.sleep(max(delay/2 - (time.time() - start), 0))

def start_up(width):
    canvas.delete('all')
    
    list_acceses = 0
    comparisons = 0
    
    info = canvas.create_text(0,5, anchor=tk.NW, font=("Arial", 10, "bold"), fill='white', text=f"  {comparisons} comparisons, {list_acceses} list accesses, .5 ms delay")

    elements = 250

    x = width//elements
    y = x/2

    nums = list(range(1,elements+1))
    shuffle(nums)

    rect_list = []

    for i, num in enumerate(nums):
        rect_list.append(canvas.create_rectangle(i*x, width//2, i*x + x, (width//2)-num*y, fill='white', outline='black'))
    
    return nums, rect_list, list_acceses, comparisons, info

def insertion_keypress(width, delay):
    nums, rect_list, list_acceses, comparisons, info = start_up(width)
    insertion(nums, rect_list, list_acceses, comparisons, info, delay)

def selection_keypress(width, delay):
    nums, rect_list, list_acceses, comparisons, info = start_up(width)
    selection(nums, rect_list, list_acceses, comparisons, info, delay)

def bubble_keypress(width, delay):
    nums, rect_list, list_acceses, comparisons, info = start_up(width)
    bubble(nums, rect_list, list_acceses, comparisons, info, delay)
    
root.bind("<Key-i>", lambda e: insertion_keypress(width, delay))
root.bind("<Key-s>", lambda e: selection_keypress(width, delay))
root.bind("<Key-b>", lambda e: bubble_keypress(width, delay))

root.mainloop()
