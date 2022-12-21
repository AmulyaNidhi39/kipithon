# streamlit_app.py

import streamlit as st
import tableauserverclient as TSC


# Set up connection.
tableau_auth = TSC.PersonalAccessTokenAuth(
    st.secrets["tableau"]["MyToken"],
    st.secrets["tableau"]["ZpGk5qMJQIytxtHerljfTg==:22aDQjNYtWww9McC5pabyXY1qqGwkcs7"],
    st.secrets["tableau"]["site21"],
)
server = TSC.Server(st.secrets["tableau"]["https://prod-useast-a.online.tableau.com/"], use_server_version=True)


[tableau]
token_name="MyToken"
personal_access_token = "ZpGk5qMJQIytxtHerljfTg==:22aDQjNYtWww9McC5pabyXY1qqGwkcs7"
server_url = "https://prod-useast-a.online.tableau.com/"
site_id = "site21"
