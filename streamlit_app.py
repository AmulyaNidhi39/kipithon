import streamlit
import tableauserverclient as TSC

tableau_auth = TSC.TableauAuth('amulya.s.nidhi@kipi.bi', 'Kipithon@123', 'Site21')
server = TSC.Server('https://prod-useast-a.online.tableau.com/')

with server.auth.sign_in(tableau_auth):
    all_datasources, pagination_item = server.datasources.get()
    print("\nThere are {} datasources on site: ".format(pagination_item.total_available))
    print([datasource.name for datasource in all_datasources])
