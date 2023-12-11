import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

url = 'https://de.wikipedia.org/wiki/Extensible_Markup_Language'

html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')

value = soup.css.select_one(".mw-page-title-main").text

toast = ToastNotifier()

toast.show_toast(
    "site-checker",
    "value = " + value,
    duration = 5,
    icon_path = "at.ico",
    threaded = True,
)