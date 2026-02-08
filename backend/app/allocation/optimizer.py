import numpy as np
from qiskit_optimization import QuadraticProgram
from qiskit_algorithms import QAOA
from qiskit.primitives import Sampler
from qiskit_optimization.algorithms import MinimumEigenOptimizer


def qaoa_chunk_optimize(prb_demands, total_prbs):
    n = len(prb_demands)

    qp = QuadraticProgram()

    for i in range(n):
        qp.binary_var(name=f"x{i}")

    qp.maximize(linear={f"x{i}": 1 for i in range(n)})

    qp.linear_constraint(
        linear={f"x{i}": prb_demands[i] for i in range(n)},
        sense="<=",
        rhs=total_prbs,
        name="limit",
    )

    sampler = Sampler()
    qaoa = QAOA(sampler=sampler, reps=2)
    optimizer = MinimumEigenOptimizer(qaoa)

    result = optimizer.solve(qp)

    return np.array(result.x)


def quantum_optimize(prb_demands, total_prbs, chunk_size=10):
    """
    Runs QAOA in chunks to scale for large users.
    """

    final_mask = []
    remaining_prbs = total_prbs

    for i in range(0, len(prb_demands), chunk_size):
        chunk = prb_demands[i:i+chunk_size]

        if remaining_prbs <= 0:
            final_mask.extend([0]*len(chunk))
            continue

        mask = qaoa_chunk_optimize(chunk, remaining_prbs)

        used = np.sum(mask * chunk)
        remaining_prbs -= used

        final_mask.extend(mask)

    return np.array(final_mask[:len(prb_demands)])
