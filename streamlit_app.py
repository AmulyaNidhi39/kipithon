import streamlit as st
import tableauserverclient as TSC
pip install streamlit-authenticator
import streamlit_authenticator as stauth

# streamlit_app.py

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTxAwB-Fkws1pXkUh6onwVeI8h-BnEnGXyTlA&usqp=CAU");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

usernames = ['jsmith','rbriggs']
passwords = ['123','456']
hashed_passwords = stauth.hasher(passwords).generate()
authenticator = stauth.authenticate(names,usernames,hashed_passwords,'cookie_name', 'signature_key',cookie_expiry_days=30)
name, authentication_status = authenticator.login('Login','sidebar')
if authentication_status:
    st.write(‘Welcome *%s*’ % (name))
 # your application
elif authentication_status == False:
    st.error(‘Username/password is incorrect’)
elif authentication_status == None:
    st.warning(‘Please enter your username and password’)
