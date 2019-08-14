from pymoo.factory import get_problem, get_sampling, get_crossover, get_mutation
from pymoo.optimize import minimize
from pymoo.algorithms.nsga2 import NSGA2
from pymoo.util import plotting

problem = get_problem("zdt5")

algorithm = NSGA2(pop_size=100,
                  sampling=get_sampling("bin_random"),
                  crossover=get_crossover("bin_two_point"),
                  mutation=get_mutation("bin_bitflip"),
                  elimate_duplicates=True)

res = minimize(problem,
               algorithm,
               ('n_gen', 300),
               seed=1,
               verbose=False)

plotting.plot(res.F, no_fill=True)