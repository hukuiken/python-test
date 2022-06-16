# coding: UTF-8
import requests
import lxml.html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

D_path = r"C:\chromedriver_win32\chromedriver.exe"
B_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

def get_lxml_html(url, proxy, tmp_header):
    r = requests.get(url)
    html = lxml.html.fromstring(r.content)
    return html

def chrome_webdriver_get_html(url):
    #JavaScriptで書かれている?のでSeleniumでテキストを抜き出す必要がある(Beautiful Soupでは抜き出せない)
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.binary_location = B_path#r'C:UsersSugataAppDataLocalGoogleChrome SxSApplicationchrome.exe'
    driver = webdriver.Chrome(options=options, executable_path=D_path)
    
    print("driver_get_start")
    driver.get(url)
    print("driver_get_end")
    
    print("portURL_get_start")

    return (lxml.html.fromstring(driver.page_source))
    #return html  


def main(): 
    url = "https://www.nicosuma.com/market-price/iphone"
    print(chrome_webdriver_get_html(url))
    
if __name__ == '__main__':
    main()