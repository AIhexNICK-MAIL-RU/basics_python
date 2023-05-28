import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score


# загрузка данных
df = pd.read_csv('gym_churn.csv')

# преобразование категориальных признаков в бинарные
df = pd.get_dummies(df, columns=['gender', 'near_location', 'partner', 'promo_friends', 'phone', 'group_visits'])

# масштабирование числовых признаков
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df.drop(['churn', 'customer_id'], axis=1))
df_scaled = pd.DataFrame(df_scaled, columns=df.drop(['churn', 'customer_id'], axis=1).columns)

# объединение преобразованных данных и целевого признака
df_scaled['churn'] = df['churn']

# разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(df_scaled.drop('churn', axis=1), df_scaled['churn'], test_size=0.2, random_state=42)

# обучение модели логистической регрессии
model = LogisticRegression()
model.fit(X_train, y_train)

# оценка F1 меры на тестовой выборке
y_pred = model.predict(X_test)
f1 = f1_score(y_test, y_pred)

print('F1 score:', f1)

# загрузка новых данных
df_test = pd.read_csv('gym_test.csv')

# преобразование категориальных признаков в бинарные
df_test = pd.get_dummies(df_test, columns=['gender', 'near_location', 'partner', 'promo_friends', 'phone', 'group_visits'])

# масштабирование числовых признаков
df_test_scaled = scaler.transform(df_test.drop('customer_id', axis=1))
df_test_scaled = pd.DataFrame(df_test_scaled, columns=df_test.drop('customer_id', axis=1).columns)

# предсказание значения целевого признака
y_test_pred = model.predict(df_test_scaled)

# сохранение результатов в файл
df_test['churn'] = y_test_pred
df_test.to_csv('gym_test_predicted.csv', index=False)
