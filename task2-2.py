#function app
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
import azure.functions as function
import os

credential = AzureCliCredential()

subscription_id = os.environ["Azure_Subscription_ID"] 

resource_client = ResourceManagementClient(credential, subscription_id)

RESOURCE_GROUP_NAME = "function-resource-grp"
LOCATION = "eastus"
#resource group
rg_result = resource_client.resource_groups.create_or_update(RESOURCE_GROUP_NAME,
   {
       "location" : LOCATION
   }
)

#storage account
storage_client = StorageManagementClient(credential, subscription_id)

STORAGE_ACCOUNT_NAME = "first-storage-account"

poller = storage_client.storage_accounts.begin_create(RESOURCE_GROUP_NAME, STORAGE_ACCOUNT_NAME, 
  {"location": LOCATION,
   "kind": "StorageV2"
  }
  )

storage_account = poller.result()

#function app
function_client = function(credential, subscription_id)

FUNCTION_APP_NAME = "first-function-app"
poller = function_client.function_apps.create_or_update(RESOURCE_GROUP_NAME, STORAGE_ACCOUNT_NAME, FUNCTION_APP_NAME,
 {
    "location": LOCATION,
   "runtime": ".NET Core",
 "plan": "Consumption",
 "os": "Windows"
 } 
 )

function_app_result = poller.result()
