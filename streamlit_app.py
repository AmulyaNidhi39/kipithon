import streamlit as st
import tableauserverclient as TSC

# streamlit_app.py

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("data:image/png;base64,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");
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

