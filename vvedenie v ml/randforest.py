# Stacking - Результаты множества плохих моделей(возможно разнотипных) передаются на входы другой модели вместе
# с исходными признаками

# Bagging(собственно random forest) - Результаты множества плохих моделей одного типа усредняются, прогноз должен
# быть лучше. Для того, чтобы построенные деревья отличались друг от друга, каждое из них обучают на подмножестве
# признаков подмножества объектов обучающей выборки (в случае нейросетей также не достаточно перемешать объекты и
# использовать другое случайное зерно из за проблемы декореляции - если подвыборки очень большие, то построенные
# модели будут слишком похожи. Это и есть проблема слишком больших сетей - много одинаково бученных нейронов
# дублируют друг друга)
# Информативность каждого признака измеряется путем премешивания значений этого признака в обучающей выборке.
# Затем обучающая выборка подаётся в модель и сравнивается результат с нормальной выборкой. Неинформативные
# признаки потом можно выбросить, возможно модель улучшится.

# Boosting - взвешенный бэггинг.
# Градиентный бустинг - оценка ошибок y-y0 плохих моделей передаются следующей модели, во время обучения модель
# получает сам объект и ошибку на нём предыдущих моделей. У каждой модели есть вес α.Количество моделей подбирается
# с помощью требуемой ошибки или её градиента
# Adaboost - каждому объекту обучающей выборки назначается вес 1/l, Затем строитя простая модель, вычисляется
# взвешенная по весам объектов ошибка обучения. В зависимости от неё по простой эмпиричесой формуле вычисляем вес
# этой модели. Пересчитываем веса объектов, чем больше была ошибка на объекте, тем больший вес он получает. Норм
# ируем веса объектов, чтобы в сумме было 1. Строим следующую модель, она будет больше внимания обрашать на объекты
# с большим весом... Должен быть критерий останова. Adaboost чувствителен к выбросам, модели после 20 стоит
# проверить веса объектов, объекты с большими весами возможно выбросы. Adaboost можно использовать в качестве
# детектора выбросов во время подготовки обучающей выборки к другим алгоритмам.
# Xgboost - градиентный бустинг с регуляризацией по весам моделей и по количеству листьев деревьев
