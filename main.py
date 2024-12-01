import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Создаём DataFrame с данными
data = {
    "День": ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"],
    "Продажи": [200, 150, 300, 250, 400]
}
df = pd.DataFrame(data)

# Выводим таблицу данных
print(df)
print(np.random.randint(1, 100, size=10) * 3)
# Построение графика
plt.figure(figsize=(8, 5))  # Размер графика
plt.plot(df["День"], df["Продажи"], marker="o", linestyle="-", color="b", label="Продажи")
plt.title("Продажи за неделю")  # Заголовок графика
plt.xlabel("День")  # Подпись оси X
plt.ylabel("Продажи")  # Подпись оси Y
plt.grid(True)  # Включение сетки
plt.legend()  # Отображение легенды
plt.show()
