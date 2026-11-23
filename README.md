# Qiskit Quantum Simulator Lab

Квантовый симулятор на базе Qiskit 1.1 + Aer 0.14. Реализованы три схемы: Bell State, Deutsch–Jozsa, QFT.

## Быстрый старт

```bash
# 1. Установить Python 3.11 (если нет)
brew install python@3.11

# 2. Создать и активировать виртуальное окружение
python3.11 -m venv qiskit-env
source qiskit-env/bin/activate

# 3. Установить зависимости
pip install qiskit==1.1.0 qiskit-aer==0.14.2 qiskit-ibm-runtime==0.23.0 matplotlib pylatexenc

# 4. Запустить симуляцию
python run_all.py
```

## Ожидаемый вывод

```
Bell State: {'11': ~512, '00': ~512}
Deutsch-Jozsa (balanced): {'111': 1024}
QFT amplitudes: |000⟩–|111⟩: 0.3536+0.0000j
```

## Файлы

| Файл | Описание |
|---|---|
| `run_all.py` | Основной скрипт — все три схемы и запуск |
| `utils.py` | Вспомогательные функции (таблица результатов, проверка Bell) |
| `README.md` | Этот файл |
