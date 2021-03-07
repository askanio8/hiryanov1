import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('_ea07570741a3ec966e284208f588e50e_titanic.csv', index_col='PassengerId')

# Найтии зависимость выживания от класса, пола, возраста и цены билета
dataN = data.filter(items=['Survived', 'Pclass', 'Sex', 'Age', 'Fare'])  # Оставляем 5 столбцов
dataN = dataN[dataN['Age'].notnull()]  # Оставляем только сторки, в которых указан возраст
dataX = dataN.filter(items=['Pclass', 'Sex', 'Age', 'Fare'])  # Входные значения
dataY = dataN.filter(items=['Survived'])  # Выходные значения
mapping ={'male': 0, 'female': 1}  # Словарь для замены текста на число
dataX = dataX.replace(mapping)  # Замена

clf = DecisionTreeClassifier(random_state=241)  # В данном случае зерно случайности мало влияет на результат обучения
clf.fit(dataX, dataY)  # Обучение
importances = clf.feature_importances_  # Показывает важность признаков

p = clf.predict([[3, 0, 10, 100]])  # Это предсказывает! 0 или 1

print(p)
print(importances)