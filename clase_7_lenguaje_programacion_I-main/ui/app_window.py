from services.task_service import TaskService
import tkinter as tk
from tkinter import ttk, messagebox

class AppWindow(tk.Tk):
    def __init__(self, service: TaskService) -> None:
        super().__init__()
        # Inyección del servicio
        self.service = service

        # Config de mi app
        self.title("Tkinter con POO + Capas")
        self.geometry("600x500")

        # Creación de widgets
        self.create_widget()

    def create_widget(self):
        """Inicializa todos los widgets"""

        self.render_entries()

        self.insert_btn = tk.Button(
            self, text="Crear tarea", command=self.insert_task)
        self.insert_btn.pack()

        self.create_data_table()
        self.render_data_table()

    def render_entries(self):
        """Renderiza los campos de entradas y las etiquetas de texto"""
        label_title = tk.Label(self, text="Ingresa el título")
        label_title.pack()

        self.entry_title = tk.Entry(self)
        self.entry_title.pack()

        label_description = tk.Label(self, text="Ingresa la descripción")
        label_description.pack()

        self.entry_description = tk.Entry(self)
        self.entry_description.pack()

    def clear_entries(self):
        """Limpia todos los campos de entrada"""
        # El método .delete() elimina desde el principio hasta el fin
        self.entry_title.delete(0, "end")
        self.entry_description.delete(0, "end")

        self.entry_title.focus()

    def insert_task(self):
        """Crea una nueva tarea"""
        title = self.entry_title.get()
        description = self.entry_description.get()

        if not title or not description:
            messagebox.showinfo(title="Información",
                                message="Todos los campos son obligatorios!")
            return

        # Llama al servicio para crear una nueva tarea
        self.service.create_one(title, description)

        # Luego de crear una tarea actualiza la tabla
        self.render_data_table()

        # Limpia los campos de entrada y establece el focus en el primer campo de entrada
        self.clear_entries()

    def create_data_table(self):
        """Crea y configura la tabla"""
        self.tree = ttk.Treeview(self, columns=("uuid",
                                                "title", "description"), show="headings")

        self.tree.column("uuid", anchor="center", width=150)
        self.tree.column("title", anchor="center", width=150)
        self.tree.column("description", anchor="center", width=250)

        self.tree.heading("uuid", text="ID")
        self.tree.heading("title", text="Título")
        self.tree.heading("description", text="Descripción")

        self.tree.pack()

    def render_data_table(self):
        """Renderiza y limpia la tabla"""
        tasks = self.service.find_all()

        # Limpiamos nuestra tabla antes de insertar los registros
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Renderizo los registros en mi tabla
        for task in tasks:
            task_uuid = str(task.uuid)

            self.tree.insert("", "end", values=(
                task_uuid, task.title, task.description))