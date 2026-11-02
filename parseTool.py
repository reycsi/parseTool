from requests_html import HTMLSession
session = HTMLSession()
def parse(site, div):
    st = session.get(site)
    return st.html.find(div, first = True).text