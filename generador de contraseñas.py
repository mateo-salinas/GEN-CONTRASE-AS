import random
import string
import tkinter as tk
from tkinter import messagebox


def generar_contrasena():
  """Valida la configuración seleccionada y genera una contraseña aleatoria.

  Asegura que se incluya al menos un carácter de cada tipo seleccionado.
  """
  # 1. Validación de entrada de longitud (Estructura Lógica)
  try:
    longitud = int(spin_longitud.get())
    if longitud < 8 or longitud > 32:
      raise ValueError("Longitud fuera del rango permitido")
  except ValueError:
    messagebox.showwarning(
        "Configuración no válida",
        "Por favor, ingresa una longitud válida entre 8 y 32.",
    )
    return

  # 2. Lectura de opciones de caracteres elegidas por el usuario
  incluir_mayus = var_mayus.get()
  incluir_minus = var_minus.get()
  incluir_nums = var_nums.get()
  incluir_simbols = var_simbols.get()

  # Validar que al menos un tipo de carácter esté seleccionado
  if not (incluir_mayus or incluir_minus or incluir_nums or incluir_simbols):
    messagebox.showerror(
        "Configuración no válida",
        "Debes seleccionar al menos un tipo de carácter.",
    )
    return

  # 3. Preparación del conjunto de caracteres
  conjunto_caracteres = ""
  garantizados = []

  if incluir_mayus:
    conjunto_caracteres += string.ascii_uppercase
    garantizados.append(random.choice(string.ascii_uppercase))
  if incluir_minus:
    conjunto_caracteres += string.ascii_lowercase
    garantizados.append(random.choice(string.ascii_lowercase))
  if incluir_nums:
    conjunto_caracteres += string.digits
    garantizados.append(random.choice(string.digits))
  if incluir_simbols:
    conjunto_caracteres += string.punctuation
    garantizados.append(random.choice(string.punctuation))

  # 4. Generación repetitiva de la contraseña (Estructura Repetitiva / Bucle)
  longitud_restante = longitud - len(garantizados)
  restantes = [
      random.choice(conjunto_caracteres) for _ in range(longitud_restante)
  ]

  # Combinar y mezclar caracteres
  contrasena_lista = garantizados + restantes
  random.shuffle(contrasena_lista)
  contrasena_final = "".join(contrasena_lista)

  # 5. Mostrar resultado en la interfaz
  entry_resultado.delete(0, tk.END)
  entry_resultado.insert(0, contrasena_final)


def copiar_portapapeles():
  """Copia la contraseña mostrada en pantalla al portapapeles."""
  texto = entry_resultado.get()
  if texto:
    ventana.clipboard_clear()
    ventana.clipboard_append(texto)
    messagebox.showinfo("Éxito", "¡Contraseña copiada al portapapeles!")
  else:
    messagebox.showwarning("Atención", "No hay contraseña para copiar.")


# --- Interfaz Gráfica con Tkinter ---
ventana = tk.Tk()
ventana.title("Generador de Contraseñas Seguras")
ventana.geometry("380x420")
ventana.config(padx=20, pady=20)
ventana.resizable(False, False)

# Componentes visuales
tk.Label(
    ventana, text="Generador de Contraseñas", font=("Arial", 14, "bold")
).pack(pady=5)
tk.Label(
    ventana, text="Longitud de la contraseña (8 - 32):", font=("Arial", 10)
).pack(anchor="w", pady=(5, 0))

spin_longitud = tk.Spinbox(ventana, from_=8, to=32, width=10, font=("Arial", 10))
spin_longitud.delete(0, "end")
spin_longitud.insert(0, "12")
spin_longitud.pack(anchor="w", pady=5)

# Variables y casillas de selección
var_mayus = tk.BooleanVar(value=True)
var_minus = tk.BooleanVar(value=True)
var_nums = tk.BooleanVar(value=True)
var_simbols = tk.BooleanVar(value=True)

tk.Checkbutton(
    ventana, text="Incluir Mayúsculas (A-Z)", variable=var_mayus
).pack(anchor="w")
tk.Checkbutton(
    ventana, text="Incluir Minúsculas (a-z)", variable=var_minus
).pack(anchor="w")
tk.Checkbutton(ventana, text="Incluir Números (0-9)", variable=var_nums).pack(
    anchor="w"
)
tk.Checkbutton(
    ventana, text="Incluir Símbolos (!@#$)", variable=var_simbols
).pack(anchor="w")

# Botones de acción
btn_generar = tk.Button(
    ventana,
    text="Generar Contraseña",
    bg="#4CAF50",
    fg="white",
    font=("Arial", 10, "bold"),
    command=generar_contrasena,
)
btn_generar.pack(fill="x", pady=15)

entry_resultado = tk.Entry(
    ventana, width=28, font=("Arial", 12), justify="center"
)
entry_resultado.pack(pady=5)

btn_copiar = tk.Button(
    ventana,
    text="Copiar al portapapeles",
    font=("Arial", 10),
    command=copiar_portapapeles,
)
btn_copiar.pack(fill="x", pady=5)

ventana.mainloop()