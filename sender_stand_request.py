import configuration
import requests
import data


def post_new_user():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=data.user_body,
                         headers=data.headers_user)


def post_new_client_kit(body):
    if data.AUTH_TOKEN == "":
        response = post_new_user()
        data.AUTH_TOKEN = response.json()['authToken']
    headers_kits = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + data.AUTH_TOKEN
    }
    return requests.post(configuration.URL_SERVICE + configuration.MAIN_KITS,
                         json=body,
                         headers=headers_kits)
