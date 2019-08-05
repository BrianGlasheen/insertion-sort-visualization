import tkinter as tk
import time
from random import shuffle

width = 1000
delay = 1./500

root = tk.Tk()
root.wm_title("Insertion Sort Visualization")
root.wm_geometry(f"{width}x{width//2}")
root.wm_resizable(width=False, height=False)

canvas = tk.Canvas(root, height=width//2, width=width, background='black')
canvas.pack()
canvas.create_text(width//2, width//4, fill='white', font=("Arial", 20, "bold"), text="Press any key")

list_acceses = 0
comparisons = 0

def insertion(x, obj, list_acceses, comparisons, info, delay):
    for j in range(1, len(x)):
        key = x[j]
        i = j - 1
        while i >= 0 and x[i] > key:
            start = time.time()
            canvas.itemconfig(obj[i+1], fill='red') #
            x[i+1], x[i] = x[i], x[i+1]
            list_acceses += 3
            comparisons += 1
            canvas.itemconfig(info, text=f"  {comparisons} comparisons, {list_acceses} list accesses, {delay} second delay")
            swap_rects(obj, i) #       
            i = i - 1 
            time.sleep(max(delay - (time.time() - start), 0))
            canvas.update() #
        canvas.itemconfig(obj[i+1], fill='white') #           
        x[i+1] = key
    print(list_acceses, comparisons)
    turn_all_green(obj, delay)

def swap_rects(l, i):
    x1, _, _, _ = canvas.coords(l[i])
    x2, _, _, _ = canvas.coords(l[i+1])
    canvas.move(l[i+1], x1 - x2, 0)
    canvas.move(l[i], x2 - x1, 0)
    l[i], l[i+1] = l[i+1], l[i]

def turn_all_green(obj, delay):
    for i in obj:
        canvas.update()
        start = time.time()
        canvas.itemconfig(i, fill='green')
        time.sleep(max(delay/2 - (time.time() - start), 0))

def call(width, list_acceses, comparisons, delay):
    canvas.delete('all')
    
    info = canvas.create_text(0,5, anchor=tk.NW, font=("Arial", 10, "bold"), fill='white', text=f"  {comparisons} comparisons, {list_acceses} list accesses, .5 ms delay")

    elements = 100

    x = width//elements
    y = x/2

    nums = list(range(1,elements+1))
    shuffle(nums)

    rect_list = []

    for i, num in enumerate(nums):
        rect_list.append(canvas.create_rectangle(i*x, width//2, i*x + x, (width//2)-num*y, fill='white'))

    insertion(nums, rect_list, list_acceses, comparisons, info, delay)

root.bind("<Key>", lambda e: call(width, list_acceses, comparisons, delay))

root.mainloop()
