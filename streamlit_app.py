import streamlit as st
import tableauserverclient as TSC

# streamlit_app.py

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXoAAACFCAMAAABizcPaAAAA81BMVEUAAAD///+y2EL8/Pz5+fmw1kIEBAS530ijo6O02kSv1EGiwkR2dnZUVFTx8fH09PSAgIDq6upIVCE9PT3D61LR0dGHh4dZWVlGVRu95EqryU8xOhbl5eURERFubm6QrTzc3NwfHx8hKAwNDwYuLi6TsTrGxsarzkRkZGRHR0e3t7cqKiqRkZEYGBisrKw6RxaEnjelx0Kz01MRFAZUZSEbIAx0iy5sgis4ODhXaSIoMQ9eciVTYiY4QhoTGASPrDZ6kzFofCtLWxx1ijcyORnQ9luhvkiRqkIfJQ3A4lV+mDEUHgCWtjgmMgYyPww8ShNgdx8uocvYAAAXW0lEQVR4nO1dC0OiTBcWECeG7tGurG20GlGtBawEi6ihflm6vrn//9d8M8NtVNCk9vL28uylGmDAhzPnnDnnzFQqFShQoECBAgUKFChQoECBAgUKFChQoECBAgUKFChQoECBAgUKFChQoECBAgUKFPglaNT052e9W/nTz/HfQ8sygQZ5pfGnH+Q/h3pfkwUARv/70w/yX0O9MwFAAJqddUKj1i2Gwy9Au2NIkgCg+k/WGXfWp1G7VJiBt0WvaykPMhC0T/3Mc9r2WDKt3/hQ7x5PtdnAcsQHWeDNkRe0paiVu6oBBAH6d7/36d4x7jz/XpMeJBnw5mM1bOt47cXzuv5Y4lkeiNVf+jifv379/Bb9fPn65S26+ZWo+5h1JM3i6LEbNPVm9njszJ92Nxg9sDzL8gLs/0JDe3S6v7X14XTnld18+bjd3Gpuf/yb2W/M/AeB10RV8WdhU9uyTZnnRdrWtma2JkMWQxCMX2Zov55eMwRn+99f0c3NTvOEdHPQ3PlrXYKKrn5TlUfnOWroVfuKLAk8K/CT+KyG7pi4jTAPRr/Ozm4xDFfmOK7MMNfn+bv5eMYwuBuOY85eO35S0HpqvUUvg/4ssZqVmmVrDzKPxZsHWj1srrviA4hEXns8fIP7puM7IiyQekT+Vu6hdX7L7EXd7N3erDm7UtrsRneW4zuDt9S5jTvd6yuCJEAi3QILlRo50HYnUIa8QFqh4m7W7c4+hXWCfM0xHOGeY8rM8Ze83J/uhS8QdcSdnK48t255rutVX+60NYZAkiTNewvBx921aq7ji7IkIYEXsGwjo2sT5tuuAWJdI4h2O0NGZqlPXyndxiwgHj6ueQ4moQz9Oc1JfWUfvbi4n92tlf5S1ZRZVlK7L+7dHQsQQnn88ivSUJu16+12bWZ5jsI/SNA0NaRoMPHavT3AH6I3QxLPh+NA0JROVlfPqpl2rFLa2uPKIZiDdXqX45IXVWb2c1L/pUm9Qo67+L6qn0MRICKVl0esRkQlsFL/FWJfOVRExTAMZaoJkgTEn2jkOfcCsq+iMcTvtIFcnamElLwgBMT3axki/+SqguSnqD9CfczD7jrqE8qwst9+E+rLyF6vpp5H1Nde3Pso0LxAecr1cATtkYQ0DIKMRpAQCm1XhaLfwS+0UusbmiRDDY0FKABedJbmWHFPNpQFdpoy08LUJwpnLfV7FPVceSevrqcVDrfbXHkupp7fiHqAfRBWdvJLfcuXWIjB89h8DksVBKSEhsR439UsQ5AB1BQ0FlzfNI1Mv6ZxaPB4aICU0A+h/uVSf8twiYdzvKHnkeDyIOmGO1590w2pr5Q8DSDNALRMQVwPFwhEgaNXyPNArFOfs1GfOYqJBgMLfXKHJ6uDjGjlKWWMVZ48ERAzLCjLlmdD6j+fcBGYk8vcH+3mQ7kcdYOFftUb3FjqS7aJSNOs3N5lw9IEHgORD9BfhTrUtiZTLPEsC8QfpRIZDLh9Zjv1pY8x8zU5cICE8bLYb0h96fRkN2J+tU+4GkfXuyH3B6v9mzzU9yxDnXTy+/V3jwD7MkTkNU1UBhGnlbZnmCD0amAyoe3VXBVo1gL1dx0VhJ4nD3hnyb/clPrSdvPs7OTk5OziMre6wThvXgTd7K8L4mxMPXqqp+5rnPpGx7mfYtxPHLdzmKiKnscDAPFb4SEwkzBORzGBAOe9mIZum/gNEgDNri090RL16+n8eLq9fYrDXq8Lvhxdon4u1weCNpf6NwgKtXVceFCrzw+dtiIRgUfkA2gk7fYDQE3TQ+rOd8ilBMTJZXnke/ZT5lQbS/0GqESa8FXYnPpEBedApbfAUqum6zXyCtqOJmCJ55ENFyd6fEZbwXFLAdqxYLd0x8Ranri5ACqDtEG4gvrKPJYb00+NO04Opt03rZtUpFD/sgvzoWE5h5Fv9NTVDzueoaqGd6jrlgERm5AFQFP73afoUUotBxLhBmak7Wt9FYbKBr8mO93X+pVSf3P+/fuX8C75sUD9HOO/gP7ePRAnbgfDte9V0dQQ14I2VVUT63k0f0LEBw/zRMZHCzmQOH4GgBmkDxsDQ4vsKwuEqZth8FdQf/6Rws5p4IhcJi2XX6MzP+9QJ5YCpq8ut5u3t7fN/dOrm9IS+eeX8SU7X0srsSz1rXpX1/X2L8mCVqrYH9RMEXGuYZ0OAIv0Oy4CQZNq/A4Ml8SLe4ee73Sq1WpfRDSjV2Ia1Rb6mK3D/hQRH4q8oBmzzFtlUF8pfb89pnEdyO9Z0nIWRs/QqdR5F+S0y/3rsxMS1989uWieXi3e9jTp52J7NRkU9fh2tY7V9417FXkfXqdaT72CyGy+MELDkAnTBMS7JxEhHhKBNxWv3sOnPQ36I02ApjgVkf7nBVkzLKLPuw7SNTi2jC8FYOr2Mm+VKfVf5iKazMl2ILcMhQ8R9VdU4x5quWqeHYTXYZQPrrcXXMh9KnixOo5AUV9BHptniBokkVsWItm0rRTylW8a+qMvH1iLSqlrysSHCUhHd8F34onYmyqSYPKJ76q2CMlsCx0V0DuBoyBW1xs8QtTAYn0DZKApq5Lk6dSjGzTLXDTh5Mrlg2j+xMTT0L0ocFkpHZWZeHJ6gJi/4EhwBgcLgv+Zg6157vejC8rcwYfVdFBS37AUjXzeIHyLxVLzlyn+JiOJfchVGtAYBhGEACyhHUsvFFXDfSJKu3Ho2VNeIM4LOobMrqY6xMfvoTeCRUIQRGUyUcRR/2mVmcuifueECg9zezE98blceY76oJlQj7O3dHCZsF/emksFxPEzbgPqu46IfGUc1II8TyJbmAHVXVQtI6xqpVzU90YS5EMLSSRfQMILp4/2rBcYy7Y7VDXUzEfaXIZqP3iAQ18UghCygvV777m22gmgqecShfP1uhxzjFhKJvurqUdfDq5OGIYiPnol5Qta4eehvvvIA+zbyWSYoy/hZ9ecBaVDosb5qG/0NSDLxKiir+g7Uo7wHMmu3sfOCx5vEA0FQvzUDu7edUZkOOJoNeUS6F5mxiZD129RzHPMcZI3pCOXqdSXL5g0oAPX1G03pB6nSuoGEnlB5hEXxmRiKNjZC6cszrwtewX1pdLgUZki5wbZkamqPBrOLBpTjVkfmVCihsDU8H1DlGVNCQP1XU/hg6ch7n2EJ0vhnZSbEKRLfbOcvI4yc3yUnL+GemZB3BPmUecUx5tL/cyHACK1ioZ+0P7D8qcCmV2ChTzsp9dQj3zX7sDzPLfapcIIjc7QJrwL2MoE1VD6o9IPnqVrKzBQ/ngYqqHQV0q6bwJZyQpep1J/dUC4ChtPaGd/HfUR/xzHLWodZjeJdW5IPQumCmb+27xuqfnBzF7+Nhchzk19RU8NV/Sqji1KhHdig+P0V3DTJ1cBQsQ8GpdKO+LFQRpS0Lysu6VQf4MVfdy2t01bi5dQzzHJ1XPNx3E3G1IvBH6euVRs0Q+4l+biDLmpbwwXK5gaNdexJ1OiZiKp1uYmSf8Q9R/yjkYgGCWu/BCbYjklS0KQQv3nRNFjmW/Olcm8kHrm+BrhbEHrHMSzp82pR+RPB8tHPVMgpY4epe4/gbzUGw+mb//Uf7RavfbMs31/opjYh2VjbpHfQyetdB+NxuQgsvm0s2sHnmpGXXgK9c1ywhbt3BCspz5w43e+frk5P709nuc+FvtNFQ6bWcT7U8MxrblAQ27qe4rEyshbNHAtgqoBSQIUryG5wOhF1HdtVZonXqFF4DBI0GdFXZep/z6n6I8XYgAvoZ673Y9Ov7yY0zpnUfumUo9nN05qGKoy4UkhHqXtc1IfTWWF0K9cIJ04U7Jp+EkO3JUAO0d8Pwjv6NiytqxRkOHN0jhL1J/fUpVhzPHHhWlBOvUcQ13DbVHXHF0nvity+iONszH1UFaf04/rWOVA2U8mVnmlvmIJUVopDWgmodoW5Uu1HJk6Oh55gQ9waExxCc+jSZjH0fr00OWSX3+b1IZwzNlSNdpa6hnKmGJ8v6BHxEXYurGuF2DWSprGhBeIOopfeG7qPRnS1CduCxoJ8lj17fmghS6C+DCvDoODbUdEgwZX8AAi8uIwq3hrnvqDqw9JQRQaBNtLU+H11O9ezsUtKpcnlNifha2bUg/l+wyhR5MgrO15kBSb5db1VQiWpF4gGsg07GGkaOp9G/fds0YgJl7pB8TXPWR2cRtP/qLrOpnRhAWFc3oWf4/cyuZyKH0N9VjdLFzx9Tqud0LUh1G0jc2sYGckurGG5rGhTVL+ualv+ZIQx86CqACifaxNhkmcaGAoGi8+IjtsguiMUT/Q5j1P0eRkpCCRt1ak5+elnjveiynkmNuUJMZa6vcWi5Vv9ikjHNXubDqbBZqbIT2VUl1FnxNKibLPTX3pH9scB5FgzCgYj7V7fzh045da9x5FWcYBJGyHSSgfQDUaD4PHqOwmeCWiv7Lafp56ChxzcZRy/lrqd5cu2TmhjEnI88aBhGlmsge5z0jZQ8mIJ+x5qccSag0d37hHMHx72O97epILe7YfVQ0RnsTz0Qsy/VDVtCxkVxN9JQBz0lldkZJFfZqJxVhL/cHSJUdnVEDoNmjbmPpVRd4uxNTfx95zXudSDy55quk4//hE+yWNmaFMIZBxOFoILACp9zbCZFjDQvoHRMYBH1IH6xKYGdTj4rLUEb42crma+sjFyRWvz0JHQ9RTLycv9YNRqoJo1Ku+IuJYNfZ/gvAkkmqBFx0rGGmtgYElPtE1vOqsT5JlUn+cvsDkldQzfy/1FeTgfFqwKI1efTBRVBNiYrG8E9tLEoDayKkG46IxUMywKI0l1R+s6R++oOwwU+Hs3aYu13kl9VHQ/i+kHvnpmmwqzqzWfnr6UW/X9MFPTDvOkbMR7zhBjjNl4sQL2K3cVbHEBzWaJKIsmBPrRUXOi9THLjhXbqbVoeag/ooys3uh6/n2up56OXmlvovcRQBFcaQijHA5CBJhQjsrhMziBmga/U54s39+qoGqCfUQANpk8MLq8kXncpea9e+ncL+W+iUP5/M2NXGI0utv6eE03srDqYl4MSCgwEZqJir4A7wmTgbh1iuNZ1vUcG4+Jl6A6vIa/iwsTqmoqSd3crmscdYnCBfXtn3domezYXnrxn69uc6vl1/v19/dSzAorA8R1CYQ00qKc6A5nbiHgcA32jNbhECIJZ5HEo8mtS+vLV8MJOyHYs+RzOByHfD6yOXxQv/nx5sEEiqVxWq+NbNZJKwmi2ez9qtnsw1bgixLTWeDBAkupwd4e4p7exDyXmkf9rHxFRKXBxFvuBvVli+Fz7biwCVX5q6Xit9fEDS+pYpPKqUvt9Qyufi9ZFCfJtkkhsPL95k7AAUxHMF7fQwH2VkIWTYMJgRFZ1BA81ZWE1V/0A2zk40a8uI1Ia6rxJUJSOK9/222mmKJ+vOLMsX90krutQoHqZztUkAiFt+brTIdj4tozpT6evf5uT33EQLqsyKXlVLDwKEqeZo40vmzVJ7J4iWDEZCwox9NVUH+TDfU4Y1uFQm8EJRVYmWEi6B4cUOJDx59sRhk5yDhqlzeupkXxZdUJJwkhbBft3YZKqx5Fh1Ip77R7St4MYdDbU0QBo1hptiH8fpE37wihtOo+iJPAjSkGAdqU2XiVPVuJAwNveqoeO0yfi+BpkGjAohOtb35+qGUOpzmXjlajM+V9/bnlcCLKhLOri9x/KdytX29m2gbLlH16dS33Ckk3jM0nTgJF+dmM8Q+EHpgDl6dpSKo685komAYk4nt6jWqoLlddaaId0GAuEwqVPEynPprYwapSMnN3lyUI16YpQXkL0qLc+Wzi+aHD1vHJ3NGgFohm0q9hVP7xJ0DWsJzSD0E6f5lH78tOFftkrcioXKHlfldu13DaNfrVBinPXCde5MsDkd8m4oi4rgCDuQ7ej3ndgUpa6muYnXPLRRAvbQOB2H34GBO1+ALT2LLkUZ99z72GHghKeGK0uIsUFPiIp4GkLoFkC6Cyl0M0usP05q7rucoeFl4UHTMasagVqtOBEk2/UE7u4p7DVIL/z7uUqY2UdAYa6mPyoujymNa6ONseSr1LqmpCbNywI9ODROEuGwaV4MkK4bwd4h5Hmt6g57I5K/D8ceOPmcte7rl2iqmHT9YML+CQ+LptB3Ft+5esawlvebytpz4LGXmmur/pdVnzFL1GUcXXaZR7wWVTsEkBhhRtUtQfWbiIj9Z/Dk3V+z62K8kmp6mID/1DtLcE3s47Huu1x8Oh75B0c6HW1EY4dztrnb3qj130qn/Hqt7orlvkw+2XupP5l9DwjytudKox1qbjVJzSbluGD6rKngNgWb0q+EIb1u4+hSv3HuzmsuKhSv1eIirXdE/yAdckzqFUCQg1KqvWxuW3C290vjognLH6Uja+vDZKVNe5J5MjQ/odf2pUg+jZQX4y5zUIzNar6m4qprVpoY/xAKpYGcDb8gkg4XtV/KXu9ZEAOM6hCg/G8sDuhcEkvmKvRfmkLWg53SP5n4vjiispf4Ed0jVr0Unn80tmUqlfizwcQWGHK8IDqW+XdJFCQk+Hvtkz45ACtEhuLgGPj/1PUWCC6U4kQbEM1tiWJNM95NrpJrlFyJrU5bP14nKwbGXSFkwlP3NCBp/2T9jyhzt2pSRnp/3URPqmZj6mhFEqjBxcrJvUhKv131kVCErRGoAT2iArLqLXnV+6iuezMYWhwrj4BmULElw4lWpJSydb7QTvPnN0neBqmB1v1eOwZyFKoeJG/cy4/WfP94iDRMuusIXI3oXAnH7ST8Hsd9Tncp4pR76nOgjxRaM7AIVqP47y5TkQOaDmT6QNHt5G/8R0si8nGtKVfclmUxUqeAZct8lRLtqe4OoxDzYCK8vC7Ka5y5RJ9e0ZqBS4Ve7czrjJHAx6aZmZqrk+we617Pm5WLk/0NytBzPs3pVFVdtIfEyvUSSO98eZPlhRFIljcO+Csg5QYGXaA9S3Opv6Ij0kFKW/ALU+yYmH5Kgcci6IPp9d9DtBR82QsMzcfX8a1TOzjYF2oW/pA9sfwimQ1TL/lF2lqpytL3d3Lq+vr5t7m/vLO+meLQfd0Mvqu16zkQxbO+Qspv1Dr3jX6NreY6hqNN7dJqrp87gOy6Cl7qkdj0aumsEe289oH9ottq3Bjo1ra37oxHeVLGDFzMizTjKd5u3QVaC8Ob8+9HR+ZfNHLFWvb12GXivXut2a79mtThG27Is/PbQl8FsLi7WswySlzJHIzOc+mUuGvkdWJeb/VehkhkXaFnKSDSDhQxCUHePHX5ZybrgN+BdUV+6S1kDXao7KqKdXVzogIh/GBdS/1Zo+d9G1o/4x0Z74E8/4ZzU0lIHQX6QjMHhn/xdAe+L+lLtk6yZ3yIEG1mCcLoR/Y+/kYBhHb7VzDYn3hn1uMqergiJggkA7zcaC7w07ut/mPfS+6P+TpWXFziAsTEYeKKMZ1uId7uq547TvyHeG/UlHScBknAC8SFVXI7Q6tpAGqvuYfp84vfj3VHf8gGgRR6nC0K3p+4hPfP3/Nqvd0c93sIvWdFDFphEcdRK6412xX8bvD/qS23PHI9BsAeUMB6Pjb9EwSziHVKPf5vgzLONe2XiuHq3OxcPqk8+bbTp5i9EQD21Adc7QeuuXq8/9eY1e8/TeAFm/gLI3wxEPRUhXl7G9u/EUjCHlDKWqprM84L4lyggRP1enPng3ovU91yv3bvrtVq9Xq896ES5eLyHLi9of81vefz8Mdl5dN0vmvnXoDYStGCrUQiANCKF810FBEtMXpGcemNUUr/9d6PS/injbBVOWeHFaaLv3ENcjUV2G/xbtP07Rd0AeIvuYFfFYHkDph0X3IM/mpz6D6Bum2SdSZgeJ3UJMsCVQO6fD529c7SqmpSsckC0Q3HiDOq93t8TS3i3qMxGQeSY1Uz10XfcWqtV0P6b0O73f/50frrV53qv1Sho/51oBHg3ntu/EAX3BQoUKFCgQIECBQoUKFCgQIECBQoU+A34P/sfsd1b61bRAAAAAElFTkSuQmCC");
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

