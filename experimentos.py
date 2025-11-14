import json
import numpy as np
from funcion.function import func
from algoritmos.gradiente_descendente import gradiente_descendente
from algoritmos.newton import newton_method
from algoritmos.guardar_resultados import guardar_experimento


# ========================================================
# GENERACIÓN CONTROLADA DE PUNTOS (ROBUSTO + RÁPIDO)
# ========================================================

# 1) Cuadrícula
puntos_grid = []
for x in [-50, -25, -5, 5, 25, 50]:
    for y in [-50, -25, -5, 5, 25, 50]:
        puntos_grid.append(np.array([float(x), float(y)]))

# 2) Puntos cercanos al origen 
puntos_cerca_origen = [
    np.array([0.5, 0.5]),
    np.array([1.0, -1.0]),
    np.array([-1.0, 1.0]),
    np.array([0.1, -0.1]),
]

# 3) Puntos aleatorios moderados (10 puntos)
puntos_random = [np.random.uniform(-40, 40, size=2) for _ in range(10)]

# Lista final de puntos iniciales (36 puntos aprox.)
puntos_iniciales = puntos_grid + puntos_cerca_origen + puntos_random


# ========================================================
# PARÁMETROS DE EXPERIMENTO
# ========================================================

# Alphas
alphas = [0.01, 0.05, 0.1]  
max_iter = 2000       


# ========================================================
# EJECUCIÓN
# ========================================================

def correr_experimentos():
    resultados = []

    print(f"🔍 Ejecutando {len(puntos_iniciales)} puntos iniciales...\n")

    for punto in puntos_iniciales:
        for alpha in alphas:

            # ========================
            # GRADIENTE DESCENDENTE
            # ========================
            try:
                x_opt, history, f_opt, tiempo = gradiente_descendente(
                    func, punto, alpha0=alpha, max_iter=max_iter
                )
                resultado_gd = {
                    "algoritmo": "Gradiente Descendente",
                    "punto_inicial": punto.tolist(),
                    "alpha": alpha,
                    "resultado": {
                        "minimo": x_opt.tolist(),
                        "valor": float(f_opt),
                        "iteraciones": len(history),
                        "tiempo": tiempo,
                        "convergio": True
                    }
                }
                resultados.append(resultado_gd)
                guardar_experimento(resultado_gd)

            except Exception as e:
                resultados.append({
                    "algoritmo": "Gradiente Descendente",
                    "punto_inicial": punto.tolist(),
                    "alpha": alpha,
                    "convergio": False,
                    "error": str(e)
                })


        # ========================
        # MÉTODO DE NEWTON
        # ========================
        try:
            x_opt, history, f_opt, tiempo = newton_method(
                func, punto, max_iter=max_iter
            )
            resultado_newton = {
                "algoritmo": "Newton",
                "punto_inicial": punto.tolist(),
                "alpha": "auto",
                "resultado": {
                    "minimo": x_opt.tolist(),
                    "valor": float(f_opt),
                    "iteraciones": len(history),
                    "tiempo": tiempo,
                    "convergio": True
                }
            }
            resultados.append(resultado_newton)
            guardar_experimento(resultado_newton)

        except Exception as e:
            resultados.append({
                "algoritmo": "Newton",
                "punto_inicial": punto.tolist(),
                "alpha": "auto",
                "convergio": False,
                "error": str(e)
            })

    # Guardar archivo completo
    with open("resultados_completos.json", "w") as f:
        json.dump(resultados, f, indent=4)

    print("\n✅ Experimentos completados.")
    print("📂 Resultados guardados en 'resultados.json' y 'resultados_completos.json'.")


if __name__ == "__main__":
    correr_experimentos()
