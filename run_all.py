# run_all.py — квантовый симулятор на базе Qiskit
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator, StatevectorSimulator
import numpy as np

# ── 1. Bell State ────────────────────────────────────────────
def bell_circuit():
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    return qc

# ── 2. Deutsch–Jozsa ─────────────────────────────────────────
def dj_oracle(n, balanced):
    oracle = QuantumCircuit(n + 1)
    if balanced:
        for qubit in range(n):
            oracle.cx(qubit, n)
    return oracle

def deutsch_jozsa(n, balanced):
    oracle = dj_oracle(n, balanced)
    qc = QuantumCircuit(n + 1, n)
    qc.x(n)
    qc.h(range(n + 1))
    qc.barrier()
    qc.compose(oracle, inplace=True)
    qc.barrier()
    qc.h(range(n))
    qc.measure(range(n), range(n))
    return qc

# ── 3. QFT ───────────────────────────────────────────────────
def qft(n):
    qc = QuantumCircuit(n)
    for j in range(n):
        qc.h(j)
        for k in range(j + 1, n):
            qc.cp(np.pi / (2 ** (k - j)), k, j)
    for i in range(n // 2):
        qc.swap(i, n - i - 1)
    return qc

# ── Запуск ───────────────────────────────────────────────────
SHOTS = 1024
sim = AerSimulator()
sv  = StatevectorSimulator()

counts_bell = sim.run(transpile(bell_circuit(), sim), shots=SHOTS).result().get_counts()
print('Bell State:', counts_bell)

counts_dj = sim.run(transpile(deutsch_jozsa(3, True), sim), shots=SHOTS).result().get_counts()
print('Deutsch-Jozsa (balanced):', counts_dj)

statevec = np.asarray(sv.run(transpile(qft(3), sv)).result().get_statevector())
print('QFT amplitudes:')
for i, amp in enumerate(statevec):
    print(f'  |{i:03b}⟩: {amp:.4f}')
