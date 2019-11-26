# TODO: Llamar a subclase Tab1 desde clase padre
# TODO: Posibilidad de cambiar Threading por multiprocessing

#import multiprocessing
from random import randint
from time import sleep
import threading
import serial.tools.list_ports
import tkinter
from tkinter import ttk

import widget


class Application(tkinter.Frame):
    port = "COM1"
    data = process = None

    def __init__(self, title, size, icon):
        self.root = tkinter.Tk()

        super().__init__(self.root)

        self.root.title(title)
        self.root.geometry(size)
        self.root.iconbitmap(icon)
        self.pack()

        self.app()

    def app(self):
        try:
            if self.port is None:
                print("ERROR! Debe especificar un puerto.")

            self.data = serial.Serial(
                port=self.port,
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
                            self.port, "sans-serif", "18")

        else:
            widget.text_box("Recibiendo datos por el puerto: " +
                            self.port, "sans-serif", "18", "green")
            # self.button_box("Recibir datos", "sans-serif", "14", self.refresh_data)
            self.process = threading.Thread(
                target=self.refresh_data, daemon=True)
            self.process.start()

            self.bar = ttk.Progressbar(
                self, orient="horizontal", length=100, mode="determinate")
            self.bar.pack()

            self.calc1 = tkinter.Label(
                self,
                text="Calculando..",
                font=("sans-serif", "12")
            )
            self.calc1.pack()

        # widget.button_box("Ver puertos disponibles",
        #                  "sans-serif", "14", self.list_ports)
        widget.button_box("Salir", "sans-serif", "14", self.exit_app, "red")

    def exit_app(self):
        self.root.destroy()

    def refresh_data(self):
        while True:
            # print(self.data.readline().decode('ascii'))
            sleep(3)
            num = randint(0, 100)
            self.bar["value"] = num
            self.calc1.configure(text=("{} %").format(num))

    def list_ports(self):
        ports = []
        for port in serial.tools.list_ports.comports():
            ports.append(port)
