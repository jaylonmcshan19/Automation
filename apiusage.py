from simple_salesforce import Salesforce

# Define Salesforce credentials
USERNAME = "programmers@thegosolution.com.jaylonm"
PASSWORD = "Violin##19"
SECURITY_TOKEN = "XbAmo2VRTxDx3HpKm6mqHtf1"
CONSUMER_KEY = "3MVG9KshNav2_JdrizuvezzTlzjv11Vy7JV9wX3DUp1ReycdB_ExmcQSUf58SxxTqm.rlnXrTVCFWD.uUlIgE"
CONSUMER_SECRET = "5747F63AE7EE2E7003CCA19F70EB2E56B9E5AF1CDCB5149D8910433C411BAD1B"

# Authenticate with Salesforce
sf = Salesforce(
    username=USERNAME,
    password=PASSWORD,
    security_token=SECURITY_TOKEN,
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    domain='test'  # Change to your Salesforce domain if not using a sandbox
)
# Query objects in Salesforce
objects = sf.describe()['sobjects']

# Iterate through each object
objects_describe = sf.describe()['sobjects']

# Iterate through each object description
for obj in objects:
    object_name = obj['name']
    print("Object:", object_name)
    
    # Query buttons for the object
    buttons = sf.query(f"SELECT Id, QuickAction.Label FROM Object__c WHERE TargetObject.Name = '{object_name}'")
    
    # Extract button names
    button_names = [button['QuickAction']['Label'] for button in buttons['records']]
    
    # Print button names
    print("Buttons:", button_names)