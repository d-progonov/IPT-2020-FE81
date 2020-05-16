from tkinter import *

from tkinter import messagebox as mb


class TShape:
    def __init__(self, canvas, id, on_click):
        self._canvas = canvas
        self._id = id
        self._canvas.tag_bind(self._id, '<ButtonPress-1>', on_click)


class Pixel(TShape):
    def __init__(self, canvas, x, y, on_click, color='black'):
        super().__init__(canvas, canvas.create_rectangle(x, y, x + 10, y + 10, fill=color, outline=""), on_click)

    def set_color(self, color):
        self._canvas.itemconfig(self._id, fill=color)

    def get_color(self):
        return self._canvas.itemcget(self._id, 'fill')


class Ellipse(Pixel):
    def __init__(self, canvas, x0, y0, x1, y1, on_click, color='black'):
        TShape.__init__(self, canvas, canvas.create_oval(x0, y0, x1, y1, fill=color, outline=""), on_click)

    def rotate(self):
        (x0, y0, x1, y1) = self._canvas.coords(self._id)
        a = (y1 - y0) / 2
        b = (x1 - x0) / 2
        self._canvas.coords(self._id, x0 + b - a, y0 - b + a, x1 - b + a, y1 + b - a)


class Circle(Ellipse):
    def __init__(self, canvas, x, y, radius, on_click, color='black'):
        r = radius
        TShape.__init__(self, canvas,
                        canvas.create_oval(x - r, y - r, x + r, y + r, fill=color, outline=""),
                        on_click)

    def set_radius(self, r):
        (x0, y0, x1, y1) = self._canvas.coords(self._id)
        x = 0.5 * (x1 - x0) + x0
        y = 0.5 * (y1 - y0) + y0
        self._canvas.coords(self._id, x - r, y - r, x + r, y + r)

    def get_radius(self):
        (x0, y0, x1, y1) = self._canvas.coords(self._id)
        return (x1 - x0) / 2

    def move(self, direction, distance):
        (x0, y0, x1, y1) = self._canvas.coords(self._id)
        if direction == 'top':
            y0 -= distance
            y1 -= distance
        elif direction == 'right':
            x0 += distance
            x1 += distance
        elif direction == 'left':
            x0 -= distance
            x1 -= distance
        elif direction == 'bot':
            y0 += distance
            y1 += distance
        self._canvas.coords(self._id, x0, y0, x1, y1)


class Sector(Ellipse):
    def __init__(self, canvas, x, y, radius, angle, on_click, color='black'):
        r = radius
        TShape.__init__(self, canvas,
                        canvas.create_arc(x - r, y - r, x + r, y + r, start=0, extent=angle, fill=color, outline=""),
                        on_click)

    def set_angle(self, angle):
        self._canvas.itemconfig(self._id, extent=angle)

    def get_angle(self):
        return self._canvas.itemcget(self._id, 'extent')


class App:
    def __init__(self):
        self.__root = Tk()

        self.__shapes = []
        self.__canvas = Canvas(self.__root, width=800, height=300)
        self.__root.resizable(False, False)
        self.__root.geometry("800x500")
        self.__canvas.grid(row=0)
        self.__menu_frame = LabelFrame(self.__root, text="Menu")
        self.__factory = self.creation_menu()
        self.__factory.grid(row=1, column=0, sticky=N + S + W)
        self.__menu_frame.grid(row=1, )

    def creation_menu(self):
        menu = LabelFrame(self.__root, text="Create")

        x = self.__add_property_change_menu('x', menu,
                                            lambda _: 100,
                                            lambda _: None, None, 0, False)
        y = self.__add_property_change_menu('y', menu,
                                            lambda _: 100,
                                            lambda _: None, None, 1, False)
        color = self.__add_property_change_menu('color', menu,
                                                lambda _: 'black',
                                                lambda _: None, None, 2, False)

        def button(name, action, row):
            b = Button(menu, text=name)

            def on_click():
                try:
                    action(int(x.get()), int(y.get()), color.get())
                except ValueError:
                    mb.showerror("", 'Bad input')
                except TclError:
                    mb.showerror("", 'Bad color')
            b.config(command=lambda: on_click())
            b.grid(row=row, columnspan=100, sticky=N + S + E + W)

        button('Pixel', lambda x, y, c: self.add_pixel(x, y, c), 3)

        button('Ellipse',
               lambda x, y, c: self.add_ellipse(x, y, x + 20, y + 40, c),
               4)
        button('Circle', lambda x, y, c: self.add_circle(x, y, 40, c), 5)
        button('Sector', lambda x, y, c: self.add_sector(x, y, 40, -70, c), 6)
        return menu

    def wait(self):
        self.__root.mainloop()

    def __clear_menu(self):
        # for w in self.__menu:
        #    w.pack_forget()
        for widget in self.__menu_frame.winfo_children():
            widget.destroy()

    def __add_property_change_menu(self, name, frame, init, action, shape, line, clear_menu):
        if clear_menu:
            self.__clear_menu()
        label_text = StringVar()
        label_text.set(name)
        label = Label(frame, textvariable=label_text, height=1)
        text = StringVar()
        text.set(init(shape))
        entry = Entry(frame, textvariable=text)
        entry.bind('<Return>', lambda _: action(entry))
        label.grid(row=line, column=0, sticky=N + S + E + W)
        entry.grid(row=line, column=1, sticky=N + S + E + W)
        return entry

    def __add_color_change_menu(self, shape, line, clear_menu=False):
        def change_color(entry):
            try:
                shape.set_color(entry.get())
            except TclError:
                mb.showerror("", 'Bad color')

        self.__add_property_change_menu('Color: ',
                                        self.__menu_frame,
                                        lambda shape_: shape_.get_color(),
                                        change_color,
                                        shape,
                                        line,
                                        clear_menu)

    def __add_rotate_menu(self, shape, line, clear_menu=False):
        if clear_menu:
            self.__clear_menu()
        button = Button(self.__menu_frame, text="Rotate")
        button.config(command=lambda: shape.rotate())

        button.grid(row=line, columnspan=100, sticky=N + S + E + W)

    def __add_radius_change_menu(self, shape, line, clear_menu=False):
        self.__add_property_change_menu('Radius: ',
                                        self.__menu_frame,
                                        lambda entry: entry.get_radius(),
                                        lambda entry: shape.set_radius(float(entry.get())),
                                        shape,
                                        line,
                                        clear_menu)

    def __add_move_menu(self, shape, line, clear_menu=False):
        distance = 20
        if clear_menu:
            self.__clear_menu()
        frame = Frame(self.__menu_frame)
        frame.grid(row=line, columnspan=100)
        top = Button(frame, text="🡅", command=lambda: shape.move('top', distance), width=23)
        top.grid(row=0, column=0, columnspan=100, sticky=N + S + E + W)
        left = Button(frame, text="🡄", command=lambda: shape.move('left', distance), width=11)
        left.grid(row=1, column=0, sticky=N + S + E + W)
        right = Button(frame, text="🡆", command=lambda: shape.move('right', distance), width=11)
        right.grid(row=1, column=1, sticky=N + S + E + W)
        bottom = Button(frame, text="🡇", command=lambda: shape.move('bot', distance), width=23)
        bottom.grid(row=2, column=0, columnspan=100, sticky=N + S + E + W)

    def __add_angle_change_menu(self, shape, line, clear_menu=False):
        self.__add_property_change_menu('Angle: ',
                                        self.__menu_frame,
                                        lambda shape: shape.get_angle(),
                                        lambda entry: shape.set_angle(float(entry.get())),
                                        shape,
                                        line,
                                        clear_menu)

    def add_pixel(self, x, y, color='black'):
        pixel = Pixel(self.__canvas, x, y, lambda _: self.__add_color_change_menu(pixel, 0, True), color)
        self.__shapes.append(pixel)

    def add_ellipse(self, x0, y0, x1, y1, color='black'):
        def menu(shape):
            self.__add_rotate_menu(shape, 0, True)
            self.__add_color_change_menu(shape, 1)

        ellipse = Ellipse(self.__canvas, x0, y0, x1, y1, lambda _: menu(ellipse), color)
        self.__shapes.append(ellipse)

    def add_circle(self, x, y, radius, color='black'):
        def menu(shape):
            self.__add_color_change_menu(shape, 0, True)
            self.__add_radius_change_menu(shape, 1)
            self.__add_move_menu(shape, 2)

        circle = Circle(self.__canvas, x, y, radius, lambda _: menu(circle), color)
        self.__shapes.append(circle)

    def add_sector(self, x, y, radius, angle, color='black'):
        def menu(shape):
            self.__add_color_change_menu(shape, 0, True)
            # self.__add_radius_change_menu(shape, 1)
            self.__add_angle_change_menu(shape, 2)

        sector = Sector(self.__canvas, x, y, radius, angle, lambda _: menu(sector), color)
        self.__shapes.append(sector)


def main():
    app = App()

    app.wait()


if __name__ == '__main__':
    main()


