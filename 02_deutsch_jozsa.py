# 02_deutsch_jozsa.py
from qiskit import QuantumCircuit
import numpy as np

def dj_oracle(n: int, balanced: bool) -> QuantumCircuit:
    """Создаём оракул: константный (f=0) или сбалансированный."""
    oracle = QuantumCircuit(n + 1)
    if balanced:
        # XOR-оракул: переключаем вспомогательный кубит
        for qubit in range(n):
            oracle.cx(qubit, n)
    # Если константный — ничего не делаем (f=0)
    return oracle

def deutsch_jozsa(n: int, balanced: bool) -> QuantumCircuit:
    oracle = dj_oracle(n, balanced)
    qc = QuantumCircuit(n + 1, n)
    # Инициализация
    qc.x(n)          # вспомогательный кубит |1⟩
    qc.h(range(n + 1))  # Адамара на всех
    qc.barrier()
    qc.compose(oracle, inplace=True)  # применяем оракул
    qc.barrier()
    qc.h(range(n))   # Адамара на входных
    qc.measure(range(n), range(n))
    return qc

# 3-кубитная версия, сбалансированный оракул
qc_balanced = deutsch_jozsa(3, balanced=True)
print(qc_balanced.draw('text'))