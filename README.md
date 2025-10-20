# 🔀 Optimización Multi-Objetivo con `pymoo`: RVEA vs NSGA-II (ZDT1 & DTLZ2)

---

## 1. 🎯 Contexto

La **optimización multiobjetivo (MOO)** aborda problemas donde existen **dos o más objetivos en conflicto**. En lugar de buscar una única solución óptima, se persigue un **frente de Pareto**, compuesto por soluciones que representan distintos compromisos entre los objetivos.

Los algoritmos evolutivos multiobjetivo (MOEAs) permiten explorar múltiples regiones del espacio de búsqueda de manera simultánea, generando soluciones diversas y evaluando su calidad mediante indicadores como **IGD** e **Hypervolume**.

---

## 2. ⚙️ Algoritmos utilizados

- **NSGA-II (Non-dominated Sorting Genetic Algorithm II)**  
  Utiliza ordenamiento por dominancia y **crowding distance** para mantener la diversidad del frente. Muy eficaz en problemas biobjetivo con geometría continua.
  
- **RVEA (Reference Vector Guided Evolutionary Algorithm)**  
  Se guía mediante **vectores de referencia** distribuidos en el espacio objetivo, lo que permite una cobertura más uniforme en problemas con tres o más objetivos.

---

## 3. 🎯 Problemas Benchmark

| Problema | Objetivos | Geometría del Frente | Propósito |
|----------|-----------|----------------------|-----------|
| **ZDT1** | 2         | Convexo y continuo   | Evaluar convergencia y diversidad en bi-objetivo. |
| **DTLZ2** | 3        | Esférico             | Analizar comportamiento en frentes tridimensionales donde la distribución uniforme es clave. |

---

## 4. 🛠️ Parámetros experimentales

| Parámetro | Valor utilizado |
|-----------|---------------|
| Población (`pop_size`) | 100 |
| Generaciones (`n_gen`) | 100 (≈ 10,000 evaluaciones) |
| Algoritmos comparados | RVEA y NSGA-II |
| Seeds utilizadas | **ZDT1:** una por algoritmo / **DTLZ2:** una por algoritmo |
| Variables de decisión | **ZDT1:** 30 / **DTLZ2:** 12 (valores por defecto `pymoo`) |
| Métricas evaluadas | **IGD (Inverted Generational Distance)** y **HV (Hypervolume)** |

---

## 8. 📊 Resultados esperados (Comportamiento teórico)

| Problema | Algoritmo que suele destacar | Razón |
|----------|----------------------------|-------|
| **ZDT1 (2 objetivos)** | ✅ **NSGA-II** | Su mecanismo de crowding distance maneja muy bien frentes convexos y continuos. |
| **DTLZ2 (3 objetivos)** | ✅ **RVEA** | Los **vectores de referencia** guían mejor la distribución en espacios tridimensionales esféricos. |

> ⚠️ Aunque los valores exactos varían según la seed, **la tendencia cualitativa se mantiene en literatura y experimentación:**  
> **NSGA-II domina en biobjetivo**, **RVEA domina en triobjetivo**.

---

## 9. 👨‍💻 Autores

| Nombre | Matrícula |
|--------|----------|
| **José Ángel Govea García** | A01639096 |
| **José Luis Santos Montaño** | A01781721 |

---