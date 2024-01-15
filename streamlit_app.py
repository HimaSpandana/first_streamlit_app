import streamlit 
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Opal Ridge healthy diner')

streamlit.header('Breakfast Menu')

streamlit.text(' 🥣 Omega 3 and Blackberry Oatmeal')
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text( '🥑🍞Avacado toast')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


#add the pick list
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

# New section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#streamlit.text(fruityvice_response.json())


# Take the json version of response and normalize it 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# output should be in a single table
streamlit.dataframe(fruityvice_normalized)

#dont run past this line while we troubleshoot
streamlit.stop()

#import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)


fruit_choice = streamlit.text_input('What fruit would you like to add?','Jackfruit')
streamlit.write('Thanks for adding Jackfruit ')

#This will not work correctly but just go with it now
my_cur.execute("insert into fruit_load_list values('from streamlit')")


#chose the fruit name column as index
#Display table on the page
#streamlit.dataframe(my_fruit_list)
