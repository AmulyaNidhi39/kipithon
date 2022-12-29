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
            #del st.session_state["username"]
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
    if st.session_state["username"] == 'user1':
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
    elif st.session_state["username"] == 'user2':
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

