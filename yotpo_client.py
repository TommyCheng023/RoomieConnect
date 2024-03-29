import requests
import json

with open('yotpo_credential.json') as f:
    keys = json.load(f)

class YotpoClient:
    def __init__(self):
        self.yotpo_app_key = keys['yotpo_api_key']
        self.yotpo_secret_key = keys['yotpo_secret_key']
        self.token = self.get_access_token()

    def get_access_token(self):
        """
            Get the access token from Yotpo.
        """
        url = f"https://api.yotpo.com/oauth/token"
        data = {
            'client_id': self.yotpo_app_key,
            'client_secret': self.yotpo_secret_key,
            'grant_type': 'client_credentials'
        }
        response = requests.post(url, data=data)
        if response.ok:
            return response.json()['access_token']
        else:
            response.raise_for_status()

    def get_reviews(self, product_id, count=10):
        """
            Retrieve reviews for a given product.
        """
        url = f"https://api.yotpo.com/v1/widget/{self.yotpo_app_key}/products/{product_id}/reviews"
        headers = {
            'Authorization': f"Bearer {self.token}"
        }
        params = {
            'count': count
        }

        response = requests.get(url, headers=headers, params=params)
        if response.ok:
            return response.json()
        else:
            response.raise_for_status()