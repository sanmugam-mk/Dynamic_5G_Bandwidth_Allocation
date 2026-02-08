import numpy as np

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


def quantum_optimize(demands, total_prbs):
    """
    QAOA-like selection using quantum sampling.
    Selects users probabilistically based on demand.
    """

    n = len(demands)

    # limit qubits for simulation safety
    n_qubits = min(n, 12)

    simulator = AerSimulator()

    qc = QuantumCircuit(n_qubits, n_qubits)

    # superposition
    qc.h(range(n_qubits))

    # bias rotation proportional to demand
    for i in range(n_qubits):
        angle = float(demands[i]) / (max(demands) + 1e-9)
        qc.ry(angle * np.pi, i)

    qc.measure(range(n_qubits), range(n_qubits))

    compiled = transpile(qc, simulator)
    result = simulator.run(compiled, shots=256).result()

    counts = result.get_counts()

    # pick most frequent bitstring
    best = max(counts, key=counts.get)

    mask = np.array(list(map(int, best[::-1])))

    allocation = np.zeros(n)

    remaining = total_prbs

    for i, select in enumerate(mask):
        if select and remaining > 0:
            alloc = min(demands[i], remaining)
            allocation[i] = alloc
            remaining -= alloc

    return allocation
