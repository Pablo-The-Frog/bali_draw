import tkinter as tk
from tkinter import filedialog
from tkinter.colorchooser import askcolor
from PIL import Image, ImageDraw

class BaliDraw:
    def __init__(self, root):
        self.root = root
        self.root.title("Bali'n Draw Pro Deluxe Turbo")
        self.color = 'black'
        self.brush_size = 5
        self.image = Image.new("RGB", (800, 600), "white")
        self.draw_ctx = ImageDraw.Draw(self.image)

        self.canvas = tk.Canvas(root, bg='white', width=800, height=600)
        self.canvas.pack()

        self.last_x, self.last_y = None, None
        self.canvas.bind('<B1-Motion>', self.draw)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

        control = tk.Frame(root)
        control.pack()

        tk.Button(control, text='Clear', command=self.clear).pack(side='left')
        tk.Button(control, text='Color', command=self.choose_color).pack(side='left')
        tk.Button(control, text='Save', command=self.save).pack(side='left')

        size_label = tk.Label(control, text="Taille:")
        size_label.pack(side='left')
        self.size_slider = tk.Scale(control, from_=1, to=20, orient='horizontal', command=self.set_brush_size)
        self.size_slider.set(self.brush_size)
        self.size_slider.pack(side='left')

    def draw(self, event):
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                                    fill=self.color, width=self.brush_size, capstyle=tk.ROUND, smooth=True)
            self.draw_ctx.line([self.last_x, self.last_y, event.x, event.y],
                               fill=self.color, width=self.brush_size)
        self.last_x, self.last_y = event.x, event.y

    def reset(self, _):
        self.last_x, self.last_y = None, None

    def clear(self):
        self.canvas.delete('all')
        self.image = Image.new("RGB", (800, 600), "white")
        self.draw_ctx = ImageDraw.Draw(self.image)

    def choose_color(self):
        color = askcolor(color=self.color)[1]
        if color:
            self.color = color

    def set_brush_size(self, val):
        self.brush_size = int(val)

    def save(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".png",
                                                filetypes=[("PNG files", "*.png")])
        if filepath:
            self.image.save(filepath)

def main():
    root = tk.Tk()
    app = BaliDraw(root)
    root.mainloop()

if __name__ == '__main__':
    main()
