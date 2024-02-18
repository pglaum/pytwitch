from .streams import Streams
import requests


class Twitch:

    __base_url = "https://api.twitch.tv/helix/"
    __debugging = False
    __client_id = ""
    __client_secret = ""
    __access_token = ""

    def __init__(self, client_id, client_secret):
        self.__client_id = client_id
        self.__client_secret = client_secret

        self.streams = Streams(self)

    def get(self, route, params, try_again=False):
        url = self.__base_url + route
        headers = {
            "Client-ID": self.__client_id,
            "Authorization": "Bearer " + self.__access_token,
        }
        res = requests.get(url, headers=headers, params=params)
        if self.__debugging:
            print(res.url)

        if res.status_code == 401:
            if not try_again:
                if self.__debugging:
                    print("Unauthorized, trying to get a new access token")
                self.get_access_token()
                return self.get(route, params, try_again=True)

            raise Exception("Unauthorized (already tried to get a new access token)")

        return res.json()

    def get_access_token(self):
        if self.__debugging:
            print("Getting access token")
        url = "https://id.twitch.tv/oauth2/token"
        params = {
            "client_id": self.__client_id,
            "client_secret": self.__client_secret,
            "grant_type": "client_credentials",
        }
        res = requests.post(url, params=params)
        self.__access_token = res.json()["access_token"]
        return self.__access_token

    def set_access_token(self, access_token):
        self.__access_token = access_token
        return self.__access_token

    def set_debugging(self, debugging):
        self.__debugging = debugging
        return self.__debugging
