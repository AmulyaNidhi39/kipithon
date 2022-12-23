import streamlit as st
import tableauserverclient as TSC

# streamlit_app.py

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("data:image/jpeg;base64,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");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

def check_password():
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    server_url = 'https://prod-useast-a.online.tableau.com'
    user = 'amulya.s.nidhi@kipi.bi'
    password = 'Kipithon@123'
    site = 'Site21'
    tableau_auth = TSC.TableauAuth(username=user, password=password, site_id=site)
    server = TSC.Server(server_url, use_server_version=True)

    # Get various data.
    # Explore the tableauserverclient library for more options.
    # Uses st.experimental_memo to only rerun when the query changes or after 10 min.
    @st.experimental_memo(ttl=1200)
    def run_query(view_name):
        with server.auth.sign_in(tableau_auth):
            workbooks, pagination_item = server.workbooks.get()
            for w in workbooks:
                if w.name == 'ourworkbook':
                    our_workbook = w
                    break
    # Get views for BHARAT_REFINERY_DASHBOARD_FINAL workbook.
            server.workbooks.populate_views(our_workbook)
            for v in our_workbook.views:
                if view_name == v.name:
                    our_view = v
                    break

        #Get an image for the view.
            server.views.populate_image(our_view)
            view_image = our_view.image
            return view_image
    view_image = run_query('MyDash')
    st.image(view_image, width=800)
