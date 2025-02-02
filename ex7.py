import numpy as np
import matplotlib.pyplot as plt

# Симуляція 100,000 кидків двох кубиків
throws = 100000
dice1 = np.random.randint(1, 7, size=throws)
dice2 = np.random.randint(1, 7, size=throws)

# Суми чисел на двох кубиках
sums = dice1 + dice2

# Підрахунок ймовірностей для кожної можливої суми
sum_counts = {i: np.sum(sums == i) for i in range(2, 13)}

# Обчислення ймовірностей
probabilities = {key: value / throws for key, value in sum_counts.items()}

# Теоретичні ймовірності
theoretical_probabilities = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
    8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}

# Виведення результатів
print("Симульовані ймовірності:")
for i in range(2, 13):
    print(f"Сума {i}: {probabilities[i]:.4f}")

print("\nТеоретичні ймовірності:")
for i in range(2, 13):
    print(f"Сума {i}: {theoretical_probabilities[i]:.4f}")

# Візуалізація результатів
labels = [str(i) for i in range(2, 13)]
simulated_vals = [probabilities[i] for i in range(2, 13)]
theoretical_vals = [theoretical_probabilities[i] for i in range(2, 13)]

x = np.arange(2, 13)
width = 0.35

fig, ax = plt.subplots()
bars1 = ax.bar(x - width / 2, simulated_vals, width, label='Симульовані')
bars2 = ax.bar(x + width / 2, theoretical_vals, width, label='Теоретичні')

ax.set_xlabel('Сума')
ax.set_ylabel('Ймовірність')
ax.set_title('Ймовірності для різних сум при киданні двох кубиків')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()
