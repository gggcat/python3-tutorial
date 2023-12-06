import requests
import msal
import atexit
import os.path

TENANT_ID = os.environ['TENANT_ID']
CLIENT_ID = os.environ['CLIENT_ID']
SHAREPOINT_HOST_NAME = 'yourcompany.sharepoint.com'

AUTHORITY = 'https://login.microsoftonline.com/' + TENANT_ID
#AUTHORITY = 'https://login.live.com'
ENDPOINT = 'https://graph.microsoft.com/v1.0'
#ENDPOINT = 'https://api.onedrive.com/v1.0'

SCOPES = [
    'Files.ReadWrite.All',
    #'Files.ReadWrite'
    #'Sites.ReadWrite.All',
    'User.Read'
    #'User.ReadBasic.All'
]

cache = msal.SerializableTokenCache()

if os.path.exists('token_cache.bin'):
    cache.deserialize(open('token_cache.bin', 'r').read())

atexit.register(lambda: open('token_cache.bin', 'w').write(cache.serialize()) if cache.has_state_changed else None)

app = msal.PublicClientApplication(CLIENT_ID, authority=AUTHORITY, token_cache=cache)

accounts = app.get_accounts()

result = None
if len(accounts) > 0:
    result = app.acquire_token_silent(SCOPES, account=accounts[0])

if result is None:
    flow = app.initiate_device_flow(scopes=SCOPES)
    if 'user_code' not in flow:
        raise Exception('Failed to create device flow')

    print(flow['message'])

    result = app.acquire_token_by_device_flow(flow)

access_token = result['access_token']

if 'access_token' in result:
    result = requests.get(f'{ENDPOINT}/me/drive', headers={'Authorization': 'Bearer ' + result['access_token']})
    #result = requests.get(f'{ENDPOINT}/drive/root:/', headers={'Authorization': 'Bearer ' + result['access_token']})
    #result.raise_for_status()
    print(result.json())

else:
    raise Exception('no access token in result')


#result = requests.get(f'{ENDPOINT}/sites/{site_id}/drive', headers={'Authorization': 'Bearer ' + access_token})
#result = requests.get(f'{ENDPOINT}/drive', headers={'Authorization': 'Bearer ' + access_token})
#print(result)
#drive_info = result.json()
#print(drive_info)
