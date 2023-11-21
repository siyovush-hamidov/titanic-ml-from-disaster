import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Загрузите модель
model = joblib.load('titanic-ml-from-disaster.joblib')

# Создайте функцию для обработки входных данных
def process_input(sex, age, fare, is_alone):
    # Преобразуйте пол в числовое значение
    if sex == 'Мужчина':
        sex = 0
    else:
        sex = 1
    # Верните DataFrame
    return pd.DataFrame({'Pclass': [2], 'Sex': [sex], 'Age': [age], 'SibSp': [0], 'Parch': [0], 'Fare': [fare], 'Embarked': [0], 'Relatives': [0], 'Is_Alone': [is_alone], 'Title': [1], 'Deck': [3], 'Age_Class': [age * 1], 'Fare_per_Person': [0]})

# Создайте форму для ввода данных
st.markdown("<h1 style='text-align: center; color: black;'>Выживете ли вы на Титанике?</h1>", unsafe_allow_html=True)
st.image('https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/ca6c7bc7-3c52-482a-9d4c-5043d91da7c3/dfpb7y1-bfff4c04-4e77-4af6-bda0-a8060abb8097.png/v1/fill/w_900,h_1303,q_80,strp/my_titanic_poster_2023_editon_by_doodle_for_adventure_dfpb7y1-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTMwMyIsInBhdGgiOiJcL2ZcL2NhNmM3YmM3LTNjNTItNDgyYS05ZDRjLTUwNDNkOTFkYTdjM1wvZGZwYjd5MS1iZmZmNGMwNC00ZTc3LTRhZjYtYmRhMC1hODA2MGFiYjgwOTcucG5nIiwid2lkdGgiOiI8PTkwMCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.F4woajhvJRW4DDE3vk1GnDTVZ_-NKewPb2_IjUn4q2E', caption='Я считаю, что жизнь — это подарок, и я не собираюсь тратить его зря. Вы не знаете, какую руку вам раздадут следующей. Вы учитесь принимать жизнь такой, какая она есть... чтобы каждый день был важен. Джек', use_column_width=True)
message = st.text_area('Имя')
st.text_input('Имя')
sex = st.selectbox('Пол', ['Мужчина', 'Женщина'])
age = st.slider('Возраст', 1, 100, 30)

if(age <= 11):
    age = 0
elif(age > 11 and age <= 18):
    age = 1
elif(age > 18 and age <= 22):
    age = 2
elif(age > 22 and age <= 27):
    age = 3
elif(age > 27 and age <= 33):
    age = 4
elif(age > 33 and age <= 40):
    age = 5
elif(age > 40 and age <= 66):
    age = 6
elif(age > 66):
    age = 7

fare = st.slider('Недельный заработок', 0, 1000, 100)

if(fare <= 8):
    fare = 0
elif(fare > 8 and fare <= 14):
    fare = 1
elif(fare > 14 and fare <= 31):
    fare = 2
elif(fare > 31 and fare <= 99):
    fare = 3
elif(fare > 99 and fare <= 250):
    fare = 4
elif(fare > 250):
    fare = 5

is_alone = st.selectbox('Брак', [0, 1])

# Обработайте входные данные
input_df = process_input(sex, age, fare, is_alone)

# Сделайте прогноз
if st.button('Узнать'):
    prediction = model.predict(input_df)[0]
    # Выведите прогноз
    if prediction == 0:
        st.markdown("<h1 style='text-align: center; color: black;'>К сожалению, этот пассажир не выжил после крушения лайнера...</h1>", unsafe_allow_html=True)
    else:
        st.markdown("<h1 style='text-align: center; color: black;'>К счастью, пассажир выжил после крушения лайнера!</h1>", unsafe_allow_html=True)
