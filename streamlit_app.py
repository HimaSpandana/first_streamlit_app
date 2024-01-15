import streamlit 
import snowflake.connector
import pandas
import requests

streamlit.title('Opal Ridge healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text(' 🥣 Omega 3 and Blackberry Oatmeal')
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado toast')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Add the pick list
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

# New section to display fruityvice API response
streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered', fruit_choice)

# Define the Snowflake cursor here
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

try:
    my_cur.execute("select * from fruit_load_list")
    my_data_row = my_cur.fetchone()
    streamlit.text("The fruit load list contains:")
    streamlit.text(my_data_row)
except Exception as e:
    streamlit.error(f"Error executing SQL query: {e}")

# Continue with the rest of your code
