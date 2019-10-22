import re
import time
import tkinter as tk

import pyautogui


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MouseArt")
        self.create_canvas()
        self.exit_button = tk.Button(self, text="Quit", command=self.quit)
        self.exit_button.pack()
        self.canvas.old_coords = None
        self.canvas.pack()
        self.quit_flag = 1
        self.bind_mouse()

    def create_canvas(self):
        self.size = str(pyautogui.size())
        self.width, self.height = re.findall(r"\d+", self.size)
        self.canvas = tk.Canvas(self, width=self.width, height=self.height)

    def draw(self, x, y):
        if self.canvas.old_coords:
            x1, y1 = self.canvas.old_coords
            self.canvas.create_line(x, y, x1, y1)
        self.canvas.old_coords = x, y
        self.canvas.update()

    def bind_mouse(self):
        old_x = old_y = 0
        while self.quit_flag:
            x, y = pyautogui.position()
            y -= 20
            if old_x != x and old_y != y:
                self.draw(x, y)
                old_x, old_y = x, y
                time.sleep(0.01)

    def quit(self):
        self.quit_flag = 0
        self.destroy()


if __name__ == "__main__":
    root = Root()
    root.mainloop()
