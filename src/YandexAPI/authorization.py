import requests
if __name__ == "__main__":
    import os
    import sys
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    sys.path.insert(0, root_path)
from src import utils

class YandexAuth:
    """
   A class used to handle Yandex OAuth authorization.

   ...

   Attributes
   ----------
   client_id : str
       The client ID for the application.
   client_secret : str
       The client secret for the application.
   auth_url : str
       The URL for the authorization endpoint.
   token_url : str
       The URL for the token endpoint.
   access_token : str
       The access token obtained after authorization.

   Methods
   -------
   get_auth_code()
       Prints the authorization URL and prompts the user to enter the authorization code.
   get_access_token(auth_code)
       Requests an access token using the provided authorization code.
   get_headers()
       Returns the headers for making authenticated requests.
   """
    def __init__(self, client_data_path = "configs/yandex_app.yml"):
        """
        Initialize the YandexAuth class.
        Parameters
        ----------
        client_data_path : str, optional
            The path to the client data file. Defaults to "configs/yandex_app.yml".
        """
        client_id, client_secret = self.__get_client(client_data_path)
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__auth_url = "https://oauth.yandex.ru/authorize"
        self.__token_url = "https://oauth.yandex.ru/token"
        self.__access_token = None

    def get_auth_code(self):
        """
        Prints the authorization URL and prompts the user to enter the authorization code.

        Returns
        -------
        str
            The authorization code entered by the user.
        """
        print(f"Go to the following link for authorization:")
        print(f"{self.__auth_url}?response_type=code&client_id={self.__client_id}")
        return input("Enter the authorization code: ")
    
    def get_auth_url(self):
        """
        Returns the authorization URL.
        Returns
        -------
        str
            The authorization URL.
        """
        return f"{self.__auth_url}?response_type=code&client_id={self.__client_id}"
        

    def get_access_token(self, auth_code):
        """
        Requests an access token using the provided authorization code.
        Parameters
        ----------
        auth_code : str
            The authorization code obtained from the authorization URL.
        """
        print("Requesting access token...")
        
        data = {
            "grant_type": "authorization_code",
            "code": auth_code,
            "client_id": self.__client_id,
            "client_secret": self.__client_secret,
        }

        response = requests.post(self.__token_url, data=data)

        if response.status_code == 200:
            tokens = response.json()
            self.__access_token = tokens.get("access_token")
        else:
            print("Error getting token:", response.json())

    def get_headers(self):
        """
        Returns the headers for making authenticated requests.
        Returns
        -------
        dict
            The headers for making authenticated requests.
        """
        if self.__access_token:
            return {
                "Authorization": f"Bearer {self.__access_token}",
            }
        else:
            print("No access token available.")
            return None
        
    def __get_client(self, client_data_path):
        client_data = utils.read_config(client_data_path)
        client_secret = client_data["client_secret"]
        client_id = client_data["client_id"]
        return client_id, client_secret