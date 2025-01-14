from propelauth_py import init_base_auth, UnauthorizedException
from streamlit.web.server.websocket_headers import _get_websocket_headers

class Auth:
    def __init__(self, auth_url, integration_api_key):
        self.auth = init_base_auth(auth_url, integration_api_key)
        self.auth_url = auth_url

    def get_user(self):
        access_token = get_access_token()

        if not access_token:
            return None

        try:
            return self.auth.validate_access_token_and_get_user("Bearer " + access_token)
        except UnauthorizedException as err:
            print("Error validating access token", err)
            return None

    def get_account_url(self):
        return self.auth_url + "/account"

def get_access_token():
    headers = _get_websocket_headers()
    if headers is None:
        return None

    cookies = headers.get("Cookie") or headers.get("cookie") or ""
    for cookie in cookies.split(";"):
        split_cookie = cookie.split("=")
        if len(split_cookie) == 2 and split_cookie[0].strip() == "__pa_at":
            return split_cookie[1].strip()

    return None
    
# Configuration, please edit
auth = Auth(
    "https://2333278.propelauthtest.com",
    "ce2621924dfe131dca0e4c04674bcb21f3eef80592330976d91236cc860c4ef3cea03d26412ead5fa818d70934955ca5"
)
