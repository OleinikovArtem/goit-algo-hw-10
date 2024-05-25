import pulp

# Створення проблеми лінійного програмування
lp_problem = pulp.LpProblem("Maximize_Drink_Production", pulp.LpMaximize)

# Змінні рішення
x1 = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
x2 = pulp.LpVariable('FruitJuice', lowBound=0, cat='Continuous')

# Цільова функція
lp_problem += x1 + x2, "Total_Production"

# Обмеження
lp_problem += 2*x1 + x2 <= 100, "Water_Constraint"
lp_problem += x1 <= 50, "Sugar_Constraint"
lp_problem += x1 <= 30, "LemonJuice_Constraint"
lp_problem += 2*x2 <= 40, "FruitPuree_Constraint"

# Розв'язання проблеми
lp_problem.solve()

# Результати
lemonade_produced = x1.varValue
fruitjuice_produced = x2.varValue
total_production = lemonade_produced + fruitjuice_produced

print(f"Lemonade Produced: {lemonade_produced}")
print(f"Fruit Juice Produced: {fruitjuice_produced}")
print(f"Total Production: {total_production}")
