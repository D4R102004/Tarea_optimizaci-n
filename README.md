# Tarea_optimización

Este proyecto corresponde a la **Tarea Evaluativa** de la asignatura de Modelos de Optimización.  
Su objetivo es analizar y resolver un **problema de optimización no lineal en dos variables**, aplicando dos métodos clásicos de optimización sin restricciones:  
el **Gradiente Descendente** y el **Método de Newton**.

---

## 📖 Descripción del problema

Se busca minimizar la siguiente función:

\[
f(x, y) = (2x^3y - y^3)^2 + x^2
\]

El problema es continuo, coercivo y no convexo, pero presenta un único mínimo global en el punto \((x, y) = (0, 0)\).

---

## ⚙️ Estructura del proyecto

Tarea_Optimizacion/
│
├── algoritmos/
│ ├── gradiente_descendente.py
│ ├── newton.py
│ ├── guardar_resultados.py
│
├── funcion/
│ └── function.py

├── graficar/
│ └── grafico.py
│
├── experimentos.py
├── analizar_resultados.py
├── main.py
├── resultados.json
├── resultados_completos.json
└── README.md


---

## 🧠 Algoritmos implementados

- **Gradiente Descendente:** método de primer orden basado en la dirección opuesta al gradiente.
- **Método de Newton:** método de segundo orden que usa la matriz Hessiana para ajustar el paso y la dirección.

Ambos métodos se implementaron manualmente utilizando **Autograd** para el cálculo automático de derivadas y **NumPy** para las operaciones vectoriales.

---

## 🧪 Ejecución del proyecto

1. Crear un entorno virtual y activar:
   ```bash
   python -m venv venv
   source venv/bin/activate     # Linux/Mac
   venv\Scripts\activate        # Windows

Instalar dependencias:
pip install numpy autograd matplotlib

Ejecutar los experimentos y análisis:
python main.py
