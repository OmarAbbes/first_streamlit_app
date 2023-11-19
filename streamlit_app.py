import streamlit
import requests
import snowflake.connector 
import pandas
from urllib.error import URLError

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
#create the repeatable code block (called a function)
def get_fruit_data(this_fruit) : 
    fruitevice_responses = requests.get ("https://fruityvice.com/api/fruit/" + this_fruit)
    fruityvice_normalized = pandas.json_normalize(fruitevice_responses.json())  
    return fruityvice_normalized

#new section to display data
try :
  fruit_choice = streamlit.text_input("What fruit would you like information about?")
  if not fruit_choice :
    streamlit.error("Please select a fruit to get information")
  else : 
    back_from_function = get_fruit_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except urlerror as e : 
  streamlit.error()
  
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")

streamlit.header("The fruit load list contains : ")
def get_fruit_load_list() : 
    with my_cnx.cursor() as my_cur : 
        my_cur.execute("select fruit_name as fruit_name from fruit_load_list") 
        return my_cur.fetchall()
#Add a button to load the fruit
if streamlit.button('Get fruit load list') : 
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])    
    my_data_row = get_fruit_load_list()
    streamlit.dataframe(my_data_row)

streamlit.stop()
add_my_fruit = streamlit.text_input("what fruit would you like to add ? : ")

streamlit.write ("thanks for adding " , add_my_fruit)
my_cur.execute ("insert into fruit_load_list values ('from streamlit')")

