import streamlit as st
import tableauserverclient as TSC
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
    username= user1
    if st.session_state["username"] == user1:
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
    elif st.session_state["username"] == user2:
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
        view_image = run_query('newdash')
        st.image(view_image, width=800)
    else:
        st.print("zz")

