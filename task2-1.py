#logic app
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.logic import LogicManagementClient
import os

credential = AzureCliCredential()

subscription_id = os.environ["Azure_Subscription_ID"] 

resource_client = ResourceManagementClient(credential, subscription_id)

RESOURCE_GROUP_NAME = "logic-resource-grp"
LOCATION = "eastus"
#resource group
rg_result = resource_client.resource_groups.create_or_update(RESOURCE_GROUP_NAME,
   {
       "location" : LOCATION
   }
)

LOGIC_APP_NAME = "first-logic-app"

logic_client = LogicManagementClient(credential, subscription_id, base_url = 'https://management.azure.com')
poller = logic_client.logic_apps.create_or_update(RESOURCE_GROUP_NAME, LOGIC_APP_NAME,
   {
    "location" : LOCATION
   }
)
logic_app_result = poller.result()
