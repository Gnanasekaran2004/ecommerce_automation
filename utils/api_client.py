import requests

class APIClient:
    BASE_URL = "https://automationexercise.com/api"

    @staticmethod
    def check_api_health():
        """Simple helper to verify API is up"""
        try:
            response = requests.get(f"{APIClient.BASE_URL}/productsList")
            return response.status_code == 200
        except:
            return False
