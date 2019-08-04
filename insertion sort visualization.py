import tkinter as tk
import time
from random import shuffle

root = tk.Tk()
root.wm_title("Insertion Sort Visualization")
root.wm_geometry("1000x500")

canvas = tk.Canvas(root, height=500, width=1000)
canvas.pack()

def insertion(x, obj):
    for j in range(1, len(x)):
        key = x[j]
        i = j - 1
        while i >= 0 and x[i] > key:
            start = time.time()
            canvas.itemconfig(obj[i+1], fill='red') #
            x[i+1], x[i] = x[i], x[i+1]         
            swap_rects(obj, i) #       
            i = i - 1 
            time.sleep(max(1./200 - (time.time() - start), 0))
            canvas.update() #
        canvas.itemconfig(obj[i+1], fill='black') #           
        x[i+1] = key
    turn_all_green(obj)

def swap_rects(l, i):
    x1, _, _, _ = canvas.coords(l[i])
    x2, _, _, _ = canvas.coords(l[i+1])
    canvas.move(l[i+1], x1 - x2, 0)
    canvas.move(l[i], x2 - x1, 0)
    l[i], l[i+1] = l[i+1], l[i]

def turn_all_green(obj):
    for i in obj:
        canvas.update()
        start = time.time()
        canvas.itemconfig(i, fill='green')
        time.sleep(max(1./100 - (time.time() - start), 0))

def call():
    canvas.delete('all')

    nums = list(range(1,101))
    shuffle(nums)

    rect_list = []

    for i, num in enumerate(nums):
        rect_list.append(canvas.create_rectangle(i*10, 500, i*10 + 10, 500-num*5, fill='black')) # bars fit to bottom
        # rect_list.append(canvas.create_rectangle(i*10, 0, i*10 + 10, num*5, fill='black'))     # bars fit to top

    insertion(nums, rect_list)

root.bind("<Key>", lambda e: call())

root.mainloop()
