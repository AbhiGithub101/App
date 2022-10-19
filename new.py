import streamlit as st      #alias name


st.title('BMI Calculator App')
st.write('This App is designed to calculate your BMI.')

name = st.text_input('What is your name : ')
st.write(f'Hi {name}')
weight = st.number_input('Weight',step=1)
height = st.number_input('Height',step=1)

check = st.checkbox('I agree to terms & conditions.')

if(check==True):
    click = st.button('Calculate BMI')

    if(click==True):
        bmi = round(weight / height ** 2 * 10000,2)
        st.title(f'Your BMI : {bmi}')

        if(bmi>=30):
            st.title('You are Obese')
        elif(bmi>=25):
            st.title('You are Overweight')
        elif(bmi>=18):
            st.title('You are Normal Weight')
        else:
            st.title('You are Underweight')
