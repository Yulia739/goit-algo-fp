# Жадібний алгоритм
def greedy_algorithm(items, budget):
    # Створюємо список страв з їх співвідношенням калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_calories = 0
    total_cost = 0
    selected_items = []

    for item, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            selected_items.append(item)
            total_calories += info['calories']
            total_cost += info['cost']

    return selected_items, total_calories, total_cost

# Тестування жадібного алгоритму
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
greedy_result = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", greedy_result[0])
print("Загальна калорійність:", greedy_result[1])
print("Загальна вартість:", greedy_result[2])


# Алгоритм динамічного програмування
def dynamic_programming(items, budget):
    # Ініціалізація таблиці для динамічного програмування
    dp = [0] * (budget + 1)  # dp[i] буде зберігати максимальні калорії для бюджету i
    
    # Для кожної страви оновлюємо таблицю dp
    for item, info in items.items():
        cost, calories = info['cost'], info['calories']
        for i in range(budget, cost - 1, -1):  # Ідемо від максимального бюджету до вартості страви
            dp[i] = max(dp[i], dp[i - cost] + calories)

    # Визначаємо максимальні калорії та вибираємо страви
    max_calories = dp[budget]
    selected_items = []
    remaining_budget = budget
    
    # Повертаємо страви, які забезпечують максимальні калорії
    for item, info in items.items():
        cost, calories = info['cost'], info['calories']
        if remaining_budget >= cost and dp[remaining_budget] == dp[remaining_budget - cost] + calories:
            selected_items.append(item)
            remaining_budget -= cost

    return selected_items, max_calories

# Тестування алгоритму динамічного програмування
dp_result = dynamic_programming(items, budget)
print("\nАлгоритм динамічного програмування:")
print("Вибрані страви:", dp_result[0])
print("Загальна калорійність:", dp_result[1])
