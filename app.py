import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from twilio.rest import Client
from dotenv import load_dotenv


load_dotenv()

chrome_driver_path = r"C:\Users\user\OneDrive\Desktop\chromedriver.exe"
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option)
def getP2PRate():
    driver.get('https://p2p.binance.com/en/trade/sell/USDT?fiat=NGN&payment=BANK')

    cookie_accept = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    cookie_accept.click()

    rate = driver.find_element(By.CLASS_NAME, "css-onyc9z")
    result = int(float(rate.text))
    account_sid = os.getenv("ACCOUNT_SID")
    auth_token = os.getenv("AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+17855723587',
        body=f"Binance P2P Rate for BTC to Naira: {result} NGN",
        to='+48517071489'
    )
    return result, message.sid


getP2PRate()

driver.quit()