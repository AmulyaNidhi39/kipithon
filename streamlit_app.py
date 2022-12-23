import streamlit as st
import tableauserverclient as TSC

# streamlit_app.py

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASIAAACuCAMAAAClZfCTAAABsFBMVEX///8AADz///3//v8AAD0AATr///sAADQAADgAAC4AADf9//80M1b3+P77+/+NjZ4AACcAACNNTGkrLEpTVHPu7vhOTmUAADIAAD8WvPoAACoAAC84eOk0NVQAAB+6vMj1//9ZPNxcNts3fuoAABcAACE8dOdCZuZXQd0Yt/g4e+lHXeVSSd/v//8bsPUcrvpBQWNAauZNVOFQTd8AwPvQ9PcgqPUho/jg9/0omvAqk+/Z7voAABUif+XKzNc7ceozXNSPpNzEzuzT2/xGNsbC8v6W3/J/2fBpyu1Au+R3z/Gk6PkvtOVEsd3J8/sAq+is3/R7yO4Ln+KZ2PY/rOMSneVeXm56e42ko6xgteM6OlKVlqem1e6BxO5QpePZ2eUdG0cfleKSxeomlPZvboSiyed/teYoh9zA4PouhN5yp+JOj9xmoelkmdCexPQddthhkN+tyfEWYchVhNkhIkt/nePM3PtlhstiesqJqOdZedamuvJdcdluiuIqTslGX8ySlNCTlt54dtFaWcrIy/CpqdNwatRJPMHHwPOzrOdgU8/W0vbp5fuYjuFQHtZDBsgXgtDqAAAWmklEQVR4nO2djV8Tx9bHJ7PZJWRNSNSYNCAEkBeBoCEFUiOvRW/b2wpaFRQroqiAXMFLa6tYFeGCKPb5l59zzsxuNpvwUssqn4/zK+Zls5vsfHPmzDlnZlPGlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlA6HOGcmlw8Y0z7z2RxKIRmTaZpmmowQmZ/7jA6XTG4iHgQFj8iOlIrFAQ+g0TQgBA85EfvcJ3XoxA3DAGsiRnDLFaJiYecywHQAj8YNU/W1UgETMCEzlQalUkz4pM99Up9bYCYOQ9F46sLFf333Pem7Hy7+O2fY/QxCAdP8MnmBmWhWyzWe/vFrW199/ePFwmtfbp8jx2M1n5vdiEYKHv7ANEPuCJESDHJfoPNGE3L0HvPS6a9sff3V6e9Tti8yYUfA+VnO8rPK0MKOYUtjY6cdjL46/WOa21DAk2vmF9jbDA7NtjGY7F+nC4zg0Wi37a81g4fDdrf7gqSl0tB42yWb33eetgWMRi8UTIxrEAd8SVYEaQaO46mLP12CcBEcjYEGcmm0E8h0dlqIOr9LoY0ZGtpa+ofvu7FraiWxEsdkt+CmioMDTkG6GBEh7qLH+Kdx9rHjJEQqrvjDi6/OpNg5931n5+hYyoD+hsl9+qfTyEcgwtsznf82gR/0RoN1/wT7wlMOdF3nx0XiwiUNV3ucsRc4NHyC+R90cvHi3xccSxGdONr6d9BCu2DdP3aegXZ/l8aRTUCQOiP/nR79OUUEzAtXgdrp0YsAKOw6oYKVoMgcC0wQiCZtieNrXOygffTgaNCbF4YRryI26C7s0lUEBCiuXsyncxd+GJVcJKXTgtWPY7lcbuzyNXp25srllFb6ncFZayLt5ZKAtYtMhEWz4Msn+6Fc2Y123yKrNLik7h0iSL4ujJ45Q0TO9PSMjtqW03PlypXRUbjp6cGXz3T2wPYeoCOeXbucKgmPYLTbaahDQtgHXVv/2chYDMUzK0Ib6kG7QER4cwZI9fRcufHz2KXu7lx394WfL1+91tNjm5XA2Yl2ZLhaCIjYCVvXQ2AsdsBOiFjohFMxFr5uPxn/u6cO7xy6aR8+Ib3/wYt3X+2RVNBaxKOrly+kTcty4ZtOdY/dIGNCiD09yBIeXvvZNaKR70xWVARJ8WMh8P4FRPh66GYyGIjHxQ6n6pgROlIdDAQr4sFA5PjfPXUw4VBtRUUcPy8erRIfc5CMOFWDtPQNQtMj2ODNtRtjwIeJqr5Je8JN6tIPV3rkLmJXYDQGp4RVEwsDQo37fH6SjogKHweoObse0X0gf8IX0Gsn4YDwkYCe8PsSvkT8byOCw0MRXff54QP1ZBU7cBuC5mgQLF6+Rg3v7ZHqvT2WLn+AmZP7Wvv39ly5hHhMZiOCm0qCAAJEjlPm6Lcma3X5qq5HZ/AwQuSDP1/FRyBioSgQ8vsAMSDiB+2NwE/D361veqm1vXjX29M7fTe9Y4nR4JduX8N9xf54fztNoVsRIl9ZRDC6s/5TPptQxVkMWg8MUcILRCYiYreme6itktLtC2zHUMUERulfpnslHrpFRAWXvRsieG0qbhGCF+/EKBQ/5Ig4FjZ+mZYmAZq+mhPBatmiIqQn3Ejdmu69Jk2ot/da3sTwx0oCdkMErvpOIGH1M19tP2QwB4HI52FHM9GMNJa+DV2t9xu6uZHG/GOnKjX6d7CZMSD0jThi+hb64ML+uyEy2VEwIl12s/MwmGkH0tEQEb6rF4hooAJOl6a/kbpBRSHDnRna54OuGWLxMTwAGX3zC04icZoLELvs5ovGmxLWC75IFRgwF4jiFTDo68Fg5UchqoURvwLDjKgniDhl3Obdc4LQ7TQXQ/MOxXuTgn1o2S15wHSOBnVzD3cNAOFvIhrAL9vv0/2J5HHp7DQWPn7W0ozjvHaaH3efWuiIdfSRCXHwx/PYUdzMQWvPnYMG7zERhIk9DN2wzy9E6Nxdxksz/TKIkHx/bYAQ6dDL9Dsh6wDD0KTCjvmDcnUCJksFhiOLgXQnLOrEJk0aM28QwQffRkIPZ/cwVDg58EQ476ilbp+DI87lDXexphwirK+wWFIP6H7hh/RIzGoJ9tySVmmcSjLFGxEMVlnwvvCSpsnlKzTf4FWOZhocG3zuATR39+kx2JNTSY0Z+YdwxMM8d2WhZRHhmBC6GYQQGLclAnq038r3KeC2v/xCTcCq/hSFVZRwEDlrM52Kw+C8Q8QWzp27N52jOcRdP8TM5UzNwDgZ/Bco73YYZRFpEBXMJH1icIbhGfIOGywgjtmyep8ZipVRWHyAptkFFVrb4zzcM0Q8DSZx7z7OanB35l7UfvPBw4f3setDy9IP7+ExrmJIeUQaq6oNWPFQMDJT1JTwsUhlZTKZrEzWWiOadjRaGYkkxeZKvMN/8TtHq+pCzPktYqZ/XuxTWVlb5V2mz+/P3bv3KCX8TJlPsDfNwn4P8+AK0BvcxYPSrvLPDoN+3Xk/eCABKX4Tv3sLkmaETwb8AUxF9WQBUSARCFgRgi29InkqPj6FnVOzPy6c1GkA0PXKKirZHYwlYXLGcAgwsPzMc4/u3Zt7jLkod3ccA/1PanY2zVL5+/NzfefuzeVlfSP3EI66i/OTJq1EKoPId4zqRWwKelkAk3tI6YN3YpisFRoSPkJthGQ/XkAUhGAwgZ4djiJBqAAP/f5AZWQmBkEn9jjyg6GklfRVUlx0EHyYmHPAsQGnDCG6Xug71zeXK7unhnMi83190/Nzi3Nz84/6+uZTFsUHfffu9c3iFCX0zrJxUZDqRSx2rDqB8a+eSOiByJRV2LcRlUTX2tEKkctB2BwIyFEwQch0PZCsrqP4jMorLBShUQBUeZChIxgQIcKH6dlH2NSFVHlEYFr5ub6+ub6Fu/k0y92aTdneJ4+b5x7kU7ROqxyiAHQ02HI0qaMFQQP9vlN1zOXvdkakowUhWL8VLODGgN93foIJG0JfZCHSDxoRA7eTn73/4D9gGNjUx+XfG4ffS7DD4hgTxUez4AfSdGjf3H/mH88CJxEhlvgig41HIHcFRtDJEpFxJMT3Z0UUI+iCgJ8IYY+DHqifmqDZIXQLHlkR9GPwIOlHjaA+oXz5kQy+8Nm5ubnFB2mOM5C5R/MpKwbm2AFB+A6Ni3exT7oRYUdjk9GEPxBAgwCPesKa0tkVkWkhgl6G4Saaj59MSWYwvtop0Q4PEWFkkxeta8RWPswVwi/nnpr5ZPHhbC4PfCD/zz9q7Fso7PmE+OBfY+O86G2m24pYf5JMAXytHoifDDvd+l6IkEuytjYSjdZGk5XVQR08UzCIJV1fxcmwPFWPEME3DhFgvk0AwtsFU7MjVueOqfnFJawIYdP57BziWMpZnGelCaIxLphlEYVDkMNjB4FmBAPVMBYZ7vmuXdx1wh+d7O/vn+rvr5uomrlzPok0dCLeNIEu2/TMFzEczdlsTaOtZ1TFhu6Xnl98lGJimpCz3NLiQsrEGUUO4+xCG+7a9kC+Bc8vNvZZb7CUwjPmbl8UuxmgLkOdpLYO38fdhvKI/KJLNdU5doxNxOPU5QBSMBDGFc8eWhFGxU8KiNoeY6gClsVXatraFnKpFLT36ZPZ5ZrHWN7GpNIsRZRbpOd0sywQseK46MjxaECmHT5fcrLsueyMCNxQtIAIs93Y2bhPWlJ0QqRrHnY0zh4DDaHGmicMGcDfb21tNY2LywtDj5+1NdfMzTqPWappxL1tRKllgCzeoWYZ142UINKrfXowIcLkwFkqiZcUxfeNCC17Ssd9kXrgiAvRAXc0qiA8bpaMatqa78NYrKHHeTIw0PxsZWnxv/9tbqypmYd9Z5+QhhlbqoFda2qciPBg/FfzPIdhNHf5ol/v6ImgT2YSEXQfpS3YLyLsohBBVKK3hqE/EY0RI6+siJwyIBJqRkRUUgR0s0P3TYool2uaB1bgQ1cyA6hlky01A6DmZgsRSy1b71BT8zzNCFAxopv9kYQvaGUItf3lWrBPRHJdyVQUEGFAqUfES14hosrh44ECoieYrBmmWKZhGjgzn19uW4ppBlsZGAAuA8tgRc01zS5EzRJS8/MQjWeaK7o2J+ypRRCkZ6WZ+H6tiMI5FopDngZ5iR6oHi+Oiw48ugYUTzLNUjXNzyBfxWKZQRd8wCMYwFL5FFbYVgYQjLAi0pD1NrlFOhY18DxsmCWIII1lM0nLXYNnOvFPEMHXB6d9DKIjfMMAJL0exkXYGJMNZwawcfg38BuOZ7jwBVwSF/mbJiqMgKgZ/NPAc7CiAdx1wEJk5OEJvQhv8SeWa93RNeZooZMVCYiLwH9ACoIrE8jaHKXV3XK0IkRi3d/xChrREr74WZpj8g4RvNuUcDLQyAy0kKiEIQgyU6kUEsRpECx7SF/0nPElQWTIOuOniBc2ZTLAWFyMZboRMTaVTGDqqVO7zlNoxIqLIRKRvyS6dnU00kzcL/KQ4JFwkRUdcEeD79swtjPYYBAweBHCciuL/b60tLz8+x/bXMwHYZy30tIsELElgpWxO9pKBkTUBjLPmCj5uRMQDetpPoBAeRY42SkamzSjFFFpAlIOUZV8d7/+K9VxvRvRwNRTf7S0YBvBCjKvZg1cJpNvxi2ZwadWBQi+8ZUWhJgBRH/i3hkLETd/I0KZTEumZfCx9DElvghT/WgCK2bIzB9Ewyqqhuy7owmNV8pSks9TRGgjECvmnz4Z+v3FYKZlINOyguEki2UyAhGPPRXS2Eo7bZOIAIhlRaHn9HTwj99Whp+GuDVj5iqGgL2aR+PQyWikhmR/hhUqcB+BaEaunPDYivC8NblCJjX8AhH9CZ3PNGIZYUXf8uGXg6QwWBGRQEQt+LKN6Gk7AnqWp7xXZsEliBimg1NxkeoTiiYxVb1vRK5S8dGgLCV564toaDAwGzBgqMYO1zKYx1ws/wp7TcvgUzY82IJ6hYhacBshokdD8j2G8LBhEytkvPzKEHTXtECnrikRQGdEuQgWHtmuvmg3K/pV94u8OH7U02KIQzhuvmhpaV/BqxvyAkwB0aAJHY0evUBE7QIRZpRGCPdYcS3kLTsDAu6oqhZLG6Jo6KucYqK6QnvvhUgWmHChAdbBq7FqhIigx5reVR3dWgcKr0wjpcVeAayW9peA6KVAFJaI2hFRO706hMan0fbnKW0f82gmmOr1Slk7hLv4zbBjIcmeiKwvgSq6dU0+TNJwbJykiwi9qxc5ZDI0iPb/oUWtIJn29m/ZsAADVjTUjlyKEGHHCg22t7evcK34lMojApOJ3amgyS5soB69bu+/NyLHhSNgjterfej2sTbbz7wshhRLY8+huYMxDFb+RCAvEREJrGhIPCJEyK39NU3OILn2p4a5nzl9LHv3N+E8mK77IcfSwWUb1tUP+/BFYqUIRP+sLorhA82EVDP+6RABmC6AsIp9O/YKHhUQvQREXQ5EoK5hMCJjG43o5Xa5y2RKEdGs/uQprGHodjXRkNHRnh1NdGVaUdlfISdG/P7kOK0v/TQdDeKhF9T4dTzt2NqOiN7gfXaICgX0uGuKafuwIjnpdT2KfcRHYWQwHmMliOIliPzOES1Wdz0SRC9E731+iqrLn8pdx15ie9u7YtiDYmtdLyEu6ipC1NWFiOBR16oZhvau0svZLZzP3hMRftlAKXyk2u+j3gaY4ic1ZuzZ0fzJyakprO5PVs3cORWN+zFo0Gnt5ziZpteIsD5O1wGvAJ4u+PcihDlm7MUIIMriNkS0le1CEaKulyvU4PUsUuvqehUTVmSf2K5rHadoVlYqcp2J+vxuE9Y+PRmNRJqaopFktajM6dhbwZ/FY/IHOjzuaDQ7ZrDtd11C2Td0GV7o9ToTiLq6bEQbgKhj41sKZta7LK0ycX2eTX0XRBq5I6vA5m+aFFPXuyPSxUS1bi0sSWA/DernJ6zg0+OOhojAkDaydpPfhHHFBbRmPSs2AqIOG9Frk2EvW39nH5B9Kyeg94EIjpyJWOU18CmyTrsrIpruKJQt6doRnS6NMOTVzF77Iqw0slVoMLUZ7zewaA6Wsf0m25HtymYtRK1rzIjRGmv2dtMiBDtsbssrW/eDiIdvVsv5EF8gEKyI7e6LbCqF7glDWSCYSB4PMytW8raj4awO2EtrlgQtBhjZtWGGSyKY9u3WRrZ1BBC1drSOrK2u4+cD0NCq2JmAgjawJKTtB5G4wkGX37meSMRv7gORWFxUEGw/NRPm9morj62I5kbfjmQ7OrIFbb425VyGGd5e19jw/9bfx0wZ/7PtNTQu2L9DWFnHRljj+0SEo3Tdedsc/P4IXqO3lxU5F6tBH4tHkxhTyQVY3iMysZe8JkIdHdRwuO1YW8cBWSMmXF65qtEQG1sdEftlrTvoaNxxkTCdYUResYeX7DlOGSu3WF+TLwYrggHwurh6P6gH8K+yFFEiEAzI3QPBeGUkEj87GRLrAGV0HmoK6mKHiHdxUXijFZssAOGDjpGNt1gblBPwnMkIZnv1XavYLytxZkfeuqBjSHDs5JGTQidChnt2MXzipEO/TsGGY3L3Y9bqfSsughG+8F4nzx6fmayLFb4J8SD0q7XDsUnnKwer7XcdREbc4G1r69rqe41Wylmfuf12Y7NeIrTVuuWe80Fro1+moav9MWtwX19smlpBYXRkYXtbMSLIeKN19u5hR6rjiDJo7b79fl4F13x709lseVe/ubH1dpsWNL/f+vBupL7V+WorEm1dZe6FHpyW+NvPDO76Yt1T+hqlanIpuv3rPxKRX8dM33pjvLq9ZAEXK1rt49VV6NCM95uy+a2t9SPZbGs9IID/6utHRkY24V9rA25BMNkOekSo6j8wo2QVAzXR+eMC7tPmlugZVgGsFUd2YcXuaDgrba8fLtN63FaYK9jpypEDkGYa324CEdS7re1Q6P3qCD0hKnRPrzasvd0Oxd6/qRcbGz6w0oXstEjT+TM+e/yQH/0ah/uyCguRz2FFZSWLSI5n3ggnqGEwb4BW138Ii0+KbTSADbUWSbhmePH9O9x3ZIuWZLpOi0ZBzpyW4kIkXzEce9AKN4cJWMtBRUezXhPHlG2C82hPOGGQwUIbDQ0Aga7TwdnztXrsbgIT3EKfW6e1LziXtL0BT9+LHKDMGdn+CZNkZq9LK3vu+PWUXFVR5It2/0ER7nZ23pkSnNfW2nZhARDfbqgvCCg1vLH9InBa3dj27kzKlfcPhWhMcVjyhpNRfX3D+8LQobm/ugPWoUXEnbV6g201oDuyCY3EDHts0aiO7J0OLyLha8Uzk7/9q8GpzUJYxouuvfRAhxURXjpZ6Gcme1+M6J3z0jN+cJfslJN5WBHhAOX4Rb7teiehvz4ULpWj0ffjf7pqbx1aRBT12ZdUGrGRv0CCz19//d9WYSzHvKvc2tcDk3Y2Ga+uro7Hq8/vHjp+VplGGDKzjbV3m5ub7zY+QLZmfLpfKjYnxquExqeYl+PCP5LGDVdE5p6b/lQncpg6WpE4XbGGCRRdG0+/cfDJTpaWQlJtwzjE/+sIg373jHFRxqEan5fDvOvD6ZcMMK44zD+rjckV00T0g8MXLTf+dB/OxVpU0zR3uyr+88pKMaizySuXP5kVCf9jGjtm9odCNJdsMhlN0hrsT3a6XF7mrtF5HFpfpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKS0s/4fEZiJE/zoZvoAAAAASUVORK5CYII=");
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
