#На плоскости задано множество точек. Найти треугольник, построенный на этих
#точках, в котором самый большой угол.
#Дать графическое изображение результатов.

#Программа сделана Ву Минь Куанг ИУ7-24Б

import tkinter as tk
import tkinter.messagebox as msg
from math import *
import numpy as np
import itertools as it

screen_width, screen_height = 600, 600
scale = 5

def trian_side1(a, b, c):
    ab_side = sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
    bc_side = sqrt((c[0]-b[0])**2+(c[1]-b[1])**2)
    ca_side = sqrt((a[0]-c[0])**2+(a[1]-c[1])**2)
    return ab_side, bc_side, ca_side

def is_trian(a, b, c):
    if (a + b) > c and (a + c) > b and (b + c) > a:
        return True
    else:
        return False

def delete_all(canv, dots):
    canv.delete("for_delete")
    dots.clear()



def processing(dots, canv):
    if len(dots) < 3:
        msg.showinfo("Incorrect input","Not enough dots")
        return;

    min_trial = 2
    list_trial=[]
    for i in range(len(dots)):
        for j in range(len(dots)):
            for k in range(len(dots)):
                ab, bc, ca =trian_side1(dots[i], dots[j], dots[k])
                if is_trian(ab, bc, ca):
                    cos_A = (ab**2+ca**2-bc**2)/(ab*ca*2)
                    cos_B = (bc**2+ab**2-ca**2)/(ab*bc*2)
                    cos_C = (bc**2+ca**2-ab**2)/(bc*ca*2)
                    min_coner = min(cos_A,cos_B,cos_C)
                    if min_coner < min_trial:
                        min_trial = min_coner
                        list_trial = [dots[i], dots[j], dots[k]]

    rez_draw_xy = list()
    for i in range(len(list_trial)):
        rez_draw_xy.append(list_trial[i][0]) 
        rez_draw_xy.append((list_trial[i][1]))
            
    canv.create_polygon(rez_draw_xy[0], rez_draw_xy[1], rez_draw_xy[2], rez_draw_xy[3], rez_draw_xy[4], rez_draw_xy[5],
                                tag = 'for_delete', fill='', outline='black')


def dot_handle_dialog(canv, dots, enter_window, entr):
    string = entr.get().strip()
    if len(string) == 0:
        msg.showerror("Incorrect input",
                      "Enter the coordinates in the correct format")
    else:
        try:
            new_dots = [float(i) for i in string.split(" ")]
            new_dots = [i+300 for i in new_dots]
            if len(new_dots) % 2:
                raise BaseException("Must be doubled")
        except:
            msg.showerror("Incorrect input",
                          "Enter the coordinates in the correct format")
        else:
            coords = list(zip(new_dots[0::2], new_dots[1::2]))
            dots.extend(coords)
            enter_window.destroy()
            for coord in coords:
                canv.create_oval(
                    coord[0] - 4,
                    coord[1] - 4,
                    coord[0] + 4,
                    coord[1] + 4,
                    fill="red",
                    outline="black",
                    tags=["dot", "for_delete"],
                )


def dot_handle(canv, dots, root):
    enter_window = tk.Toplevel(root)
    enter_window.geometry("520x150")

    app = tk.Frame(enter_window, bg="white")
    app.pack(padx=10, pady=10, fill=tk.BOTH)

    info_text = "Enter the coordinates of the points (use space as separation)"
    lbl = tk.Label(app, text=info_text, font="Arial 10", bg="white")
    lbl.pack(padx=10, pady=10, side=tk.TOP)

    entr = tk.Entry(app, width=30)
    entr.pack(padx=20, pady=10, side=tk.TOP)
    entr.insert(0, "")

    btn = tk.Button(app, text="Display dots", bg="gray", foreground="white",
                    command=lambda : dot_handle_dialog(canv, dots, enter_window, entr))
    btn.pack(padx=20, pady=10, side=tk.TOP)

    enter_window.mainloop()


def add_dot(event, canv, dots):
    x = event.x - 300
    y = event.y - 300
    canv.create_oval(
        event.x-4,
        event.y-4,
        event.x+4,
        event.y+4,
        fill="red",
        outline="black",
        tags=["dot", "for_delete"]
        )
    dots.append(tuple([x + 300, y + 300]))


def create_axis(canv):
    canv.create_line(
        screen_width // 2, 0,
        screen_width // 2, screen_height,
        width=2
    )
    canv.create_line(
        0, screen_width // 2,
        screen_width, screen_width // 2,
        width=2
    )
    canv.create_text(
        screen_width // 2 - 10, screen_height - 12,
        text="Y", font="Times 15"
    )
    canv.create_text(
        screen_width - 10, screen_height // 2 + 15,
        text="X", font="Times 15"
    )
    canv.create_text(
        screen_width // 2 - 10, screen_height // 2 - 12,
        text="0", font="Times 15"
    )
    canv.create_line(
        screen_width // 2 + 50, screen_height // 2 - 10,
        screen_width // 2 + 50, screen_height // 2 + 10,
        width=1
    )
    canv.create_text(
        screen_width // 2 + 50, screen_height // 2 - 20,
        text="50", font="Times 15"
    )
    canv.create_line(
        screen_width // 2 - 10, screen_height // 2 + 50,
        screen_width // 2 + 10, screen_height // 2 + 50,
        width=1
    )
    canv.create_text(
        screen_width // 2 - 25, screen_height // 2 + 50,
        text="50", font="Times 15"
    )


def info():
    msg.showinfo("Information", "Planimetric task\n"
                 "Developer: Ву Минь Куанг ИУ7-24Б\n")


def main_init(root):
    dots = []
    canv = tk.Canvas(root, width=screen_width,
        height=screen_height, bg="#ffffff")

    main_menu = tk.Menu(root)
    root.config(menu=main_menu)
    main_menu.add_command(label="Run",
        command=lambda : processing(dots, canv))  
    main_menu.add_command(label="Enter the coordinates",
        command=lambda : dot_handle(canv, dots, root))
    main_menu.add_command(label="Clear",
        command=lambda : delete_all(canv, dots))
    main_menu.add_command(label="Info", command=lambda : info())  

    canv.bind("<Button-1>", lambda event : add_dot(event, canv, dots))
    create_axis(canv)

    canv.pack(side=tk.BOTTOM)


if __name__ == "__main__":
    root = tk.Tk()
    app = tk.Frame(root)
    app.pack()
    root.title("Planimetric task")
    root.geometry((str(screen_width) + 'x' + str(screen_height)))
    root.resizable(False, False)

    main_init(root)

    root.mainloop()
