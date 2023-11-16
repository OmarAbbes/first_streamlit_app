import streamlit
import requests

streamlit.title('My parents new healthy diner, Thanks !')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.title('My Mom''s new healthy diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑 🍞 Avocado Toast')

import pandas
#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# streamlit.multiselect("Pick some fruits (list 2):", list(my_fruit_list.Fruit))

# my_fruit_list = my_fruit_list.set_index('Fruit') 
# streamlit.multiselect("Pick some fruits: (list 3)", list(my_fruit_list.index),['Avocado','Strawberries'])

# fruit_selected = streamlit.multiselect("show picked fruits :", list(my_fruit_list.index),[])
# fruits_to_show = my_fruit_list.loc[fruit_selected]
# streamlit.dataframe(fruits_to_show)

#streamlit.dataframe(my_fruit_list)

streamlit.header("Fruityvice Fruit Advice!")

fruitebvice_responses = requests.get ("https://fruityvice.com/api/fruit/watermelon")
streamlit.text (fruitebvice_responses.json())

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
