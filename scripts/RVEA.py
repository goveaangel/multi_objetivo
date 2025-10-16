from pymoo.algorithms.moo.rvea import RVEA
from pymoo.optimize import minimize
from pymoo.problems import get_problem
from pymoo.util.ref_dirs import get_reference_directions
from pymoo.indicators.igd import IGD
from pymoo.indicators.hv import HV
import numpy as np

# configuración
problem = get_problem("zdt1")  # el profe usa zdt1, no dtlz1
ref_dirs = get_reference_directions("das-dennis", problem.n_obj, n_partitions=12)

algorithm = RVEA(ref_dirs=ref_dirs, pop_size=100)

# ejecutar multiples veces
results = []
for seed in [42, 123, 456]:
    res = minimize(problem,
                   algorithm,
                   ('n_gen', 100),
                   seed = seed,
                   verbose=False)
    results.append(res)



