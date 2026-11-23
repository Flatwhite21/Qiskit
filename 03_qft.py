# 03_qft.py
from qiskit import QuantumCircuit
import numpy as np

def qft(n: int) -> QuantumCircuit:
    """QFT на n кубитах."""
    qc = QuantumCircuit(n)
    for j in range(n):
        qc.h(j)
        for k in range(j + 1, n):
            angle = np.pi / (2 ** (k - j))
            qc.cp(angle, k, j)  # управляемая фазовая вентиль
    # Перестановка кубитов (обращение порядка)
    for i in range(n // 2):
        qc.swap(i, n - i - 1)
    return qc

n_qubits = 3
qc_qft = qft(n_qubits)
print(qc_qft.draw('text'))
print(f'Глубина схемы: {qc_qft.depth()}')
print(f'Количество вентилей: {qc_qft.size()}')

