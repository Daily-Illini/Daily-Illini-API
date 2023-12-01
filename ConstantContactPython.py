#vbSamEjMSHKM4q-f3mGeuw

import requests
import json
from urllib.parse import urlencode
import base64
import webbrowser

def get_authorization_code(client_id, redirect_uri, scope, client_secret):
    authorization_url = "https://authz.constantcontact.com/oauth2/default/v1/authorize"
    redirect_uri = redirect_uri  # This should match the redirect URI you provided when registering your application
    state = "state"  # A unique string to prevent CSRF attacks

    # Construct the authorization URL
    params = {
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "scope": scope,
        "response_type": "code",
        "state": state
    }
    authorization_url += "?" + urlencode(params)
    print(authorization_url)
    oauth = requests.get(authorization_url)
    webbrowser.open(oauth.url)
    auth_code = input("code ")
    get_access_token(redirect_uri, client_id, client_secret, auth_code)

def get_access_token(redirect_uri, client_id, client_secret, auth_code):
    base_url = "https://authz.constantcontact.com/oauth2/default/v1/token"
    to_b64 = client_id + ":" + client_secret
    auth_headers = {
        "Accept": "application/json",
        "Content-type": "application/x-www-form-urlencoded",
        "Authorization": "Basic " + base64.b64encode(bytes(to_b64, 'utf-8')).decode('utf-8'),
        "create_source": "Account"
    }
    params = {
        "code": auth_code,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code"
    }
    request_uri =  base_url + "?" + urlencode(params)
    print(request_uri)
    a = requests.post(request_uri, headers=auth_headers)
    create_contact(client_id, a.json()["access_token"], email, first_name, last_name)
    
def create_contact(api_key, access_token, email, first_name, last_name):
    base_url = "https://api.cc.email/v3"
    endpoint = "/contacts/sign_up_form"
    url = base_url + endpoint

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
    }
    data = {
        "first_name": first_name,
        "last_name": last_name,
        "create_source": "Account",
        "email_address": email,
        "list_memberships": ["c69be490-79c8-11ee-9cf7-fa163e1ce73c"],
        "custom_field": [{
            "custom_field_id":"0e80cf38-8f76-11ee-a641-fa163e6eddcc",
            "value": "weekly"
        }]
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.json())

    if response.status_code == 201:
        print("Contact created successfully!")
    else:
        print(f"Failed to create contact. Status code: {response.status_code}")
        print(response.text)

# Replace with your own values
client_id = "d0d8d364-b7b6-497a-a8e7-6e89ac0c754d"
client_secret = "A5sErJbUHdPu6pAHxo7x0w"
email = "sent@sent.com"
first_name = "week"
last_name = "weekly"
redirect_uri = "https://cavemanfury.github.io/"
scope = "contact_data offline_access"

get_authorization_code(client_id, redirect_uri, scope, client_secret)