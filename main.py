import threading
import multiprocessing
import tkinter
from tkinter import ttk
from tkinter import messagebox
import serial.tools.list_ports
from random import randint
from time import sleep
# import serial

class Application(tkinter.Frame):
        
	port = 'COM1'
	data = process = None
       
	def __init__(self, master=None):
            
		super().__init__(master)
		self.master = master
		self.pack()
		self.app()

	def white_box(self):

		self.wb = tkinter.Label(self, text="")
		self.wb.pack()

	def button_box(self, text, font, size, cmd, color=None):

		if color is not None:
			self.btn = tkinter.Button(
				self,
				text=text,
				font=(font, size),
				command=cmd,
				fg=color
			)
		else:
			self.btn = tkinter.Button(
				self,
				text=text,
				font=(font, size),
				command=cmd
			)
		self.btn.pack()

	def text_box(self, text, font, size, color=None):

		if color is not None:
			self.text = tkinter.Label(
				self,
				text=text,
				font=(font, size),
				fg=color
			)
		else:
			self.text = tkinter.Label(
				self,
				text=text,
				font=(font, size)
			)
		self.text.pack()

	def app(self):

		try:
			if self.port is None:
				print("ERROR! Debe especificar un puerto")

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
			self.white_box()
            # Texto para cuando no se detecta ningún puerto
			self.text_box("No se ha detectado el puerto: " + self.port, "sans-serif", "18")
			self.white_box()
		else:
			self.white_box()
            # Texto para cuando está recibiendo datos
			self.text_box("Recibiendo datos por el puerto: " + self.port, "sans-serif", "18", "green")
            # Boton para actualizar los datos
            # self.button_box("Recibir datos", "sans-serif", "14", self.refresh_data)
			self.process = threading.Thread(target=self.refresh_data, daemon=True)
			# self.process = multiprocessing.Process(target=self.refresh_data, daemon=True)
			self.process.start()
			self.white_box()
			# Barra de progreso
			self.bar = ttk.Progressbar(self, orient="horizontal", length=100, mode="determinate")
			self.bar.pack()

			self.calc1 = tkinter.Label(
				self,
				text="Calculando..",
				font=("sans-serif", "12")
			)
			self.calc1.pack()
			self.white_box()

        # Boton para listar todos los puertos
		self.button_box("Ver puertos disponibles", "sans-serif", "14", self.list_ports)
		self.white_box()

		# Boton para cerrar la ventana
		self.button_box("Salir", "sans-serif", "14", self.exit_app, "red")
		self.white_box()

	def refresh_data(self):

		while True:
			# print(self.data.readline().decode('ascii'))
			sleep(3)
			num = randint(0,100)
			self.bar['value'] = num
			self.calc1.configure(text=("{} %").format(num))

	def exit_app(self):

		self.master.destroy()

	def list_ports(self):

		ports = []
		for port in serial.tools.list_ports.comports():
			ports.append(port)
		messagebox.showinfo('Lista de puertos disponibles', ports)


ROOT = tkinter.Tk()

ROOT.title("KartingControl")
ROOT.geometry("600x250")
ROOT.iconbitmap('gasolinera.ico')

APP = Application(master=ROOT)
APP.mainloop()
