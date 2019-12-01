# TODO: Convertir a clase e invocarla en Application.py

import tkinter


def space_box():
    sb = tkinter.Label(text="")
    sb.pack()


def button_box(text, font, size, cmd, color=None):
    if color is not None:
        btn = tkinter.Button(
            text=text,
            font=(font, size),
            command=cmd,
            fg=color
        )
    else:
        btn = tkinter.Button(
            text=text,
            font=(font, size),
            command=cmd
        )
    btn.pack()


def text_box(text, font, size, color=None):
    if color is not None:
        text = tkinter.Label(
            text=text,
            font=(font, size),
            fg=color
        )
    else:
        text = tkinter.Label(
            text=text,
            font=(font, size)
        )
    text.pack()
