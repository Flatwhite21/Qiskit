# utils.py — вспомогательные функции для квантовых схем
def print_counts_table(counts: dict, total_shots: int) -> None:
    """Выводит таблицу результатов измерений с вероятностями."""
    print(f"{'Состояние':<12} {'Счётчик':>8} {'Вероятность':>14}")
    print("-" * 36)
    for state, count in sorted(counts.items()):
        prob = count / total_shots
        print(f"|{state}⟩{'':<8} {count:>8} {prob:>13.1%}")
    print("-" * 36)
    print(f"{'Итого':<12} {total_shots:>8} {'100.0%':>14}")


def theoretical_bell() -> dict:
    """Теоретические вероятности для состояния Белла."""
    return {'00': 0.5, '11': 0.5}


def check_bell(counts: dict, shots: int, tol: float = 0.05) -> bool:
    """Проверяет, что результаты Bell State в допуске от теории."""
    theory = theoretical_bell()
    for state, expected_prob in theory.items():
        got_prob = counts.get(state, 0) / shots
        if abs(got_prob - expected_prob) > tol:
            return False
    # Не должно быть |01⟩ или |10⟩
    for state in ('01', '10'):
        if counts.get(state, 0) > 0:
            return False
    return True