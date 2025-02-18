# goit-algo-fp
Homework on topic Final project


EX7

# Теоретичні ймовірності
Теоретичні ймовірності для кожної можливої суми при киданні двох кубиків можна обчислити, враховуючи можливі варіанти, як можуть випадати числа на двох кубиках. Ось ймовірності для кожної суми:

| Сума | Теоретична ймовірність |
|------|------------------------|
| 2    | 1/36 = 0.0278           |
| 3    | 2/36 = 0.0556           |
| 4    | 3/36 = 0.0833           |
| 5    | 4/36 = 0.1111           |
| 6    | 5/36 = 0.1389           |
| 7    | 6/36 = 0.1667           |
| 8    | 5/36 = 0.1389           |
| 9    | 4/36 = 0.1111           |
| 10   | 3/36 = 0.0833           |
| 11   | 2/36 = 0.0556           |
| 12   | 1/36 = 0.0278           |

Ці ймовірності отримуються, виходячи з можливих варіантів для кожної суми. Наприклад, для суми 7 є 6 варіантів (1+6, 2+5, 3+4, 4+3, 5+2, 6+1), що дає ймовірність 6/36.

# Результати Монте-Карло
Після виконання симуляції на 100,000 кидків, отримано наступні ймовірності:

| Сума | Симульована ймовірність |
|------|-------------------------|
| 2    | 0.0276                  |
| 3    | 0.0551                  |
| 4    | 0.0820                  |
| 5    | 0.1110                  |
| 6    | 0.1386                  |
| 7    | 0.1667                  |
| 8    | 0.1376                  |
| 9    | 0.1106                  |
| 10   | 0.0823                  |
| 11   | 0.0563                  |
| 12   | 0.0278                  |

# Порівняння результатів
# Відповідність теоретичних та симульованих ймовірностей:
- **Суми 2 та 12**: Ймовірності досить точно збігаються з теоретичними значеннями, з незначними відхиленнями (симульована ймовірність 0.0276 та 0.0278 порівняно з теоретичною 0.0278).
- **Сума 7**: Це найбільш ймовірна сума, і симульована ймовірність 0.1667 точно збігається з теоретичною ймовірністю 0.1667.
- **Суми 3 та 11**: Симульовані ймовірності близькі до теоретичних, з деякими незначними коливаннями, що характерно для ймовірнісних методів.
- **Суми 4, 5, 6, 8, 9, 10**: Різниця між симульованими та теоретичними ймовірностями є незначною. Наприклад, для суми 5, симульована ймовірність 0.1110 і теоретична 0.1111.

# Висновок
Отримані ймовірності, обчислені за допомогою методу Монте-Карло, дуже близькі до теоретичних значень. Це підтверджує, що метод Монте-Карло є точним інструментом для оцінки ймовірностей у задачах подібного типу. Відмінності між симульованими та теоретичними значеннями можуть бути пояснені випадковими коливаннями при симуляціях, але ці відхилення зменшуються при збільшенні кількості кидків.

Завдяки великій кількості ітерацій (100,000 кидків) симуляція дає точні результати, що підтверджує правильність роботи методу Монте-Карло.

# Заключення
Метод Монте-Карло продемонстрував хорошу точність у розрахунках ймовірностей для випадання різних сум при киданні двох кубиків. Отримані симульовані ймовірності добре узгоджуються з теоретичними значеннями, що вказує на правильність виконаних розрахунків.
