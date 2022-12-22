import streamlit as st
import tableauserverclient as TSC

server_url = 'https://prod-useast-a.online.tableau.com'
user = 'amulya.s.nidhi@kipi.bi'
password = 'Kipithon@123'
site = 'Site21'
tableau_auth = TSC.TableauAuth(username=user, password=password, site_id=site)server = TSC.Server(server_url, use_server_version=True)

# Get various data.
# Explore the tableauserverclient library for more options.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query():
    with server.auth.sign_in(tableau_auth):
        workbooks, pagination_item = server.workbooks.get()
        for w in workbooks:
            if w.name == 'trydashboard':
                our_workbook = w
                break
# Get views for BHARAT_REFINERY_DASHBOARD_FINAL workbook.
        server.workbooks.populate_views(our_workbook)
        for v in our_workbook.views:
            if view_name == v.name:
            our_view = v
            break
st.subheader(":notebook: Workbooks")
st.write("Found the following workbooks:", ", ".join(our_workbook))
    #Get an image for the view.
    #server.views.populate_image(our_view)
    #view_image = our_view.image
    #return view_image
#view_image = run_query("1_Demand_&_Supply')
#st.image(view_image, width=800)
