import tkinter as tk

# Creamos la ventana principal
ventana = tk.Tk()
ventana.geometry('300x200')

# ------ SCALE ------
# Creamos el widget Scale
scale = tk.Scale(ventana, from_=0, to=100, orient='horizontal')
scale.pack(pady=20)

# Definimos una función que se ejecutará cuando se cambie el valor del Scale


def imprimir_valor(valor):
    print(f'El valor seleccionado es {valor}')


# Asociamos la función con el evento 'command' del Scale
scale.config(command=imprimir_valor)
# ----------------------------------------

# ------ CHECKBOX ------
# Creamos una variable Tkinter para almacenar el estado del Checkbox
var_checkbox = tk.BooleanVar()

# Creamos un objeto Checkbox y lo ubicamos en la ventana
checkbox = tk.Checkbutton(ventana, text="Habilitar", variable=var_checkbox)
checkbox.pack()

# Creamos una función para manejar el evento de clic del Checkbox


def clic_checkbox():
    if var_checkbox.get():
        print("Checkbox seleccionado")
    else:
        print("Checkbox no seleccionado")


# Asignamos la función de clic al Checkbox
checkbox.config(command=clic_checkbox)
# ----------------------------------------

# ------ RADIOBUTTON ------
# Creamos una variable Tkinter para almacenar la selección del Radiobutton
var_radiobutton = tk.StringVar()

# Creamos los objetos Radiobutton y los ubicamos en la ventana
radiobutton1 = tk.Radiobutton(
    ventana, text="Opción 1", variable=var_radiobutton, value="Opción 1")
radiobutton1.pack()

radiobutton2 = tk.Radiobutton(
    ventana, text="Opción 2", variable=var_radiobutton, value="Opción 2")
radiobutton2.pack()

radiobutton3 = tk.Radiobutton(
    ventana, text="Opción 3", variable=var_radiobutton, value="Opción 3")
radiobutton3.pack()

# Creamos una función para manejar la selección del Radiobutton


def seleccion_radiobutton():
    print("Selección: " + var_radiobutton.get())


# Asignamos la función de selección a los Radiobutton
radiobutton1.config(command=seleccion_radiobutton)
radiobutton2.config(command=seleccion_radiobutton)
radiobutton3.config(command=seleccion_radiobutton)
# ----------------------------------------


# Iniciamos el bucle principal de la aplicación
ventana.mainloop()
