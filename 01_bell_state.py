# 01_bell_state.py
from qiskit import QuantumCircuit

def bell_circuit() -> QuantumCircuit:
    qc = QuantumCircuit(2, 2)
    qc.h(0)        # Адамара на q0 → суперпозиция
    qc.cx(0, 1)    # CNOT: запутываем q0 и q1
    qc.measure([0, 1], [0, 1])
    return qc

circuit = bell_circuit()
print(circuit.draw('text'))