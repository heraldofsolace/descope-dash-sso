from dash import Dash
from dash_auth import OIDCAuth
import os
from dotenv import load_dotenv

load_dotenv()

app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True)

auth = OIDCAuth(app, secret_key="aStaticSecretKey!", public_routes=["/"])
auth.register_provider(
    "descope",
    token_endpoint_auth_method="client_secret_post",
    client_id=os.getenv("DESCOPE_CLIENT_ID"),
    client_secret=os.getenv("DESCOPE_CLIENT_SECRET"),
    server_metadata_url="https://api.descope.com/P2sQdG3RMb9A3wikGsti6ZhpN8GM/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"}
)

if __name__ == '__main__':
    app.run(debug=True)
