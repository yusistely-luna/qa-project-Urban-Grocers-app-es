import configuration
import requests
import data

# Send a POST request to create a new user
def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json = user_body,
                         headers = data.headers)

# Send a POST request to create a new kit with Authorization param
def post_new_client_kit(kit_body, auth_token):
    current_header = data.headers.copy()
    current_header['Authorization'] = 'Bearer ' + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json = kit_body,
                         headers = current_header)