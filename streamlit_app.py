import streamlit
import requests
import snowflake.connector 

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

fruit_choice = streamlit.text_input("What fruit would you like information about?" , "kiwi")
streamlit.write ("The user entered", fruit_choice)

fruitevice_responses = requests.get ("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text (fruitevice_responses.json())

fruityvice_normalized = pandas.json_normalize(fruitevice_responses.json())
streamlit.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from fruit_load_list") ; 
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains : ")
streamlit.text(my_data_row)
