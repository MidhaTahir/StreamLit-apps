import streamlit as st
import numpy as np

st.title('Streamlit')
st.header('This is a header')
st.subheader('This is a sub_header')
st.text('Hello streamlit')
st.markdown('### This is a Markdown')
st.markdown('__bold__')
st.markdown('_italics_')
st.success('Successful')
st.info('Information')
st.warning('Warning')
st.exception("NameError('Name three not defined')")

st.help(range)

st.write(range(10))

#The Write function is the swiss-army knife of the Streamlit commands. It behaves differently based on its input. For example, if you throw in a Matplotlib figure it will automatically show you that visualization.
# A few examples:
# write(string) : Prints the formatted Markdown string.
# write(data_frame) : Displays the DataFrame as a table.
# write(dict) : Displays dictionary in an interactive widget.
# write(keras) : Displays a Keras model.
# write(plotly_fig) : Displays a Plotly figure.

#image
from PIL import Image
img = Image.open('email-sign.png')
st.image(img,width=800,caption="Sign")

#videos
vid_file = open('video.mp4',"rb").read()
# vid_bytes = vid_file.read()
st.video(vid_file)

#Audio
audio_file = open('sense.mp3','rb').read()
st.audio(audio_file,format='audio/mp3')

#widgets

#select box
age = st.selectbox("Choose your age: ", np.arange(18, 66, 1))

occupation = st.selectbox('Choose occupation',["Programmer", "DataScientist" , "DataAnalyst"])
st.write("You selected this option",occupation)

#slider
age = st.slider("Choose your age: ", min_value=16,max_value=66, value=35, step=1)

#multiselect
artists = st.multiselect("Who are your favorite artists?", 
                         ["Michael Jackson", "Elvis Presley",
                         "Eminem", "Billy Joel", "Madonna"])
st.write("You selected", len(artists) , " artists that are: ",artists)        

#checkbox
if st.checkbox('Show/Hide'):
    st.text('Showing or Hiding Widget')

#Radio
status = st.radio('What is your gender',('Man','Woman'))

if status == "Man":
    st.text(f'Hey {status}')
else:
    st.text(f'Hey {status}')


#buttons
if st.button("About"):
    st.text("It's cool")


#Text Input
first_name = st.text_input("Enter your first name","Type Here .. ")
message = st.text_area("Enter your message","Type Here .. ")
if st.button("Submit"):
    result = first_name.title()
    result1 = message
    st.success(f"Successful you entered {result}, {result1}")

#date 
import datetime
datehere = st.date_input("Date", datetime.datetime.now())
timehere = st.time_input("The time: ",datetime.time())

st.text('Raw Code')
st.code("import numpy as np")

#progress bar
import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p+1)

#spinner
with st.spinner("Waiting .. "):
    time.sleep(5)
st.success("Finish")

# Balloons
st.balloons()


#Sidebars
st.sidebar.header("About")
st.sidebar.text("This is Streamlit")

#function
def run_fun():
    return range(100)

st.write(run_fun())


# #plot 
# st.pyplot()
# #Dataframe
# st.dataframe(df)
# #Tables
# st.table(df)


# with st.echo:
#     #this will show comment also 
#     import pandas as pd  
#     df = pd.DataFrame()

#Display JSON
# st.text('Display JSON')
# st.json({"name":"John", "age":31, "city":"New York"})