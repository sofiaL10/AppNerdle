import smtplib
import tkinter as tk
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from Nerdle.modelo.estadisticas import Estadisticas


class EstadisticasApp:
    def __init__(self, root1):
        self.correo_entry = None
        self.root = root1
        self.root.title("Estadísticas")
        self.estadisticas = Estadisticas()
        self.create_widgets()
        self.create_plot()

    def create_widgets(self):
        label = tk.Label(self.root, text="Estadísticas del Juego")
        label.pack(pady=10)
        correo_label = tk.Label(self.root, text="¿Desea recibir sus estadísticas de juego por correo electrónico?" \
                                                "si es asi, ingrese su email:")
        correo_label.pack()
        self.correo_entry = tk.Entry(self.root)
        self.correo_entry.pack()
        enviar_button = tk.Button(self.root, text="Enviar Estadísticas", command=self.enviar_estadisticas)
        enviar_button.pack()

    def create_plot(self):
        self.fig = self.estadisticas.crear_grafica()
        canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()

    def enviar_estadisticas(self):
        correo = self.correo_entry.get()
        if not correo:
            messagebox.showerror("Error", "Por favor, ingrese su correo electrónico.")
            return

        # para configurar el smtp
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_user = 'nerdlejuego@gmail.com'
        smtp_password = 'ydkk obdg slcn eyuo'

        # Mensaje de correo
        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = correo
        msg['Subject'] = "Estadísticas de Juego"
        estadisticas_text = "Aquí van tus estadísticas: ¡éxito!"
        msg.attach(MIMEText(estadisticas_text, 'plain', 'utf-8'))  # Usa UTF-8 para admitir caracteres no ASCII

        # Guardar la gráfica como imagen
        self.fig.savefig('grafica.png', format='png')
        with open('../../assets/grafica.png', 'rb') as img_file:
            img = MIMEImage(img_file.read())
            img.add_header('Content-Disposition', 'attachment', filename="../../assets/grafica.png")
            msg.attach(img)

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, correo, msg.as_string())
            server.quit()
            messagebox.showinfo("Éxito", "Estadísticas enviadas exitosamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron enviar las estadísticas. Error: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = EstadisticasApp(root)
    root.mainloop()
