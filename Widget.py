import tkinter

class Widget():
    def white_box(self):
        wb = tkinter.Label(self, text="")
        wb.pack()

    def button_box(self, text, font, size, cmd, color=None):
        if color is not None:
            btn = tkinter.Button(
                self,
                text=text,
                font=(font, size),
                command=cmd,
                fg=color
            )
        else:
            btn = tkinter.Button(
                self,
                text=text,
                font=(font, size),
                command=cmd
            )
        btn.pack()

    def text_box(self, text, font, size, color=None):
        if color is not None:
            text = tkinter.Label(
                self,
                text=text,
                font=(font, size),
                fg=color
            )
        else:
            text = tkinter.Label(
                self,
                text=text,
                font=(font, size)
            )
        text.pack()
