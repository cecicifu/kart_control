# TODO: Posibilidad de cambiar Threading por multiprocessing
# TODO: Sistema de ventanas (TABS), una que muestre el listado de puertos COM disponibles

# import multiprocessing
from random import randint
from time import sleep
import threading
import serial.tools.list_ports
import tkinter as tk
from tkinter import ttk

import widget

if __name__ == "__main__":
    port = "COM1"
    data = process = None

    def exit_app():
        APP.destroy()

    def refresh_data():
        while True:
            # print(data.readline().decode('ascii'))
            sleep(3)
            num = randint(0, 100)
            bar["value"] = num
            calc_text.configure(text=("{} %").format(num))

    def list_ports():
        ports = []
        for port in serial.tools.list_ports.comports():
            ports.append(port)

    APP = tk.Tk()
    APP.title("KartingControl")
    APP.geometry("600x150")
    APP.iconbitmap("karting_icon.ico")

    try:
        if port is None:
            print("ERROR! Debe especificar un puerto.")

        serial.Serial(
            port=port,
            baudrate=9600,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=1,
            xonxoff=False,
            rtscts=False,
            dsrdtr=False,
            writeTimeout=2
        )
    except serial.SerialException:
        widget.text_box("No se ha detectado el puerto: " +
                        port, "sans-serif", "18")

    else:
        widget.text_box("Recibiendo datos por el puerto: " +
                        port, "sans-serif", "18", "green")
        # button_box("Recibir datos", "sans-serif", "14", refresh_data)
        process = threading.Thread(
            target=refresh_data, daemon=True)
        process.start()

        bar = ttk.Progressbar(orient="horizontal",
                              length=100, mode="determinate")
        bar.pack()

        calc_text = tk.Label(
            text="Calculando..", font=("sans-serif", "12"))
        calc_text.pack()

    # widget.button_box("Ver puertos disponibles", "sans-serif", "14", list_ports)
    widget.button_box("Salir", "sans-serif", "14", exit_app, "red")

    APP.mainloop()
