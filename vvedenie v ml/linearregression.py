import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import DictVectorizer

traindata = pd.read_csv('salary-train.csv')
testdata = pd.read_csv('salary-test-mini.csv')

# Переводим тексты в нижний регистр
traindata['FullDescription'] = traindata['FullDescription'].str.lower()
testdata['FullDescription'] = testdata['FullDescription'].str.lower()

# Заменяем всё, кроме букв и цифр на пробелы для лучшего разбиения на слова
traindata['FullDescription'] = traindata['FullDescription'].replace('[^a-zA-Z0-9]', ' ', regex=True)
testdata['FullDescription'] = testdata['FullDescription'].replace('[^a-zA-Z0-9]', ' ', regex=True)

# Из столбца FullDescription делаем тысячи столбцов слов, которые встречаются в более чем 5 объектах
# Их значения - взвешенное среднее (TF-IDF)
# Результат - матрица а не DataFrame
vectorizer = TfidfVectorizer(min_df=5)
X = vectorizer.fit_transform(traindata['FullDescription'])
Y = vectorizer.transform(testdata['FullDescription'])

# Заполняем nan пропуски значений в столбцах LocationNormalized и ContractTime
traindata['LocationNormalized'] = traindata['LocationNormalized'].fillna('nan', inplace=True)
testdata['LocationNormalized'] = testdata['LocationNormalized'].fillna('nan', inplace=True)
traindata['ContractTime'] = traindata['ContractTime'].fillna('nan', inplace=True)
testdata['ContractTime'] = testdata['ContractTime'].fillna('nan', inplace=True)

# Из двух столбцов категориальных признаков LocationNormalized и ContractTime делаем много столбцов -
# для каждого варианта признака выделяем отдельный столбец со значением 0 или 1.
# Это называется one-hot-кодирование. Используем DictVectorizer

print(Y)
