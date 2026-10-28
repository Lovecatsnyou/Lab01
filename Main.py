import random
import tkinter as tk

W, H, COUNT = 800, 500, 150
root = tk.Tk()
cv = tk.Canvas(root, width=W, height=H, bg="#E8EAF6")
cv.pack()

drops = []
for _ in range(COUNT):
    z = random.uniform(0.2, 1.0)
    x, y = random.randint(0, W), random.randint(0, H)
    length, speed = int(z * 20), int(z * 15) + 3
    line_id = cv.create_line(x, y, x, y + length, fill="#6A1B9A", width=int(z * 2))
    drops.append([line_id, x, y, length, speed])


def update():
    for d in drops:
        d[2] += d[4]
        if d[2] > H:
            d[1], d[2] = random.randint(0, W), -d[3]
        cv.coords(d[0], d[1], d[2], d[1], d[2] + d[3])
    root.after(20, update)


update()
root.mainloop()⏎
