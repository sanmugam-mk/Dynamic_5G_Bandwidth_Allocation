import numpy as np
from qiskit_optimization import QuadraticProgram
from qiskit_algorithms import QAOA
from qiskit.primitives import Sampler
from qiskit_optimization.algorithms import MinimumEigenOptimizer


def quantum_optimize(prb_demands, total_prbs):
    """
    Select max users under PRB constraint using QAOA
    """

    num_users = len(prb_demands)

    qp = QuadraticProgram()

    # binary decision variable per user
    for i in range(num_users):
        qp.binary_var(name=f"x{i}")

    # maximize number of served users
    qp.maximize(
        linear={f"x{i}": 1 for i in range(num_users)}
    )

    # PRB constraint
    qp.linear_constraint(
        linear={f"x{i}": prb_demands[i] for i in range(num_users)},
        sense="<=",
        rhs=total_prbs,
        name="prb_limit"
    )

    # QAOA backend
    sampler = Sampler()
    qaoa = QAOA(sampler=sampler, reps=2)

    optimizer = MinimumEigenOptimizer(qaoa)

    result = optimizer.solve(qp)

    solution = np.array(result.x)

    return solution
