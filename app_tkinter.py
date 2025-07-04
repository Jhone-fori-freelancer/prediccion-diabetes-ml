import tkinter as tk
from tkinter import messagebox
import joblib

model = joblib.load('modelo_diabetes.pkl')

def predecir():
    try:
        datos = [float(entry.get()) for entry in entradas]
        prediccion = model.predict([datos])
        resultado = "Positivo (diabetes)" if prediccion[0] == 1 else "Negativo (no diabetes)"
        messagebox.showinfo("Resultado", resultado)
    except:
        messagebox.showerror("Error", "Verifica los datos ingresados.")

ventana = tk.Tk()
ventana.title("Predicción de Diabetes")

campos = ['Embarazos', 'Glucosa', 'Presión', 'Pliegue', 'Insulina', 'IMC', 'Pedigrí', 'Edad']
entradas = []

for campo in campos:
    tk.Label(ventana, text=campo).pack()
    entry = tk.Entry(ventana)
    entry.pack()
    entradas.append(entry)

tk.Button(ventana, text="Predecir", command=predecir).pack()
ventana.mainloop()
