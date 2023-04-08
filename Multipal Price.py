import pickle
import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
Diamond = pickle.load(open('C:/Diamnod_Model.sav', 'rb'))

Flight = pickle.load(open('C:/Flight_Price_Model.sav', 'rb'))

House = pickle.load(open('C:/US_House_Price_Model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Price Prediction System',
                          
                          ['Diamond Price Prediction',
                           'Flight Price Prediction',
                           'US Hosue Price Prediction'],
                          #icons=["gem","airplane","House"],
                          default_index=0)


#with st.sidebar:
    #selected = option_menu("Main Menu", ["Home", 'Settings'], 
        #icons=['house', 'gear'], menu_icon="cast", default_index=1)
    #selected

# horizontal Menu
#selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
    #icons=['house', 'cloud-upload', "list-task", 'gear'], 
    #menu_icon="cast", default_index=0, orientation="horizontal")
#selected2

## Diamond Price Prediction Page
if (selected == 'Diamond Price Prediction'):

    st.markdown("<h1 style='text-align: center; font-family: algerian; color:black;'>DIAMOND PRICE PREDICTION</h1>", unsafe_allow_html=True)

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:

        carat = st.number_input(label='Enter carat value in range 0.2-5.01',step=1.,format="%.2f")

    with col2:
    #i= st.text_input("Enter dimaond cut quality from '['Ideal','Premium','Good','Very Good','Fair']':")
    #st.write('Dimaond cut quality is :', i)
    #cut=8

        i = st.selectbox('Select dimaond cut quality',(' ','Ideal','Premium','Good','Very Good','Fair'))
        #st.write(' Selected Option Is:',i)
        cut=0

        if i=='Ideal':
            cut=2
        elif i == 'Premium':
            cut=3
        elif i == 'Good':
            cut=1
        elif i=='Very Good':
            cut =4
        elif i=='Fair':
            cut=0

    #st.write('your cut quality value is:', cut)
    #print("your cut quality value is:",cut)


    with col3:
   # j= st.text_input("Enter dimaond color grading from '['E','I','J','H','F','G','D']':")
    #st.write('Dimaond color garde is :', j)
    #color=100

    
        j = st.selectbox('Select dimaond color grading',(' ','E','I','J','H','F','G','D'))
        #st.write(' Selected Option Is:',j)
        color=0

        if j=='E':
            color=1
        elif j=='I':
            color=5
        elif j=='J':
            color=6
        elif j=='H':
            color=4
        elif j=='F':
            color=2
        elif j=='G':
            color=3
        elif j=='D':
            color=0

        #st.write('your diamond color garde value is:',color)
        #print("your diamond color garde value is:",color)


    with col1:
    #k= st.text_input("Enter dimaond clarity from '['SI2','SI1','VS1','VS2','VVS2','VVS1','I1','IF']':")
    #st.write('Dimaond clarity is :', k)
    #clarity=100

        k = st.selectbox('Select dimaond clarity',(' ','SI2','SI1','VS1','VS2','VVS2','VVS1','I1','IF'))
        #st.write(' Selected Option Is:',k)
        clarity=0

    
    
    
        if k=='SI2':
            clarity=3
        elif k=='SI1':
            clarity=2
        elif k=='VS1':
            clarity=5
        elif k=='VS2':
            clarity=7
        elif k=='VVS2':
            clarity=6
        elif k=='VVS1':
            clarity=4
        elif k=='I1':
            clarity=0
        elif k=='IF':
            clarity=1

        #st.write('Your clarity value is:',clarity)
        #print("Your clarity value is:",clarity)


    with col2:
        depth = st.number_input(label='Enter depth value ',step=1.,format="%.2f")

    with col3:

        table = st.number_input(label='Enter table value ',step=1.,format="%.2f")

    with col1:

        length = st.number_input(label='Enter length value ',step=1.,format="%.2f")


    with col2:

        width = st.number_input(label='Enter width value ',step=1.,format="%.2f")

    with col3:    

        hight = st.number_input(label='Enter hight value ',step=1.,format="%.2f")


  

   



    if st.button('Click to check price'):
        price = Diamond.predict([[carat,cut,color,clarity,depth,table,length,width,hight]])
        st.subheader('Price Of Diamond')
        st.subheader('$'+str(np.round(price[0], 2)))



## Flight Price Prediction Page
if (selected == 'Flight Price Prediction'):

    st.markdown("<h1 style='text-align: center; font-family: algerian; color:black;'>DOMESTIC FLIGHT PRICE PREDICTION</h1>", unsafe_allow_html=True)

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        #print("'SpiceJet'=4, 'AirAsia'=0, 'Vistara'=5, 'GO_FIRST'=2, 'Indigo'=3,'Air_India'=1")
        #i = str(input('Enetre airline above list:'))

        i = st.selectbox('Select Airline',(' ','SpiceJet', 'AirAsia', 'Vistara', 'GO_FIRST', 'Indigo','Air_India'))
        #st.write(' Selected Option Is:',i)
        airline=0

        #airline=0
        #print("your entered airline is:",i)

        if i=='SpiceJet':
             airline=4
        elif i == 'AirAsia':
            airline=0
        elif i == 'Vistara':
            airline=5
        elif i=='GO_FIRST':
            airline=2
        elif i=='Indigo':
            airline=3
        elif i=='Air_India':
            airline=1
        #print("your airline value is:",airline)

        #print(" --------")



        
    with col2:
       
        #print("'Evening'=2, 'Early_Morning'=1, 'Morning'=4, 'Afternoon'=0, 'Night'=5,'Late_Night'=3")
        #j=str(input("Enetre departure_time From above list:"))
        #departure_time=0
        #print("your entered departure_time is:",j)

        j = st.selectbox('Select Departure_time',(' ','Evening', 'Early_Morning', 'Morning', 'Afternoon', 'Night','Late_Night'))
        #st.write(' Selected Option Is:',j)
        departure_time=0

        if j=='Evening':
            departure_time=2
        elif j=='Early_Morning':
            departure_time=1
        elif j=='Morning':
            departure_time=4
        elif j=='Afternoon':
            departure_time=0
        elif j=='Night':
            departure_time=5
        elif j=='Late_Night':
            departure_time=3

        #print("Your departure_time value is:",departure_time)
        #print(" --------")
    
    with col3:
    
    #print("'zero'=2, 'one'=0, 'two_or_more'=1")
    #k=str(input("Enter your stops from above list:"))
    #stops=0
    #print("your entered stops is:",k)

        k = st.selectbox('Select stops in path',(' ','zero', 'one', 'two_or_more'))
        #st.write(' Selected Option Is:',k)
        stops=0

        if k=='zero':
            stops=2
        elif k=='one':
            stops=0
        elif k=='two_or_more':
            stops=1
    
        # print("Your stope value is:",stops)
        #print("--------")

    
    with col1:
    #print("'Evening'=2, 'Early_Morning'=1, 'Morning'=4, 'Afternoon'=0, 'Night'=5,'Late_Night'=3")
    #l=str(input("Enetre arrival_time From above list:"))
    #arrival_time=0
    #print("your arrival_time is:",l)

        l = st.selectbox('Select arrival_time',(' ','Evening', 'Early_Morning', 'Morning', 'Afternoon', 'Night','Late_Night'))
       # st.write(' Selected Option Is:',l)
        arrival_time=0

        if l=='Evening':
            arrival_time=2
        elif l=='Early_Morning':
            arrival_time=1
        elif l=='Morning':
            arrival_time=4
        elif l=='Afternoon':
            arrival_time=0
        elif l=='Night':
            arrival_time=5
        elif l=='Late_Night':
            arrival_time=3

        #print("Your arrival_time value is:",arrival_time)
        #print(" --------")

    
    with col2:
    #print("'Economy'=1, 'Business'=0")
    #m=str(input("Enter your class from above list:"))
    #c=0
    #print("your entered class is:",m)

        m = st.selectbox('Select class',(' ','Economy', 'Business'))
        #st.write(' Selected Option Is:',m)
        c=0

        if m=='Economy':
            c=1
        elif m=='Business':
            c=0
    
        #print("Your class value is:",c)
        #print("--------")


    with col3:
    
    #duration=float(input("Enter A duration vlaue:"))
    #print('your entered duration value is:',duration)
    #print("----------")

        duration = st.number_input(label='Enter flight duration ',step=1.,format="%.2f")


   
    with col1:
    
   # days_left=float(input("Enter A days_left vlaue:"))
   # print('your entered days_left value is:',days_left)

        days_left = st.number_input(label='Enter days_left to flight ',step=1.,format="%.2f")

    
    if st.button('Click to check price'):
        price = Flight.predict([[airline,departure_time,stops,arrival_time,c,duration,days_left]])
        st.subheader('Price Of Flight Ticket Is :')
        st.subheader('$'+str(np.round(price[0], 2)))




# US House Price Prediction Page
if (selected == "US Hosue Price Prediction"):
    
    st.markdown("<h2 style='text-align: center; font-family: algerian; color:black;'>US HOUSE PRICE PREDICTION</h2>", unsafe_allow_html=True)

    beds= st.number_input(label='Enter No. of bedrooms ',step=1.,format="%.2f")

    baths= st.number_input(label='Enter No. of bathrooms ',step=1.,format="%.2f")

    size= st.number_input(label='Enter area/size of plot/House in Sqft. ',step=1.,format="%.2f")

    zip_code= st.number_input(label='Enter ZIP code for loction of plot/House ',step=1.,format="%.2f")

    if st.button('Click to check price'):
        price = House.predict([[beds,baths,size,zip_code]])
        st.subheader('Price Of House Is :')
        st.subheader('$'+str(np.round(price[0], 2)))
    