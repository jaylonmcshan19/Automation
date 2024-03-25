
from datetime import datetime
from flask import Flask, request, redirect, url_for
import requests
from simple_salesforce import Salesforce
# Define your Salesforce credentials
USERNAME = "jaylon.mcshan@thegosolution.com"
PASSWORD = "Violin##19"
SECURITY_TOKEN = "XbAmo2VRTxDx3HpKm6mqHtf1"
CONSUMER_KEY = "3MVG9KsVczVNcM8yQQIoTGjDxF_EUO1sPlgFDIrwAxyZCSqRt0WTtliVfkvCtSsVIPtU0Uy1NEBop5oxvjYeN"
CONSUMER_SECRET = "2AACFB7BCAE1265ECFDFCF4087B58556D5286511578AC14A1DE0FC872BA47169"

# Initialize Salesforce instance
sf = Salesforce(username=USERNAME, 
                password=PASSWORD, 
                security_token=SECURITY_TOKEN, 
                consumer_key=CONSUMER_KEY,
                consumer_secret=CONSUMER_SECRET)

# Query some data from Salesforce (example query)
accounts = sf.query("SELECT ID, Name FROM Account LIMIT 5")

# Print out the queried data
for account in accounts['records']:
    print("Account Name:", account["Name"])
