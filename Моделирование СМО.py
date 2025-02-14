from math import factorial

lambda_requests = 90
mu = 30
n_max = 6

rho = lambda_requests / mu

channels = list(range(1, n_max + 1))
relative_throughput = []
absolute_throughput = []

for n in channels:
    p0 = sum([(rho ** k) / factorial(k) for k in range(n + 1)]) ** -1
    p_otk = (rho ** n) / factorial(n) * p0
    Q = 1 - p_otk
    A = lambda_requests * Q
    relative_throughput.append(round(Q, 2))
    absolute_throughput.append(round(A, 1))

print(f"Интенсивность обслуживания (mu): {mu:.2f} заявок/час")
print(f"Коэффициент загрузки (rho): {rho:.2f}")
print("\nТаблица характеристик обслуживания:")
header_length = len("Характеристика обслуживания          │ Обозначение │ " + "       │ ".join(str(n) for n in channels) + "      │")
print("┌" + "─" * header_length + "┐")
print("│ Характеристика обслуживания          │ Обозначение │ " + "       │ ".join(str(n) for n in channels) + "      │")
print("├" + "─" * header_length + "┤")
print("│ Относительная пропускная способность │      Q      │ " + "  │ ".join(f"{value:>6}" for value in relative_throughput) + " │")
print("│ Абсолютная пропускная способность    │      A      │ " + "  │ ".join(f"{value:>6}" for value in absolute_throughput) + " │")
print("└" + "─" * header_length + "┘")