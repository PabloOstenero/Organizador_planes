import tkinter as tk
from tkinter import ttk, messagebox
import heapq

def crear_horario(tareas, horas_libres):
    tareas_ordenadas = [(-importancia, nombre, duracion) for nombre, importancia, duracion in tareas]
    heapq.heapify(tareas_ordenadas)
    
    horario = {dia: {hora: "" for hora in range(8, 20)} for dia in horas_libres}

    for dia, horas in horas_libres.items():
        horas_lista = sorted(horas)
        indice_hora = 0
        tiempo_restante = len(horas_lista)
        
        while tareas_ordenadas and indice_hora < len(horas_lista):
            importancia, nombre, duracion = heapq.heappop(tareas_ordenadas)
            
            horas_asignadas = 0
            while horas_asignadas < duracion and indice_hora < len(horas_lista):
                hora_actual = horas_lista[indice_hora]
                
                # Verificar si la hora ya está ocupada antes de asignar
                if horario[dia][hora_actual] == "":
                    horario[dia][hora_actual] = nombre
                    horas_asignadas += 1
                    tiempo_restante -= 1
                
                indice_hora += 1
                
            if horas_asignadas < duracion:
                heapq.heappush(tareas_ordenadas, (-importancia, nombre, duracion - horas_asignadas))

            if tiempo_restante <= 0:
                break

    return horario

class HorarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Horario")
        self.root.geometry("800x600")  # Aumentar el tamaño de la ventana
        self.tareas = []
        self.horas_libres = {dia: [] for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]}
        
        self.setup_ui()
    
    def setup_ui(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(pady=10, expand=True)
        
        frame_tareas = ttk.Frame(notebook, padding=10)
        frame_horas = ttk.Frame(notebook, padding=10)
        frame_resultado = ttk.Frame(notebook, padding=10)
        
        notebook.add(frame_tareas, text="Tareas")
        notebook.add(frame_horas, text="Horas Libres")
        notebook.add(frame_resultado, text="Horario Generado")
        
        self.setup_tareas(frame_tareas)
        self.setup_horas(frame_horas)
        self.setup_resultado(frame_resultado)
    
    def setup_tareas(self, frame):
        ttk.Label(frame, text="Tarea:").grid(row=0, column=0, padx=5, pady=5)
        self.tarea_name = ttk.Entry(frame, width=30)
        self.tarea_name.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame, text="Importancia:").grid(row=1, column=0, padx=5, pady=5)
        self.importancia = ttk.Entry(frame, width=10)
        self.importancia.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(frame, text="Duración:").grid(row=2, column=0, padx=5, pady=5)
        self.duracion = ttk.Entry(frame, width=10)
        self.duracion.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Button(frame, text="Añadir Tarea", command=self.add_tarea).grid(row=3, columnspan=2, pady=10)
        
        self.lista_tareas = tk.Listbox(frame, width=50, height=5)
        self.lista_tareas.grid(row=4, columnspan=2, pady=10)
    
    def setup_horas(self, frame):
        ttk.Label(frame, text="Día:").grid(row=0, column=0, padx=5, pady=5)
        self.dia_selector = ttk.Combobox(frame, values=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"], state="readonly")
        self.dia_selector.grid(row=0, column=1, padx=5, pady=5)
        self.dia_selector.set("Lunes")
        
        ttk.Label(frame, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
        self.hora_selector = ttk.Combobox(frame, values=[str(i) for i in range(8, 20)], state="readonly")
        self.hora_selector.grid(row=1, column=1, padx=5, pady=5)
        self.hora_selector.set("8")
        
        ttk.Button(frame, text="Añadir Hora", command=self.add_hora).grid(row=2, columnspan=2, pady=10)
    
    def setup_resultado(self, frame):
        ttk.Button(frame, text="Generar Horario", command=self.generar_horario).pack(pady=10)
        
        # Usar un widget Text con fuente monoespaciada para mejor alineación
        self.resultado_text = tk.Text(frame, width=90, height=20, font=("Courier", 10))
        self.resultado_text.pack()
    
    def add_tarea(self):
        nombre = self.tarea_name.get()
        try:
            importancia = int(self.importancia.get())
            duracion = int(self.duracion.get())
        except ValueError:
            messagebox.showerror("Error", "Importancia y duración deben ser números.")
            return
        
        if nombre and importancia > 0 and duracion > 0:
            self.tareas.append((nombre, importancia, duracion))
            self.lista_tareas.insert(tk.END, f"{nombre} (Importancia: {importancia}, Duración: {duracion} hrs)")
            self.tarea_name.delete(0, tk.END)
            self.importancia.delete(0, tk.END)
            self.duracion.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Todos los campos deben estar completos y ser válidos.")
    
    def add_hora(self):
        dia = self.dia_selector.get()
        hora = int(self.hora_selector.get())
        if hora not in self.horas_libres[dia]:
            self.horas_libres[dia].append(hora)
            messagebox.showinfo("Éxito", f"Hora {hora}:00 añadida al día {dia}.")
        else:
            messagebox.showinfo("Info", f"La hora {hora}:00 ya está seleccionada para {dia}.")
    
    def generar_horario(self):
        if not self.tareas or not any(self.horas_libres.values()):
            messagebox.showerror("Error", "Debe añadir tareas y horas libres.")
            return
        
        horario = crear_horario(self.tareas, self.horas_libres)
        
        # Calcular el ancho de celda basado en la tarea más larga
        max_task_length = max([len(tarea[0]) for tarea in self.tareas] or [0])
        cell_width = max(7, max_task_length)  # Asegurar un mínimo de 7 para las horas
        
        self.resultado_text.delete(1.0, tk.END)
        
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        header = "Hora     " + "".join([f"| {dia:<{cell_width}} " for dia in dias]) + "|\n"
        separator = "---------" + "+".join(["-" * (cell_width + 3)] * len(dias)) + "+\n"
        
        self.resultado_text.insert(tk.END, header)
        self.resultado_text.insert(tk.END, separator)
        
        for hora in range(8, 20):
            row = f"{hora:02d}:00   "  # Formatear la hora a dos dígitos
            for dia in dias:
                task = horario[dia].get(hora, "")
                row += f"| {task:<{cell_width}} "
            row += "|\n"
            self.resultado_text.insert(tk.END, row)

if __name__ == "__main__":
    root = tk.Tk()
    app = HorarioApp(root)
    root.mainloop()
