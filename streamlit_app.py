import streamlit 

streamlit.title('Opal Ridge healthy diner')

streamlit.header('Breakfast Menu')

streamlit.text(' 🥣 Omega 3 and Blackberry Oatmeal')
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text( '🥑🍞Avacado toast')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


#add the pick list
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

# New section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())


# Take the json version of response and normalize it 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# output should be in a single table
streamlit.dataframe(fruityvice_normalized)

#chose the fruit name column as index


#Display table on the page
#streamlit.dataframe(my_fruit_list)


